"""
Swarms Interactive GUI
A comprehensive graphical interface for the Swarms CLI
"""

import os
import sys
import json
import yaml
import webbrowser
import subprocess
from pathlib import Path
from typing import Optional, Tuple, List, Dict, Any
import gradio as gr
from datetime import datetime

# Import Swarms components
try:
    from swarms.cli.main import (
        check_swarms_version,
        check_python_version,
        check_api_keys,
        check_dependencies,
        check_env_file,
        check_workspace_dir,
        run_setup_check,
    )
    from swarms.agents.auto_generate_swarm_config import (
        generate_swarm_config,
    )
    from swarms.agents.create_agents_from_yaml import (
        create_agents_from_yaml,
    )
    from swarms.structs.agent import Agent
    from swarms.structs.agent_loader import AgentLoader
except ImportError as e:
    print(f"Warning: Some Swarms modules could not be imported: {e}")
    print("Some features may not work correctly.")


# Custom CSS for beautiful UI
CUSTOM_CSS = """
.gradio-container {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

.primary-btn {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border: none;
    color: white;
    font-weight: 600;
}

.secondary-btn {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    border: none;
    color: white;
}

.success-box {
    background-color: #d4edda;
    border-color: #c3e6cb;
    color: #155724;
    padding: 12px;
    border-radius: 6px;
    margin: 10px 0;
}

.error-box {
    background-color: #f8d7da;
    border-color: #f5c6cb;
    color: #721c24;
    padding: 12px;
    border-radius: 6px;
    margin: 10px 0;
}

.info-box {
    background-color: #d1ecf1;
    border-color: #bee5eb;
    color: #0c5460;
    padding: 12px;
    border-radius: 6px;
    margin: 10px 0;
}

h1, h2, h3 {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.tab-nav button {
    font-size: 14px;
    font-weight: 600;
}

.yaml-editor {
    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    font-size: 13px;
}
"""


# ============================================================================
# SETUP & DIAGNOSTICS FUNCTIONS
# ============================================================================

def run_environment_check(verbose: bool = False) -> Tuple[str, str]:
    """Run comprehensive environment setup check"""
    try:
        results = []
        results.append("=== Swarms Environment Check ===\n")

        # Python Version
        py_check = check_python_version()
        results.append(f"Python Version: {py_check[1]} {py_check[2]}")

        # Swarms Version
        sw_check = check_swarms_version(verbose)
        results.append(f"Swarms Version: {sw_check[1]} {sw_check[2]}")
        if len(sw_check) > 3:
            results.append(f"Latest Version: {sw_check[3]}")

        # API Keys
        api_check = check_api_keys()
        results.append(f"API Keys: {api_check[1]} {api_check[2]}")

        # Dependencies
        dep_check = check_dependencies()
        results.append(f"Dependencies: {dep_check[1]} {dep_check[2]}")

        # Environment File
        env_check = check_env_file()
        results.append(f"Environment File: {env_check[1]} {env_check[2]}")

        # Workspace Directory
        ws_check = check_workspace_dir()
        results.append(f"Workspace: {ws_check[1]} {ws_check[2]}")

        all_passed = all([
            py_check[0], sw_check[0], api_check[0],
            dep_check[0], env_check[0], ws_check[0]
        ])

        if all_passed:
            status = "✅ All checks passed!"
        else:
            status = "⚠️ Some checks failed. Please review the details."

        return status, "\n".join(results)

    except Exception as e:
        return f"❌ Error: {str(e)}", str(e)


def install_dependencies() -> Tuple[str, str]:
    """Install or upgrade Swarms dependencies"""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "--upgrade", "swarms"],
            capture_output=True,
            text=True,
            timeout=300
        )
        if result.returncode == 0:
            return "✅ Successfully upgraded Swarms!", result.stdout
        else:
            return "❌ Failed to upgrade Swarms", result.stderr
    except Exception as e:
        return f"❌ Error: {str(e)}", str(e)


