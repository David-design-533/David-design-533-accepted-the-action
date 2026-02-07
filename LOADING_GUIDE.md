# 代码加载完全指南 / Complete Code Loading Guide

本文档提供了将肺部可视化模型加载到各种代码空间的详细步骤。
This document provides detailed steps for loading the lung visualization model into various code spaces.

---

## 🎯 目录 / Table of Contents

1. [GitHub Codespaces（推荐）](#github-codespaces)
2. [VS Code开发容器](#vs-code-dev-container)
3. [本地开发环境](#local-development)
4. [Jupyter Notebook](#jupyter-notebook)
5. [Python脚本导入](#python-script-import)
6. [Docker容器](#docker-container)
7. [常见问题](#troubleshooting)

---

## 1. GitHub Codespaces（推荐） <a name="github-codespaces"></a>

### 优点 / Advantages
- ✅ 无需本地安装任何软件
- ✅ 完全在浏览器中运行
- ✅ 自动配置开发环境
- ✅ 所有依赖自动安装

### 步骤 / Steps

#### 方法A: 通过网页界面 / Via Web Interface

1. **访问仓库页面**
   ```
   https://github.com/David-design-533/David-design-533-accepted-the-action
   ```

2. **点击绿色 "Code" 按钮**
   
3. **选择 "Codespaces" 标签**

4. **点击 "Create codespace on main"**

5. **等待环境构建**（首次约2-3分钟）
   - 自动安装Python 3.12
   - 自动安装Node.js
   - 自动安装项目依赖
   - 自动配置端口转发

6. **环境就绪后，运行**
   ```bash
   ./run.sh
   ```

7. **浏览器会自动弹出端口转发通知**
   - 点击 "Open in Browser" 查看可视化界面

#### 方法B: 通过命令行 / Via Command Line

```bash
# 安装GitHub CLI（如果没有）
# https://cli.github.com/

# 创建Codespace
gh codespace create -R David-design-533/David-design-533-accepted-the-action

# 连接到Codespace
gh codespace ssh

# 运行项目
./run.sh
```

#### 方法C: 一键链接 / One-Click Link

点击此徽章直接打开：
Click this badge to open directly:

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=David-design-533/David-design-533-accepted-the-action)

### 配置说明 / Configuration

Codespace配置文件：`.devcontainer/devcontainer.json`

主要配置：
- **基础镜像**: Python 3.12 Dev Container
- **扩展**: Python, Pylance, Jupyter
- **端口转发**: 8000 (主服务器), 8080 (备用)
- **自动命令**: `postCreateCommand` 自动安装依赖

---

## 2. VS Code开发容器 <a name="vs-code-dev-container"></a>

### 优点 / Advantages
- ✅ 本地运行，性能更好
- ✅ 完全隔离的开发环境
- ✅ 与团队共享一致的环境
- ✅ 支持GPU（如果需要）

### 前提条件 / Prerequisites

1. 安装 [Visual Studio Code](https://code.visualstudio.com/)
2. 安装 [Docker Desktop](https://www.docker.com/products/docker-desktop)
3. 安装 VS Code 扩展: "Remote - Containers"

### 步骤 / Steps

1. **克隆仓库**
   ```bash
   git clone https://github.com/David-design-533/David-design-533-accepted-the-action.git
   cd David-design-533-accepted-the-action
   ```

2. **在VS Code中打开**
   ```bash
   code .
   ```

3. **VS Code会检测到 `.devcontainer` 配置**
   - 会在右下角弹出提示：
     "Folder contains a Dev Container configuration file..."
   
4. **点击 "Reopen in Container"**
   - 或使用命令面板 (F1): "Remote-Containers: Reopen in Container"

5. **等待容器构建**（首次约5-10分钟）
   - 下载基础镜像
   - 安装依赖
   - 配置环境

6. **容器就绪后，使用调试功能**
   - 按 `F5` 启动调试
   - 选择调试配置：
     - "Python: Start Web Server"
     - "Python: Run Tests"
     - "Python: Lung Model Demo"

### 调试配置 / Debug Configurations

`.vscode/launch.json` 提供了4种调试模式：

1. **启动Web服务器**
   - 自动打开浏览器
   - 支持断点调试
   
2. **运行演示**
   - 查看完整演示输出
   
3. **运行测试**
   - 调试单元测试
   
4. **运行当前文件**
   - 快速测试任意Python文件

---

## 3. 本地开发环境 <a name="local-development"></a>

### 优点 / Advantages
- ✅ 最快的执行速度
- ✅ 完全控制
- ✅ 可以使用任何编辑器
- ✅ 离线工作

### 步骤 / Steps

#### 快速安装 / Quick Install

```bash
# 1. 克隆仓库
git clone https://github.com/David-design-533/David-design-533-accepted-the-action.git
cd David-design-533-accepted-the-action

# 2. 运行一键安装
./install.sh

# 3. 启动项目
./run.sh
```

#### 手动安装 / Manual Install

```bash
# 1. 克隆仓库
git clone https://github.com/David-design-533/David-design-533-accepted-the-action.git
cd David-design-533-accepted-the-action

# 2. 创建虚拟环境
python3 -m venv .venv

# 3. 激活虚拟环境
# Linux/Mac:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate

# 4. 安装包
pip install -e .

# 5. 安装开发依赖（可选）
pip install -r requirements.txt

# 6. 运行测试验证
python3 test_lung_visualization.py

# 7. 启动服务器
python3 lung_visualization/serve.py
```

### 系统要求 / System Requirements

- **Python**: 3.8 或更高版本
- **操作系统**: Windows, macOS, Linux
- **内存**: 最少 512MB
- **磁盘**: 最少 100MB

---

## 4. Jupyter Notebook <a name="jupyter-notebook"></a>

### 优点 / Advantages
- ✅ 交互式探索
- ✅ 可视化数据分析
- ✅ 逐步执行代码
- ✅ 保存结果和可视化

### 步骤 / Steps

1. **安装Jupyter**
   ```bash
   pip install jupyter
   ```

2. **启动Jupyter Notebook**
   ```bash
   cd David-design-533-accepted-the-action
   jupyter notebook
   ```

3. **创建新的Notebook**
   - 点击 "New" → "Python 3"

4. **导入和使用**
   ```python
   # Cell 1: 导入模块
   from lung_visualization.lung_model import LungModel
   import json
   
   # Cell 2: 创建模型
   model = LungModel()
   
   # Cell 3: 获取健康基线
   baseline = model.get_baseline_data()
   print(json.dumps(baseline, indent=2))
   
   # Cell 4: 模拟吸烟效果
   years = [0, 5, 10, 20, 30]
   results = []
   for year in years:
       data = model.simulate_smoking_stage(year)
       results.append({
           'years': year,
           'fev1': data['fev1_percent'],
           'volume': data['lung_volume']
       })
   
   # Cell 5: 可视化（需要matplotlib）
   import matplotlib.pyplot as plt
   
   years_list = [r['years'] for r in results]
   fev1_list = [r['fev1'] for r in results]
   
   plt.plot(years_list, fev1_list, marker='o')
   plt.xlabel('吸烟年数 / Years of Smoking')
   plt.ylabel('FEV1 (%)')
   plt.title('肺功能随时间下降 / Lung Function Decline')
   plt.grid(True)
   plt.show()
   ```

---

## 5. Python脚本导入 <a name="python-script-import"></a>

### 方法A: 安装为包后导入

```python
#!/usr/bin/env python3
"""
示例：使用肺部可视化模型
"""

from lung_visualization.lung_model import LungModel, export_model_data

# 创建模型
model = LungModel()

# 模拟不同阶段
stages = {
    'healthy': model.simulate_smoking_stage(0),
    'short_term': model.simulate_smoking_stage(3),
    'medium_term': model.simulate_smoking_stage(10),
    'long_term': model.simulate_smoking_stage(30),
}

# 打印结果
for name, data in stages.items():
    print(f"\n{name.upper()}:")
    print(f"  FEV1: {data['fev1_percent']}%")
    print(f"  Lung Volume: {data['lung_volume']} ml")
    print(f"  Tar Deposits: {data['tar_deposits']} mg")

# 导出完整数据
export_model_data('my_lung_data.json')
print("\nData exported to my_lung_data.json")
```

### 方法B: 直接导入（无需安装）

```python
#!/usr/bin/env python3
"""
不安装包直接导入
"""

import sys
from pathlib import Path

# 添加项目路径
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# 现在可以导入
from lung_visualization.lung_model import LungModel

model = LungModel()
data = model.get_baseline_data()
print(data)
```

---

## 6. Docker容器 <a name="docker-container"></a>

### 创建Dockerfile

虽然项目已有 `.devcontainer`，你也可以创建独立的Docker镜像：

```dockerfile
# Dockerfile
FROM python:3.12-slim

WORKDIR /app

# 复制项目文件
COPY . .

# 安装依赖
RUN pip install --no-cache-dir -e .

# 暴露端口
EXPOSE 8000

# 启动命令
CMD ["python3", "lung_visualization/serve.py"]
```

### 构建和运行

```bash
# 构建镜像
docker build -t lung-visualization .

# 运行容器
docker run -p 8000:8000 lung-visualization

# 访问
# http://localhost:8000/index.html
```

---

## 7. 常见问题 <a name="troubleshooting"></a>

### Q1: 端口被占用

**问题**: "Address already in use: 8000"

**解决**:
```bash
# 查找占用进程
lsof -ti:8000

# 终止进程
kill <PID>

# 或使用不同端口
python3 -m http.server 8080
```

### Q2: 导入错误

**问题**: "ModuleNotFoundError: No module named 'lung_visualization'"

**解决**:
```bash
# 确保安装了包
pip install -e .

# 或设置PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

### Q3: Python版本不兼容

**问题**: "Python 3.7 or lower"

**解决**:
```bash
# 检查版本
python3 --version

# 需要 Python 3.8+
# 升级Python或使用pyenv
```

### Q4: 虚拟环境问题

**问题**: 包安装到了系统Python

**解决**:
```bash
# 创建新的虚拟环境
python3 -m venv .venv

# 激活
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# 重新安装
pip install -e .
```

### Q5: Codespace构建失败

**问题**: "Dev container build failed"

**解决**:
- 删除并重新创建Codespace
- 检查网络连接
- 查看构建日志获取详细错误

### Q6: 找不到数据文件

**问题**: "lung_model_data.json not found"

**解决**:
```bash
# 生成数据文件
cd lung_visualization
python3 lung_model.py
```

---

## 📚 额外资源 / Additional Resources

- **项目主页**: README.md
- **快速开始**: QUICKSTART.md
- **实现细节**: IMPLEMENTATION.md
- **模块文档**: lung_visualization/README.md
- **API文档**: 查看源代码中的docstrings

---

## 💡 最佳实践 / Best Practices

1. **首次使用**: 推荐使用 GitHub Codespaces，零配置
2. **本地开发**: 使用虚拟环境隔离依赖
3. **团队协作**: 使用 VS Code Dev Container 保持环境一致
4. **数据分析**: 使用 Jupyter Notebook 交互式探索
5. **生产部署**: 使用 Docker 容器化部署

---

## 🎯 快速参考 / Quick Reference

| 场景 | 推荐方法 | 命令 |
|------|---------|------|
| 首次体验 | GitHub Codespaces | 点击仓库"Code"按钮 |
| 本地开发 | 虚拟环境 | `./install.sh && ./run.sh` |
| 团队协作 | Dev Container | VS Code: "Reopen in Container" |
| 数据分析 | Jupyter | `jupyter notebook` |
| 快速测试 | 直接运行 | `python3 lung_visualization/serve.py` |

---

**更新日期**: 2026-02-07
**版本**: 1.0.0
