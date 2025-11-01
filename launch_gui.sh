#!/bin/bash

# Swarms GUI Launch Script
# This script sets up and launches the Swarms Interactive GUI

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}🐝 Swarms Interactive GUI Launcher${NC}"
echo -e "${BLUE}========================================${NC}\n"

# Check Python version
echo -e "${YELLOW}Checking Python version...${NC}"
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
REQUIRED_VERSION="3.10"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" = "$REQUIRED_VERSION" ]; then
    echo -e "${GREEN}✓ Python $PYTHON_VERSION detected${NC}\n"
else
    echo -e "${RED}✗ Python 3.10+ required, but $PYTHON_VERSION found${NC}"
    echo -e "${YELLOW}Please upgrade Python and try again${NC}"
    exit 1
fi

# Check if GUI dependencies are installed
echo -e "${YELLOW}Checking dependencies...${NC}"
if python3 -c "import gradio" 2>/dev/null; then
    echo -e "${GREEN}✓ Gradio installed${NC}"
else
    echo -e "${YELLOW}⚠ Gradio not found. Installing dependencies...${NC}"
    if [ -f "gui_requirements.txt" ]; then
        pip3 install -r gui_requirements.txt
        echo -e "${GREEN}✓ Dependencies installed${NC}\n"
    else
        echo -e "${RED}✗ gui_requirements.txt not found${NC}"
        echo -e "${YELLOW}Installing Gradio directly...${NC}"
        pip3 install gradio>=4.0.0
    fi
fi

# Check if swarms is installed
if python3 -c "import swarms" 2>/dev/null; then
    echo -e "${GREEN}✓ Swarms installed${NC}\n"
else
    echo -e "${YELLOW}⚠ Swarms not found. Installing...${NC}"
    pip3 install swarms
    echo -e "${GREEN}✓ Swarms installed${NC}\n"
fi

# Check for .env file
if [ -f ".env" ]; then
    echo -e "${GREEN}✓ .env file found${NC}"
else
    echo -e "${YELLOW}⚠ .env file not found${NC}"
    echo -e "${YELLOW}Creating sample .env file...${NC}"
    cat > .env << EOF
# Swarms Environment Configuration
# Add your API keys below

# OpenAI
OPENAI_API_KEY=your_openai_key_here

# Anthropic (Claude)
ANTHROPIC_API_KEY=your_anthropic_key_here

# Google
GOOGLE_API_KEY=your_google_key_here

# Workspace Directory
WORKSPACE_DIR=./workspace
EOF
    echo -e "${GREEN}✓ Sample .env created. Please add your API keys.${NC}\n"
fi

# Create workspace directory if it doesn't exist
if [ ! -d "workspace" ]; then
    mkdir -p workspace
    echo -e "${GREEN}✓ Workspace directory created${NC}\n"
fi

# Launch the GUI
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}🚀 Launching Swarms GUI...${NC}"
echo -e "${GREEN}========================================${NC}\n"
echo -e "${BLUE}Access the GUI at: http://localhost:7860${NC}"
echo -e "${BLUE}Press Ctrl+C to stop the server${NC}\n"

# Run the GUI
python3 swarms_gui.py