# ============================================================================
# AGENT CREATION FUNCTIONS
# ============================================================================

def create_single_agent(
    name: str,
    description: str,
    system_prompt: str,
    model_name: str,
    task: str,
    temperature: float = 0.5,
    max_loops: int = 1,
    streaming_on: bool = False,
    verbose: bool = True,
) -> Tuple[str, str]:
    """Create and run a single agent"""
    try:
        if not all([name, description, system_prompt, model_name, task]):
            return "❌ Error", "All fields are required!"

        # Create agent
        agent = Agent(
            agent_name=name,
            agent_description=description,
            system_prompt=system_prompt,
            model_name=model_name,
            temperature=temperature,
            max_loops=max_loops,
            streaming_on=streaming_on,
            verbose=verbose,
        )

        # Run task
        result = agent.run(task)

        return f"✅ Agent '{name}' executed successfully!", str(result)

    except Exception as e:
        return f"❌ Error creating agent", str(e)


def generate_agent_yaml(
    num_agents: int,
    agent_names: str,
    model: str = "gpt-4",
) -> Tuple[str, str]:
    """Generate YAML configuration for agents"""
    try:
        names = [n.strip() for n in agent_names.split(",") if n.strip()]

        if len(names) != num_agents:
            return "❌ Error", f"Please provide exactly {num_agents} agent names separated by commas"

        agents_config = []
        for name in names:
            agent = {
                "agent_name": name,
                "model": {
                    "model_name": model,
                    "temperature": 0.5,
                    "max_tokens": 4000,
                },
                "system_prompt": f"You are {name}, a specialized AI assistant.",
                "max_loops": 1,
                "autosave": True,
                "verbose": True,
                "stopping_token": "<DONE>",
            }
            agents_config.append(agent)

        config = {
            "agents": agents_config,
            "tasks": [f"Analyze and process the given task for {name}" for name in names],
        }

        yaml_str = yaml.dump(config, default_flow_style=False, sort_keys=False)

        # Save to file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"agents_config_{timestamp}.yaml"
        with open(filename, "w") as f:
            f.write(yaml_str)

        return f"✅ YAML configuration generated and saved to {filename}", yaml_str

    except Exception as e:
        return f"❌ Error: {str(e)}", str(e)


# ============================================================================
# SWARM FUNCTIONS
# ============================================================================

def run_agents_from_yaml(yaml_file_path: str) -> Tuple[str, str]:
    """Run agents from YAML configuration"""
    try:
        if not os.path.exists(yaml_file_path):
            return "❌ Error", f"File not found: {yaml_file_path}"

        result = create_agents_from_yaml(
            yaml_file=yaml_file_path,
            return_type="run_swarm"
        )

        return "✅ Agents executed successfully!", str(result)

    except Exception as e:
        return f"❌ Error: {str(e)}", str(e)


def generate_autoswarm(task: str, model: str = "gpt-4") -> Tuple[str, str]:
    """Generate autonomous swarm configuration"""
    try:
        if not task or task.strip() == "":
            return "❌ Error", "Task cannot be empty"

        if not model or model.strip() == "":
            return "❌ Error", "Model name cannot be empty"

        result = generate_swarm_config(task=task, model=model)

        if result:
            return "✅ Swarm configuration generated successfully!", str(result)
        else:
            return "❌ Failed to generate swarm configuration", "No result returned"

    except Exception as e:
        return f"❌ Error: {str(e)}", str(e)


