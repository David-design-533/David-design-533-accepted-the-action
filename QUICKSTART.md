# 快速开始指南 / Quick Start Guide

## 🚀 快速启动 / Quick Launch

### 方法1: 一键安装和运行 / Method 1: One-Click Install & Run

```bash
# 克隆仓库 / Clone repository
git clone https://github.com/David-design-533/David-design-533-accepted-the-action.git
cd David-design-533-accepted-the-action

# 安装 / Install
./install.sh

# 运行 / Run
./run.sh

# 打开浏览器访问 / Open browser
# http://localhost:8000/index.html
```

### 方法2: 手动安装 / Method 2: Manual Installation

```bash
# 1. 安装Python包 / Install Python package
pip install -e .

# 2. 启动服务器 / Start server
python3 lung_visualization/serve.py

# 3. 打开浏览器 / Open browser
# http://localhost:8000/index.html
```

### 方法3: GitHub Codespaces / Method 3: GitHub Codespaces

1. 点击仓库页面的 "Code" 按钮 / Click "Code" button on repository page
2. 选择 "Codespaces" 标签 / Select "Codespaces" tab
3. 点击 "Create codespace on main" / Click "Create codespace on main"
4. 等待环境自动配置完成 / Wait for automatic setup
5. 运行 `./run.sh` 启动服务器 / Run `./run.sh` to start server

### 方法4: VS Code 开发容器 / Method 4: VS Code Dev Container

1. 安装 VS Code 和 "Remote - Containers" 扩展 / Install VS Code and "Remote - Containers" extension
2. 打开项目文件夹 / Open project folder
3. VS Code 会提示"在容器中重新打开" / VS Code will prompt "Reopen in Container"
4. 点击确认，等待容器构建 / Click confirm and wait for container build
5. 容器启动后自动安装依赖 / Dependencies auto-install after container starts

## 📦 代码导入 / Code Import

### 作为Python包使用 / Use as Python Package

```python
# 导入模块 / Import module
from lung_visualization.lung_model import LungModel, export_model_data

# 创建模型实例 / Create model instance
model = LungModel()

# 获取健康基线 / Get healthy baseline
baseline = model.get_baseline_data()

# 模拟吸烟10年 / Simulate 10 years of smoking
data = model.simulate_smoking_stage(10)

# 生成3D几何 / Generate 3D geometry
geometry = model.generate_lung_geometry(data)

# 导出数据 / Export data
export_model_data('output.json')
```

### 在Jupyter Notebook中使用 / Use in Jupyter Notebook

```python
# 1. 安装Jupyter / Install Jupyter
pip install jupyter

# 2. 启动Jupyter / Start Jupyter
jupyter notebook

# 3. 在notebook中导入 / Import in notebook
from lung_visualization.lung_model import LungModel
import json

model = LungModel()
comparison = model.get_comparison_data()

# 显示数据 / Display data
print(json.dumps(comparison['stages'][0]['data'], indent=2))
```

## 🔧 开发环境设置 / Development Environment Setup

### VS Code 配置 / VS Code Configuration

项目已包含完整的VS Code配置：
The project includes complete VS Code configuration:

- **调试配置** / Debug Configurations (`.vscode/launch.json`)
  - 运行演示 / Run demo
  - 运行测试 / Run tests
  - 启动服务器 / Start server
  - 运行当前文件 / Run current file

- **编辑器设置** / Editor Settings (`.vscode/settings.json`)
  - Python路径配置 / Python path
  - 代码格式化 / Code formatting
  - 测试配置 / Test configuration

### Python虚拟环境 / Python Virtual Environment

```bash
# 创建虚拟环境 / Create virtual environment
python3 -m venv .venv

# 激活虚拟环境 / Activate virtual environment
# Linux/Mac:
source .venv/bin/activate

# Windows:
.venv\Scripts\activate

# 安装依赖 / Install dependencies
pip install -e .
pip install -r requirements.txt
```

