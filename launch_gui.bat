@echo off
REM Swarms GUI Launch Script for Windows
REM This script sets up and launches the Swarms Interactive GUI

echo ========================================
echo 🐝 Swarms Interactive GUI Launcher
echo ========================================
echo.

REM Check if Python is installed
echo Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ✗ Python not found. Please install Python 3.10+ from python.org
    pause
    exit /b 1
)
echo ✓ Python detected
echo.

REM Check if Gradio is installed
echo Checking dependencies...
python -c "import gradio" >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠ Gradio not found. Installing dependencies...
    if exist gui_requirements.txt (
        pip install -r gui_requirements.txt
        echo ✓ Dependencies installed
    ) else (
        echo Installing Gradio directly...
        pip install gradio>=4.0.0
    )
) else (
    echo ✓ Gradio installed
)
echo.

REM Check if Swarms is installed
python -c "import swarms" >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠ Swarms not found. Installing...
    pip install swarms
    echo ✓ Swarms installed
) else (
    echo ✓ Swarms installed
)
echo.

REM Check for .env file
if not exist .env (
    echo ⚠ .env file not found
    echo Creating sample .env file...
    (
        echo # Swarms Environment Configuration
        echo # Add your API keys below
        echo.
        echo # OpenAI
        echo OPENAI_API_KEY=your_openai_key_here
        echo.
        echo # Anthropic (Claude^)
        echo ANTHROPIC_API_KEY=your_anthropic_key_here
        echo.
        echo # Google
        echo GOOGLE_API_KEY=your_google_key_here
        echo.
        echo # Workspace Directory
        echo WORKSPACE_DIR=./workspace
    ) > .env
    echo ✓ Sample .env created. Please add your API keys.
) else (
    echo ✓ .env file found
)
echo.

REM Create workspace directory
if not exist workspace (
    mkdir workspace
    echo ✓ Workspace directory created
)
echo.

REM Launch the GUI
echo ========================================
echo 🚀 Launching Swarms GUI...
echo ========================================
echo.
echo Access the GUI at: http://localhost:7860
echo Press Ctrl+C to stop the server
echo.

python swarms_gui.py

pause