def load_agents_from_markdown(
    markdown_path: str,
    concurrent: bool = True
) -> Tuple[str, str]:
    """Load agents from markdown files"""
    try:
        if not os.path.exists(markdown_path):
            return "❌ Error", f"Path not found: {markdown_path}"

        loader = AgentLoader()

        if os.path.isdir(markdown_path):
            agents = loader.load_multiple_agents(
                markdown_path,
                concurrent=concurrent
            )
        else:
            agents = [loader.load_single_agent(markdown_path)]

        if agents:
            agent_info = "\n".join([
                f"- {getattr(a, 'agent_name', 'Unknown')}: {getattr(a, 'agent_description', 'No description')}"
                for a in agents
            ])
            return f"✅ Loaded {len(agents)} agents successfully!", agent_info
        else:
            return "⚠️ Warning", "No agents were loaded"

    except Exception as e:
        return f"❌ Error: {str(e)}", str(e)


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def open_api_keys_page():
    """Open browser to API keys page"""
    webbrowser.open("https://swarms.world/platform/api-keys")
    return "✅ Opened API keys page in your browser"


def open_docs():
    """Open Swarms documentation"""
    webbrowser.open("https://docs.swarms.world")
    return "✅ Opened documentation in your browser"


def book_strategy_call():
    """Open booking page"""
    webbrowser.open("https://cal.com/swarms/swarms-strategy-session")
    return "✅ Opened booking page in your browser"


def save_yaml_config(yaml_content: str, filename: str) -> str:
    """Save YAML configuration to file"""
    try:
        if not filename:
            filename = f"config_{datetime.now().strftime('%Y%m%d_%H%M%S')}.yaml"

        if not filename.endswith('.yaml') and not filename.endswith('.yml'):
            filename += '.yaml'

        with open(filename, 'w') as f:
            f.write(yaml_content)

        return f"✅ Configuration saved to {filename}"
    except Exception as e:
        return f"❌ Error saving file: {str(e)}"


def load_yaml_file(file_path: str) -> Tuple[str, str]:
    """Load YAML file content"""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        return "✅ File loaded successfully!", content
    except Exception as e:
        return f"❌ Error: {str(e)}", ""


def validate_yaml(yaml_content: str) -> str:
    """Validate YAML syntax"""
    try:
        yaml.safe_load(yaml_content)
        return "✅ YAML is valid!"
    except yaml.YAMLError as e:
        return f"❌ YAML Error: {str(e)}"
    except Exception as e:
        return f"❌ Error: {str(e)}"


# ============================================================================
# GRADIO INTERFACE
# ============================================================================

