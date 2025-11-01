# 🐝 Swarms Interactive GUI

## Overview

The **Swarms Interactive GUI** is a comprehensive web-based graphical interface that provides full access to all Swarms CLI functionality through an intuitive, user-friendly interface. Built with Gradio, it offers a modern, responsive design perfect for both beginners and advanced users.

![Swarms GUI](https://img.shields.io/badge/Swarms-GUI-purple?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge)
![Gradio](https://img.shields.io/badge/Gradio-4.0+-orange?style=for-the-badge)

## ✨ Features

### 🔧 Environment Setup
- **Comprehensive diagnostics** - Check Python version, Swarms version, API keys, dependencies, and more
- **One-click upgrades** - Update Swarms to the latest version with a single click
- **Quick access** - Direct links to API key management and documentation
- **Verbose debugging** - Detailed output for troubleshooting

### 🤖 Single Agent Creation
- **Interactive agent builder** - Create custom agents with a visual form
- **Full parameter control** - Configure model, temperature, max loops, streaming, and more
- **Real-time execution** - Run tasks and see results immediately
- **Multiple model support** - GPT-4, Claude, and other LLMs

### 📝 YAML Configuration
- **Visual YAML generator** - Create multi-agent configurations without writing YAML
- **Syntax validation** - Check YAML syntax before saving
- **Live editor** - Edit configurations with syntax highlighting
- **Auto-save** - Timestamp-based automatic file naming

### 🐝 Multi-Agent Swarms
- **Run from YAML** - Execute pre-configured swarms
- **Markdown loading** - Import agents from markdown files
- **Concurrent processing** - Run multiple agents in parallel
- **Progress tracking** - Monitor swarm execution in real-time

### 🌟 AutoSwarm
- **AI-powered generation** - Automatically create swarm configurations from task descriptions
- **Intelligent agent design** - AI determines optimal agent architecture
- **Model selection** - Choose which LLM powers the generation
- **Export configurations** - Save generated configs for reuse

### 📚 Resources & Support
- **Quick links** - Access documentation, marketplace, and community
- **Strategy calls** - Book consultations directly from the GUI
- **Getting started guide** - In-app tutorials and tips
- **Community integration** - Direct links to Discord, GitHub, and more

## 🚀 Installation

### Prerequisites

- Python 3.10 or higher
- pip package manager
- An active internet connection

### Quick Install

```bash
# Clone the repository (if not already done)
git clone https://github.com/kyegomez/swarms.git
cd swarms

# Install GUI dependencies
pip install -r gui_requirements.txt

# Or install manually
pip install gradio>=4.0.0 swarms>=8.0.0
```

## 🎯 Usage

### Starting the GUI

```bash
# From the swarms directory
python swarms_gui.py
```

The GUI will start and automatically open in your default browser at `http://localhost:7860`

### Alternative Launch Methods

```bash
# With custom port
python swarms_gui.py --port 8080

# Share publicly (creates a temporary public URL)
# Modify the launch() call in swarms_gui.py to set share=True
```

## 📖 User Guide

### Tab 1: Environment Setup

**Purpose**: Verify and configure your Swarms environment

**Steps**:
1. Click **"Run Environment Check"** to diagnose your setup
2. Review the status messages
3. Click **"Upgrade Swarms"** if an update is available
4. Click **"Get API Keys"** to retrieve credentials
5. Use **Verbose Output** for detailed diagnostics

**Checks Performed**:
- ✅ Python version (3.10+ required)
- ✅ Swarms version (latest recommended)
- ✅ API keys (OpenAI, Anthropic, etc.)
- ✅ Dependencies (torch, transformers, etc.)
- ✅ Environment file (.env)
- ✅ Workspace directory

### Tab 2: Create Agent

**Purpose**: Build and run a single custom agent

**Steps**:
1. **Agent Name**: Give your agent a descriptive name
2. **Description**: Describe what the agent does
3. **System Prompt**: Define the agent's role and capabilities
4. **Model**: Select the LLM (GPT-4, Claude, etc.)
5. **Temperature**: Adjust creativity (0=focused, 2=creative)
6. **Max Loops**: Set reasoning iterations
7. **Task**: Enter what you want the agent to do
8. Click **"Create and Run Agent"**

**Example Configuration**:
```
Name: Financial Analyst
Description: Expert in analyzing financial data and creating reports
System Prompt: You are an expert financial analyst with 20 years of experience...
Model: gpt-4
Temperature: 0.3
Max Loops: 1
Task: Analyze the Q4 2023 earnings report and summarize key findings
```

### Tab 3: YAML Configuration

**Purpose**: Create and edit multi-agent configurations

**Generate YAML**:
1. Set **Number of Agents** (1-10)
2. Enter **Agent Names** (comma-separated)
3. Select **Default Model**
4. Click **"Generate YAML"**

**Edit & Save**:
1. Modify the YAML in the editor
2. Click **"Validate YAML"** to check syntax
3. Enter a **Filename** (optional)
4. Click **"Save YAML"**

**Example Generated YAML**:
```yaml
agents:
  - agent_name: Researcher
    model:
      model_name: gpt-4
      temperature: 0.5
      max_tokens: 4000
    system_prompt: You are Researcher, a specialized AI assistant.
    max_loops: 1
    autosave: true
```

### Tab 4: Run Swarms

**Purpose**: Execute multi-agent systems

**From YAML File**:
1. Enter the **YAML File Path** (e.g., `./agents.yaml`)
2. Click **"Run Agents from YAML"**
3. View results in the output panel

**From Markdown**:
1. Enter **Markdown Path** (file or directory)
2. Enable/disable **Concurrent Loading**
3. Click **"Load from Markdown"**

**Markdown Format**:
```markdown
---
name: Agent Name
description: Agent Description
model_name: gpt-4
temperature: 0.1
---

System prompt content here...
```

### Tab 5: AutoSwarm

**Purpose**: AI-powered swarm generation

**Steps**:
1. Enter detailed **Task Description**
2. Select **AI Model** for generation
3. Click **"Generate AutoSwarm"**
4. Review and save the generated configuration

**Example Task**:
```
Analyze market trends across multiple sectors, identify investment
opportunities, perform risk assessment, and generate a comprehensive
investment strategy report with specific recommendations.
```

The AI will automatically:
- Determine optimal number of agents
- Design agent specializations
- Create task distribution
- Generate complete YAML configuration

### Tab 6: Resources

**Purpose**: Access documentation and community

**Quick Actions**:
- **Book Strategy Call**: Schedule a consultation
- **Star on GitHub**: Support the project
- **Join Discord**: Connect with the community

**Links Provided**:
- Documentation & API reference
- Examples & tutorials
- Swarms Cloud platform
- Agent marketplace
- Community channels

## 🎨 GUI Features

### Beautiful Design
- Modern, responsive interface
- Gradient color scheme (purple/pink)
- Intuitive tab navigation
- Real-time status updates
- Syntax-highlighted code editor

### User Experience
- **Progressive disclosure**: Simple by default, advanced when needed
- **Helpful tooltips**: Contextual information for every field
- **Clear feedback**: Success/error messages with details
- **Auto-saving**: Configurations saved with timestamps
- **Validation**: Real-time YAML syntax checking

### Accessibility
- **Keyboard navigation**: Full keyboard support
- **Screen reader friendly**: Semantic HTML
- **High contrast**: Readable in all lighting conditions
- **Mobile responsive**: Works on tablets and phones

## 🔧 Configuration

### Environment Variables

Create a `.env` file in your project root:

```bash
# LLM API Keys
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GOOGLE_API_KEY=...
COHERE_API_KEY=...

# Workspace
WORKSPACE_DIR=/path/to/your/workspace

# Optional
SWARMS_API_KEY=...
```

### Custom Styling

Modify the `CUSTOM_CSS` variable in `swarms_gui.py` to customize colors, fonts, and layout.

### Port Configuration

Change the default port by modifying the `server_port` parameter in the `app.launch()` call:

```python
app.launch(
    server_name="0.0.0.0",
    server_port=8080,  # Change this
    share=False,
)
```

## 🐛 Troubleshooting

### Common Issues

**Issue**: GUI won't start
```bash
# Solution: Check Python version
python --version  # Should be 3.10+

# Reinstall dependencies
pip install --upgrade -r gui_requirements.txt
```

**Issue**: Import errors
```bash
# Solution: Install Swarms
pip install --upgrade swarms

# Or install from source
pip install -e .
```

**Issue**: API key errors
```bash
# Solution: Check .env file
cat .env

# Ensure API keys are set
export OPENAI_API_KEY=sk-...
```

**Issue**: YAML validation fails
- Check for proper indentation (use spaces, not tabs)
- Ensure all strings are properly quoted
- Validate at [yamllint.com](http://www.yamllint.com/)

**Issue**: Port already in use
```bash
# Solution: Use a different port
# Edit swarms_gui.py and change server_port to 7861 or higher
```

### Debug Mode

Enable verbose logging:

```python
# In swarms_gui.py, modify launch():
app.launch(
    ...
    show_error=True,
    quiet=False,
)
```

## 🚢 Deployment

### Local Network Access

```python
# Allow access from other devices on your network
app.launch(
    server_name="0.0.0.0",  # Listen on all interfaces
    server_port=7860,
    share=False,
)
```

Access from other devices: `http://YOUR_IP:7860`

### Public Access (Temporary)

```python
# Create a temporary public URL
app.launch(
    server_name="0.0.0.0",
    server_port=7860,
    share=True,  # Creates a public gradio.live link
)
```

⚠️ **Warning**: Public links expire after 72 hours and should not be used for production.

### Production Deployment

For production, consider:
- **Docker**: Use the included Dockerfile
- **Nginx**: Reverse proxy for SSL/TLS
- **Authentication**: Add login requirements
- **Rate limiting**: Prevent abuse
- **Monitoring**: Track usage and errors

Example Docker deployment:
```bash
# Build Docker image
docker build -t swarms-gui .

# Run container
docker run -p 7860:7860 -v $(pwd)/.env:/app/.env swarms-gui
```

## 📊 Performance

### Optimization Tips

1. **Concurrent Processing**: Enable for faster multi-agent execution
2. **Streaming**: Use for real-time responses on long tasks
3. **Model Selection**: GPT-3.5-turbo is faster than GPT-4
4. **Caching**: Results are cached where possible
5. **Resource Limits**: Set max_loops to prevent infinite execution

### Resource Requirements

- **RAM**: 2GB minimum, 4GB recommended
- **CPU**: 2+ cores recommended
- **Network**: Stable internet for API calls
- **Storage**: 500MB for installation

## 🤝 Contributing

We welcome contributions! Here's how:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**
4. **Test thoroughly**
5. **Commit**: `git commit -m 'Add amazing feature'`
6. **Push**: `git push origin feature/amazing-feature`
7. **Open a Pull Request**

### Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/swarms.git
cd swarms

# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/

# Start GUI in dev mode
python swarms_gui.py
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Swarms Team**: For the incredible multi-agent framework
- **Gradio**: For the amazing GUI framework
- **Community**: For feedback and contributions

## 📞 Support

### Getting Help

- **Documentation**: [docs.swarms.world](https://docs.swarms.world)
- **Discord**: [Join our community](https://discord.gg/EamjgSaEQf)
- **GitHub Issues**: [Report bugs](https://github.com/kyegomez/swarms/issues)
- **Email**: support@swarms.world

### Enterprise Support

Need enterprise support? [Book a strategy call](https://cal.com/swarms/swarms-strategy-session)

## 🗺️ Roadmap

### Upcoming Features

- [ ] Real-time collaboration (multi-user)
- [ ] Agent performance analytics
- [ ] Visual swarm designer (drag-and-drop)
- [ ] Pre-built agent templates
- [ ] Cost tracking and budgeting
- [ ] Export to various formats (JSON, Python, etc.)
- [ ] Integration with Swarms Cloud
- [ ] Mobile app version
- [ ] Dark mode theme
- [ ] Multi-language support

### Version History

- **v1.0.0** (Current)
  - Initial release
  - All CLI commands supported
  - Modern Gradio interface
  - Comprehensive documentation

## 💡 Tips & Tricks

### Best Practices

1. **Start Simple**: Create single agents before building swarms
2. **Test Incrementally**: Validate each agent before combining
3. **Use Templates**: Save successful configurations for reuse
4. **Monitor Costs**: Track API usage with verbose mode
5. **Version Control**: Keep configurations in git

### Power User Features

```python
# Custom agent configurations
agent = Agent(
    agent_name="SuperAgent",
    model_name="gpt-4",
    temperature=0.7,
    max_loops=5,
    streaming_on=True,
    dynamic_temperature_enabled=True,
    retry_attempts=3,
    context_length=8000,
)
```

### Keyboard Shortcuts

- **Ctrl+Enter**: Submit form
- **Tab**: Navigate between fields
- **Shift+Tab**: Navigate backwards
- **Esc**: Close modals

## 🎓 Learning Resources

### Tutorials

1. **Getting Started**: Environment setup and first agent
2. **YAML Mastery**: Advanced configuration techniques
3. **Swarm Patterns**: Common multi-agent architectures
4. **AutoSwarm Guide**: Leveraging AI for swarm design
5. **Production Deploy**: Taking swarms to production

### Example Projects

- **Research Assistant**: Multi-agent research system
- **Content Creation**: Automated content pipeline
- **Data Analysis**: Multi-step data processing
- **Customer Support**: Intelligent support bot swarm

### Video Tutorials

- [YouTube Playlist](https://youtube.com/@swarms)
- [Getting Started Guide](https://youtube.com/@swarms)
- [Advanced Patterns](https://youtube.com/@swarms)

## 📚 Additional Resources

- [Swarms Documentation](https://docs.swarms.world)
- [API Reference](https://docs.swarms.world/en/latest/swarms/cli/cli_reference/)
- [GitHub Repository](https://github.com/kyegomez/swarms)
- [Example Projects](https://github.com/kyegomez/swarms/tree/master/examples)
- [Agent Marketplace](https://swarms.world/marketplace)

---

<div align="center">

**Built with ❤️ by the Swarms Community**

[⭐ Star on GitHub](https://github.com/kyegomez/swarms) | [📖 Read the Docs](https://docs.swarms.world) | [💬 Join Discord](https://discord.gg/EamjgSaEQf)

</div>
