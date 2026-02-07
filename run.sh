#!/bin/bash
# Lung Visualization Model - Run Script
# 肺部可视化模型 - 运行脚本

echo "════════════════════════════════════════════════════════════════"
echo "  🫁 Lung Visualization Model - Quick Start"
echo "  肺部可视化模型 - 快速启动"
echo "════════════════════════════════════════════════════════════════"
echo ""

# Check if virtual environment exists
if [ -d ".venv" ]; then
    echo "Activating virtual environment..."
    source .venv/bin/activate
    echo "✓ Virtual environment activated"
    echo ""
fi

# Check what to run
if [ "$1" == "demo" ]; then
    echo "Running demonstration..."
    python3 example_demo.py
elif [ "$1" == "test" ]; then
    echo "Running tests..."
    python3 test_lung_visualization.py
elif [ "$1" == "server" ] || [ -z "$1" ]; then
    echo "Starting web server..."
    echo ""
    python3 lung_visualization/serve.py
else
    echo "Unknown command: $1"
    echo ""
    echo "Usage:"
    echo "  ./run.sh         - Start web server (default)"
    echo "  ./run.sh server  - Start web server"
    echo "  ./run.sh demo    - Run demonstration"
    echo "  ./run.sh test    - Run tests"
    exit 1
fi
