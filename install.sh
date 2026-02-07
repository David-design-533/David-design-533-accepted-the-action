#!/bin/bash
# Lung Visualization Model - Installation Script
# 肺部可视化模型 - 安装脚本

set -e

echo "════════════════════════════════════════════════════════════════"
echo "  🫁 Lung Visualization Model - Installation"
echo "  肺部可视化模型 - 安装"
echo "════════════════════════════════════════════════════════════════"
echo ""

# Check Python version
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    echo "✓ Python detected: $PYTHON_VERSION"
else
    echo "✗ Python 3 not found. Please install Python 3.8 or higher."
    exit 1
fi

# Create virtual environment (optional but recommended)
if [ ! -d ".venv" ]; then
    echo ""
    echo "Creating virtual environment..."
    python3 -m venv .venv
    echo "✓ Virtual environment created"
fi

# Activate virtual environment
echo ""
echo "Activating virtual environment..."
source .venv/bin/activate
echo "✓ Virtual environment activated"

# Upgrade pip
echo ""
echo "Upgrading pip..."
pip install --upgrade pip > /dev/null 2>&1
echo "✓ pip upgraded"

# Install package in development mode
echo ""
echo "Installing lung-visualization package..."
pip install -e . > /dev/null 2>&1
echo "✓ Package installed in development mode"

# Install optional dev dependencies
echo ""
echo "Installing development dependencies..."
pip install -r requirements.txt > /dev/null 2>&1
echo "✓ Development dependencies installed"

# Run tests to verify installation
echo ""
echo "Running tests to verify installation..."
python3 test_lung_visualization.py
TEST_RESULT=$?

echo ""
echo "════════════════════════════════════════════════════════════════"
if [ $TEST_RESULT -eq 0 ]; then
    echo "  ✅ Installation successful!"
    echo ""
    echo "  Quick Start:"
    echo "  1. Activate virtual environment: source .venv/bin/activate"
    echo "  2. Start server: python3 lung_visualization/serve.py"
    echo "  3. Or use: ./run.sh"
    echo "  4. Open browser: http://localhost:8000/index.html"
else
    echo "  ⚠️  Installation completed but tests failed"
    echo "  Please check the error messages above"
fi
echo "════════════════════════════════════════════════════════════════"
echo ""
