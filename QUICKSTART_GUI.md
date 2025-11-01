# 🚀 Swarms GUI Quick Start Guide

Get up and running with the Swarms Interactive GUI in under 5 minutes!

## 📋 Prerequisites

Before you begin, ensure you have:

- ✅ **Python 3.10+** installed ([Download](https://www.python.org/downloads/))
- ✅ **pip** package manager (comes with Python)
- ✅ **Internet connection** for API calls
- ✅ **API Keys** from OpenAI, Anthropic, or other providers

## ⚡ Quick Installation

### Option 1: Automated Launch (Recommended)

**Linux/macOS:**
```bash
# Navigate to swarms directory
cd swarms

# Make the script executable (first time only)
chmod +x launch_gui.sh

# Launch the GUI
./launch_gui.sh
```

**Windows:**
```cmd
# Navigate to swarms directory
cd swarms

# Launch the GUI
launch_gui.bat
```

The launch script will automatically:
- ✅ Check Python version
- ✅ Install missing dependencies
- ✅ Create .env file template
- ✅ Start the GUI server

### Option 2: Manual Installation

```bash
# Install dependencies
pip install -r gui_requirements.txt

# Or install manually
pip install gradio>=4.0.0 swarms>=8.0.0

# Launch the GUI
python swarms_gui.py
```

## 🔑 Setup API Keys

### Step 1: Create .env File

Create a file named `.env` in the swarms directory:

```bash
# OpenAI (for GPT models)
OPENAI_API_KEY=sk-your-key-here

# Anthropic (for Claude models)
ANTHROPIC_API_KEY=sk-ant-your-key-here

# Google (for Gemini models)
GOOGLE_API_KEY=your-key-here

# Workspace directory
WORKSPACE_DIR=./workspace
```

### Step 2: Get Your API Keys

1. **OpenAI**: [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. **Anthropic**: [console.anthropic.com](https://console.anthropic.com)
3. **Google**: [makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)

Or use the GUI's built-in "Get API Keys" button!

## 🎯 First Steps

### 1. Access the GUI

Once launched, open your browser to:
```
http://localhost:7860
```

The GUI should automatically open in your default browser.

### 2. Run Environment Check

1. Go to the **"🔧 Environment Setup"** tab
2. Click **"🔍 Run Environment Check"**
3. Review the status of all components
4. Fix any issues highlighted in red or yellow

### 3. Create Your First Agent

1. Navigate to **"🤖 Create Agent"** tab
2. Fill in the form:
   - **Name**: `My First Agent`
   - **Description**: `A helpful assistant`
   - **System Prompt**: `You are a helpful AI assistant`
   - **Model**: `gpt-4` or `gpt-3.5-turbo`
   - **Task**: `Tell me a joke about programming`
3. Click **"🚀 Create and Run Agent"**
4. Watch your agent in action!

### 4. Try AutoSwarm (Advanced)

1. Go to **"🤖 AutoSwarm"** tab
2. Enter a complex task:
   ```
   Research the latest trends in AI, summarize findings,
   and create a presentation outline
   ```
3. Select a model (GPT-4 recommended)
4. Click **"🌟 Generate AutoSwarm"**
5. Watch as AI creates a multi-agent configuration!

## 🎨 GUI Overview

### Available Tabs

| Tab | Purpose | Key Features |
|-----|---------|--------------|
| 🔧 Environment Setup | Diagnostics & configuration | Version checks, upgrades, API key management |
| 🤖 Create Agent | Single agent creation | Full parameter control, instant execution |
| 📝 YAML Configuration | Multi-agent configs | Visual generator, syntax validation |
| 🐝 Run Swarms | Execute multi-agent systems | YAML & Markdown loading |
| 🌟 AutoSwarm | AI-powered swarm generation | Automatic architecture design |
| 📚 Resources | Docs & support | Links, tutorials, community |

## 💡 Common Use Cases

### Use Case 1: Simple Question Answering

```
Tab: Create Agent
Name: Q&A Assistant
Task: What is quantum computing?
```

### Use Case 2: Content Generation

```
Tab: Create Agent
Name: Blog Writer
System Prompt: You are an expert content writer
Task: Write a blog post about sustainable energy
Temperature: 0.8 (more creative)
```

### Use Case 3: Data Analysis

```
Tab: AutoSwarm
Task: Analyze sales data, identify trends, create visualizations,
      and generate executive summary
```

### Use Case 4: Research Assistant

```
Tab: YAML Configuration
Generate: 3 agents (Researcher, Analyst, Writer)
Then: Run Swarms tab → Execute configuration
```

## 🔧 Troubleshooting

### GUI Won't Start

**Problem**: Port 7860 already in use

**Solution**:
```python
# Edit swarms_gui.py, change the port:
app.launch(
    server_port=7861,  # Change to any available port
    ...
)
```

### API Key Errors

**Problem**: "No API key found"

**Solution**:
1. Check `.env` file exists
2. Verify API keys are correct (no quotes needed)
3. Restart the GUI after adding keys

### Import Errors

**Problem**: "ModuleNotFoundError: No module named 'gradio'"

**Solution**:
```bash
pip install --upgrade gradio swarms
```

### Connection Issues

**Problem**: Can't access http://localhost:7860

**Solution**:
1. Check if the server started (look for "Running on..." message)
2. Try http://127.0.0.1:7860
3. Check firewall settings
4. Restart the GUI

## 📱 Access from Other Devices

### On Your Network

```python
# Edit swarms_gui.py:
app.launch(
    server_name="0.0.0.0",  # Allow network access
    server_port=7860,
)
```

Then access from other devices:
```
http://YOUR_COMPUTER_IP:7860
```

Find your IP:
- **Linux/Mac**: `ifconfig` or `ip addr`
- **Windows**: `ipconfig`

### Public Access (Temporary)

```python
# Edit swarms_gui.py:
app.launch(
    share=True,  # Creates a public URL
)
```

⚠️ **Warning**: Public URLs expire after 72 hours.

## 🎓 Next Steps

### Beginner Track
1. ✅ Complete environment setup
2. ✅ Create your first agent
3. ✅ Try different models and temperatures
4. ✅ Experiment with system prompts
5. ✅ Save successful configurations

### Intermediate Track
1. ✅ Generate YAML configurations
2. ✅ Run multi-agent swarms
3. ✅ Load agents from markdown
4. ✅ Use AutoSwarm for complex tasks
5. ✅ Optimize agent parameters

### Advanced Track
1. ✅ Design custom swarm architectures
2. ✅ Integrate with external tools
3. ✅ Deploy to production
4. ✅ Build specialized agent teams
5. ✅ Contribute to the project

## 📚 Learning Resources

### Documentation
- **Main Docs**: [docs.swarms.world](https://docs.swarms.world)
- **API Reference**: [docs.swarms.world/api](https://docs.swarms.world/en/latest/swarms/cli/cli_reference/)
- **GUI README**: `GUI_README.md`

### Video Tutorials
- **Getting Started**: [YouTube Playlist](https://youtube.com/@swarms)
- **Advanced Patterns**: Coming soon!

### Community
- **Discord**: [Join our community](https://discord.gg/EamjgSaEQf)
- **GitHub**: [Star the repo](https://github.com/kyegomez/swarms)

## ⚡ Pro Tips

1. **Start Simple**: Begin with single agents before building swarms
2. **Use Templates**: Save successful configurations for reuse
3. **Monitor Costs**: Enable verbose mode to track API usage
4. **Test Incrementally**: Validate each agent before combining
5. **Read Docs**: Check [docs.swarms.world](https://docs.swarms.world) for advanced features

## 🎯 Quick Reference

### Environment Variables
```bash
OPENAI_API_KEY        # OpenAI API key
ANTHROPIC_API_KEY     # Anthropic API key
GOOGLE_API_KEY        # Google API key
WORKSPACE_DIR         # Working directory for agents
```

### Model Options
- `gpt-4` - Most capable, slower, more expensive
- `gpt-4-turbo` - Faster GPT-4 variant
- `gpt-3.5-turbo` - Fast, economical, good for simple tasks
- `claude-3-opus-20240229` - Anthropic's most capable
- `claude-3-sonnet-20240229` - Balanced performance

### Temperature Guide
- `0.0-0.3` - Focused, deterministic (analysis, factual)
- `0.4-0.7` - Balanced (general use)
- `0.8-1.0` - Creative (writing, brainstorming)
- `1.1-2.0` - Highly creative (experimental)

### Useful Commands
```bash
# Launch GUI
python swarms_gui.py

# Install dependencies
pip install -r gui_requirements.txt

# Upgrade Swarms
pip install --upgrade swarms

# Check version
python -c "import swarms; print(swarms.__version__)"
```

## 💬 Get Help

### Having Issues?

1. **Check the logs** in the terminal where GUI is running
2. **Review the FAQ** in `GUI_README.md`
3. **Search issues** on [GitHub](https://github.com/kyegomez/swarms/issues)
4. **Ask on Discord** at [discord.gg/EamjgSaEQf](https://discord.gg/EamjgSaEQf)
5. **Book a call** for enterprise support

### Report a Bug

1. Go to [GitHub Issues](https://github.com/kyegomez/swarms/issues)
2. Click "New Issue"
3. Provide:
   - Python version
   - Swarms version
   - Error message
   - Steps to reproduce

## 🎉 Success!

You're now ready to build powerful multi-agent systems with the Swarms GUI!

**Next**: Try creating your first multi-agent swarm in the YAML Configuration tab.

---

<div align="center">

**Happy Swarming! 🐝**

[📖 Full Documentation](GUI_README.md) | [🌟 Star on GitHub](https://github.com/kyegomez/swarms) | [💬 Join Discord](https://discord.gg/EamjgSaEQf)

</div>