def create_gui():
    """Create the main Gradio interface"""

    with gr.Blocks(
        title="Swarms Interactive GUI",
        theme=gr.themes.Soft(
            primary_hue="purple",
            secondary_hue="pink",
        ),
        css=CUSTOM_CSS
    ) as app:

        # Header
        gr.Markdown(
            """
            # 🐝 Swarms Interactive GUI
            ### The Ultimate Interface for Multi-Agent Orchestration

            Welcome to the Swarms GUI! This interface provides graphical access to all Swarms CLI functionality.
            """
        )

        # Main Tabs
        with gr.Tabs():

            # ================================================================
            # TAB 1: Environment Setup
            # ================================================================
            with gr.Tab("🔧 Environment Setup"):
                gr.Markdown("### Check and configure your Swarms environment")

                with gr.Row():
                    with gr.Column(scale=1):
                        verbose_check = gr.Checkbox(
                            label="Verbose Output",
                            value=False,
                            info="Show detailed version detection"
                        )
                        check_btn = gr.Button("🔍 Run Environment Check", variant="primary")
                        upgrade_btn = gr.Button("⬆️ Upgrade Swarms", variant="secondary")
                        api_key_btn = gr.Button("🔑 Get API Keys", variant="secondary")
                        docs_btn = gr.Button("📚 Open Documentation", variant="secondary")

                    with gr.Column(scale=2):
                        check_status = gr.Textbox(label="Status", lines=1)
                        check_output = gr.Textbox(label="Details", lines=15)

                check_btn.click(
                    fn=run_environment_check,
                    inputs=[verbose_check],
                    outputs=[check_status, check_output]
                )

                upgrade_btn.click(
                    fn=install_dependencies,
                    outputs=[check_status, check_output]
                )

                api_key_btn.click(
                    fn=open_api_keys_page,
                    outputs=[check_status]
                )

                docs_btn.click(
                    fn=open_docs,
                    outputs=[check_status]
                )

            # ================================================================
            # TAB 2: Single Agent Creator
            # ================================================================
            with gr.Tab("🤖 Create Agent"):
                gr.Markdown("### Create and run a single agent with custom parameters")

                with gr.Row():
                    with gr.Column():
                        agent_name = gr.Textbox(
                            label="Agent Name",
                            placeholder="e.g., Financial Analyst",
                            info="Give your agent a descriptive name"
                        )
                        agent_desc = gr.Textbox(
                            label="Agent Description",
                            placeholder="e.g., Expert in financial analysis and reporting",
                            lines=2
                        )
                        system_prompt = gr.Textbox(
                            label="System Prompt",
                            placeholder="e.g., You are an expert financial analyst...",
                            lines=4,
                            info="Define the agent's role and capabilities"
                        )

                        with gr.Row():
                            model_name = gr.Dropdown(
                                choices=["gpt-4", "gpt-4-turbo", "gpt-3.5-turbo", "claude-3-opus-20240229", "claude-3-sonnet-20240229"],
                                value="gpt-4",
                                label="Model",
                                info="Select the LLM model"
                            )
                            temperature = gr.Slider(
                                minimum=0.0,
                                maximum=2.0,
                                value=0.5,
                                step=0.1,
                                label="Temperature",
                                info="Control randomness (0=focused, 2=creative)"
                            )

                        with gr.Row():
                            max_loops = gr.Number(
                                value=1,
                                label="Max Loops",
                                precision=0,
                                info="Number of reasoning iterations"
                            )
                            streaming = gr.Checkbox(
                                label="Enable Streaming",
                                value=False,
                                info="Stream responses in real-time"
                            )
                            verbose = gr.Checkbox(
                                label="Verbose Mode",
                                value=True,
                                info="Show detailed execution logs"
                            )

                        agent_task = gr.Textbox(
                            label="Task",
                            placeholder="e.g., Analyze the Q4 financial report...",
                            lines=3,
                            info="What should the agent do?"
                        )

                        create_agent_btn = gr.Button("🚀 Create and Run Agent", variant="primary")

                    with gr.Column():
                        agent_status = gr.Textbox(label="Status", lines=1)
                        agent_output = gr.Textbox(label="Agent Output", lines=20)

                create_agent_btn.click(
                    fn=create_single_agent,
                    inputs=[
                        agent_name, agent_desc, system_prompt, model_name,
                        agent_task, temperature, max_loops, streaming, verbose
                    ],
                    outputs=[agent_status, agent_output]
                )

            # ================================================================
            # TAB 3: YAML Configuration
            # ================================================================
            with gr.Tab("📝 YAML Configuration"):
                gr.Markdown("### Generate and edit agent configurations in YAML")

                with gr.Row():
                    with gr.Column(scale=1):
                        gr.Markdown("#### Generate Configuration")
                        num_agents = gr.Slider(
                            minimum=1,
                            maximum=10,
                            value=3,
                            step=1,
                            label="Number of Agents",
                            info="How many agents to configure"
                        )
                        agent_names_input = gr.Textbox(
                            label="Agent Names (comma-separated)",
                            placeholder="e.g., Researcher, Analyst, Writer",
                            info="Enter names separated by commas"
                        )
                        yaml_model = gr.Dropdown(
                            choices=["gpt-4", "gpt-4-turbo", "gpt-3.5-turbo", "claude-3-opus-20240229"],
                            value="gpt-4",
                            label="Default Model"
                        )
                        generate_yaml_btn = gr.Button("⚙️ Generate YAML", variant="primary")

                        gr.Markdown("#### Save Configuration")
                        yaml_filename = gr.Textbox(
                            label="Filename",
                            placeholder="my_agents.yaml",
                            info="Leave empty for auto-generated name"
                        )
                        save_yaml_btn = gr.Button("💾 Save YAML", variant="secondary")
                        validate_btn = gr.Button("✅ Validate YAML", variant="secondary")

                    with gr.Column(scale=2):
                        yaml_status = gr.Textbox(label="Status", lines=1)
                        yaml_editor = gr.Code(
                            label="YAML Configuration",
                            language="yaml",
                            lines=20,
                            value="# Your YAML configuration will appear here"
                        )

                generate_yaml_btn.click(
                    fn=generate_agent_yaml,
                    inputs=[num_agents, agent_names_input, yaml_model],
                    outputs=[yaml_status, yaml_editor]
                )

                save_yaml_btn.click(
                    fn=save_yaml_config,
                    inputs=[yaml_editor, yaml_filename],
                    outputs=[yaml_status]
                )

                validate_btn.click(
                    fn=validate_yaml,
                    inputs=[yaml_editor],
                    outputs=[yaml_status]
                )

            # ================================================================
            # TAB 4: Run Swarms
            # ================================================================
            with gr.Tab("🐝 Run Swarms"):
                gr.Markdown("### Execute multi-agent swarms from YAML configurations")

                with gr.Row():
                    with gr.Column(scale=1):
                        gr.Markdown("#### Run from YAML File")
                        yaml_file_path = gr.Textbox(
                            label="YAML File Path",
                            placeholder="./agents.yaml",
                            info="Path to your YAML configuration file"
                        )
                        run_yaml_btn = gr.Button("▶️ Run Agents from YAML", variant="primary")

                        gr.Markdown("#### Load from Markdown")
                        markdown_path = gr.Textbox(
                            label="Markdown Path",
                            placeholder="./agents/ or ./agent.md",
                            info="Path to markdown file or directory"
                        )
                        concurrent_load = gr.Checkbox(
                            label="Concurrent Loading",
                            value=True,
                            info="Load multiple agents in parallel"
                        )
                        load_md_btn = gr.Button("📖 Load from Markdown", variant="secondary")

                    with gr.Column(scale=2):
                        swarm_status = gr.Textbox(label="Status", lines=1)
                        swarm_output = gr.Textbox(label="Output", lines=20)

                run_yaml_btn.click(
                    fn=run_agents_from_yaml,
                    inputs=[yaml_file_path],
                    outputs=[swarm_status, swarm_output]
                )

                load_md_btn.click(
                    fn=load_agents_from_markdown,
                    inputs=[markdown_path, concurrent_load],
                    outputs=[swarm_status, swarm_output]
                )

            # ================================================================
            # TAB 5: AutoSwarm
            # ================================================================
            with gr.Tab("🤖 AutoSwarm"):
                gr.Markdown("### Generate autonomous swarm configurations using AI")

                with gr.Row():
                    with gr.Column(scale=1):
                        autoswarm_task = gr.Textbox(
                            label="Task Description",
                            placeholder="e.g., Analyze market trends and generate a comprehensive report",
                            lines=5,
                            info="Describe what you want the swarm to accomplish"
                        )
                        autoswarm_model = gr.Dropdown(
                            choices=["gpt-4", "gpt-4-turbo", "gpt-3.5-turbo"],
                            value="gpt-4",
                            label="AI Model",
                            info="Model to use for swarm generation"
                        )
                        autoswarm_btn = gr.Button("🌟 Generate AutoSwarm", variant="primary")

                    with gr.Column(scale=2):
                        autoswarm_status = gr.Textbox(label="Status", lines=1)
                        autoswarm_output = gr.Textbox(label="Generated Configuration", lines=20)

                autoswarm_btn.click(
                    fn=generate_autoswarm,
                    inputs=[autoswarm_task, autoswarm_model],
                    outputs=[autoswarm_status, autoswarm_output]
                )

            # ================================================================
            # TAB 6: Resources & Support
            # ================================================================
            with gr.Tab("📚 Resources"):
                gr.Markdown(
                    """
                    ### Swarms Resources & Community

                    #### 📖 Documentation
                    - [Main Documentation](https://docs.swarms.world)
                    - [API Reference](https://docs.swarms.world/en/latest/swarms/cli/cli_reference/)
                    - [Examples & Tutorials](https://github.com/kyegomez/swarms/tree/master/examples)

                    #### 🛠️ Tools & Platforms
                    - [Swarms Cloud](https://swarms.world)
                    - [Agent Marketplace](https://swarms.world/marketplace)
                    - [GitHub Repository](https://github.com/kyegomez/swarms)

                    #### 💬 Community
                    - [Discord Server](https://discord.gg/EamjgSaEQf)
                    - [LinkedIn](https://linkedin.com/company/swarms)
                    - [YouTube Channel](https://youtube.com/@swarms)

                    #### 🎯 Quick Actions
                    """
                )

                with gr.Row():
                    book_call_btn = gr.Button("📞 Book Strategy Call", variant="primary")
                    github_btn = gr.Button("⭐ Star on GitHub", variant="secondary")
                    discord_btn = gr.Button("💬 Join Discord", variant="secondary")

                resource_status = gr.Textbox(label="Status", lines=1)

                book_call_btn.click(
                    fn=book_strategy_call,
                    outputs=[resource_status]
                )

                github_btn.click(
                    fn=lambda: (webbrowser.open("https://github.com/kyegomez/swarms"), "✅ Opened GitHub repository")[1],
                    outputs=[resource_status]
                )

                discord_btn.click(
                    fn=lambda: (webbrowser.open("https://discord.gg/EamjgSaEQf"), "✅ Opened Discord invite")[1],
                    outputs=[resource_status]
                )

                gr.Markdown(
                    """
                    ---

                    ### 🚀 Getting Started Guide

                    1. **Setup Environment**: Go to the "Environment Setup" tab and run the environment check
                    2. **Get API Keys**: Click "Get API Keys" to retrieve your credentials
                    3. **Create Your First Agent**: Use the "Create Agent" tab to build a custom agent
                    4. **Configure Swarms**: Generate YAML configurations in the "YAML Configuration" tab
                    5. **Run Multi-Agent Systems**: Execute swarms using the "Run Swarms" tab

                    ### 💡 Pro Tips

                    - Use **AutoSwarm** for AI-powered swarm generation
                    - Enable **streaming** for real-time agent responses
                    - Adjust **temperature** to control creativity (lower = more focused)
                    - Use **max_loops** for iterative reasoning tasks
                    - Save your configurations for reuse

                    ### ⚙️ Environment Variables

                    Set these in your `.env` file:
                    ```
                    OPENAI_API_KEY=your_key_here
                    ANTHROPIC_API_KEY=your_key_here
                    WORKSPACE_DIR=/path/to/workspace
                    ```
                    """
                )

        # Footer
        gr.Markdown(
            """
            ---

            <div style='text-align: center; color: #666; font-size: 12px;'>
                <p>Swarms Interactive GUI v1.0 | Built with ❤️ using Gradio</p>
                <p>© 2024 Swarms | <a href='https://docs.swarms.world'>Documentation</a> | <a href='https://github.com/kyegomez/swarms'>GitHub</a></p>
            </div>
            """
        )

    return app


# ============================================================================
# MAIN ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    print("🐝 Starting Swarms Interactive GUI...")
    print("📝 Initializing interface...")

    app = create_gui()

    print("✅ GUI Ready!")
    print("🌐 Launching web interface...")
    print("💡 Access the GUI at: http://localhost:7860")
    print("\n🔧 Press Ctrl+C to stop the server\n")

    # Launch the app
    app.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,  # Set to True to create a public link
        show_error=True,
        quiet=False,
    )