## 🧪 运行测试 / Run Tests

```bash
# 运行所有测试 / Run all tests
python3 test_lung_visualization.py

# 或使用 pytest / Or use pytest
pytest test_lung_visualization.py -v

# 使用快捷脚本 / Use quick script
./run.sh test
```

## 📊 运行演示 / Run Demonstration

```bash
# 运行完整演示 / Run full demonstration
python3 example_demo.py

# 或使用快捷脚本 / Or use quick script
./run.sh demo
```

## 🌐 Web服务器选项 / Web Server Options

### 使用内置服务器 / Use Built-in Server

```bash
# 方式1: 使用提供的服务器脚本 / Method 1: Use provided server script
python3 lung_visualization/serve.py

# 方式2: 使用Python http.server / Method 2: Use Python http.server
cd lung_visualization
python3 -m http.server 8000

# 方式3: 使用快捷脚本 / Method 3: Use quick script
./run.sh server
```

### 自定义端口 / Custom Port

修改 `lung_visualization/serve.py` 中的 `PORT` 变量
Modify the `PORT` variable in `lung_visualization/serve.py`

```python
PORT = 8080  # 改为你想要的端口 / Change to your desired port
```

## 📱 移动设备访问 / Mobile Device Access

如果在本地网络中访问：
To access from local network:

1. 找到你的本地IP地址 / Find your local IP address:
   ```bash
   # Linux/Mac:
   ifconfig | grep "inet "
   
   # Windows:
   ipconfig
   ```

2. 使用IP地址访问 / Access using IP address:
   ```
   http://YOUR_IP_ADDRESS:8000/index.html
   ```

## 🔍 故障排查 / Troubleshooting

### 端口被占用 / Port Already in Use

```bash
# 查找占用端口的进程 / Find process using port
# Linux/Mac:
lsof -ti:8000

# 终止进程 / Kill process
kill <PID>

# 或使用不同端口 / Or use different port
python3 -m http.server 8080
```

### Python版本问题 / Python Version Issues

```bash
# 检查Python版本 / Check Python version
python3 --version

# 应该是 3.8 或更高 / Should be 3.8 or higher
# 如果不是，请升级Python / If not, upgrade Python
```

### 导入错误 / Import Errors

```bash
# 确保安装了包 / Make sure package is installed
pip install -e .

# 或将项目目录添加到PYTHONPATH / Or add project to PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

## 📚 更多资源 / More Resources

- **项目文档** / Project Documentation: `IMPLEMENTATION.md`
- **模块说明** / Module Documentation: `lung_visualization/README.md`
- **API参考** / API Reference: 查看 `lung_visualization/lung_model.py` 的docstrings

## 💡 使用技巧 / Tips

1. **首次使用** / First Time Use
   - 运行 `./install.sh` 进行完整安装 / Run `./install.sh` for complete setup
   - 运行测试确保一切正常 / Run tests to ensure everything works

2. **开发模式** / Development Mode
   - 使用虚拟环境隔离依赖 / Use virtual environment to isolate dependencies
   - 使用VS Code的调试功能 / Use VS Code debugging features

3. **生产部署** / Production Deployment
   - 考虑使用专业的Web服务器（如nginx） / Consider using professional web server (like nginx)
   - 添加SSL证书用于HTTPS / Add SSL certificate for HTTPS

## 🎯 下一步 / Next Steps

1. ✅ 浏览 Web 界面 / Explore the web interface
2. ✅ 尝试不同的时间点 / Try different time points
3. ✅ 查看API文档学习如何集成 / Check API docs to learn integration
4. ✅ 运行示例代码 / Run example code
5. ✅ 根据需要自定义模型 / Customize model as needed

---

**需要帮助？** / **Need Help?**
- 查看 Issues: https://github.com/David-design-533/David-design-533-accepted-the-action/issues
- 阅读文档: `IMPLEMENTATION.md`
