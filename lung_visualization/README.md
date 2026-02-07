# 肺部变化可视化模型 / Lung Visualization Model

## 项目简介 / Project Overview

这是一个动态可视化模型，用于模拟抽烟行为对肺部结构和功能的长期影响。该项目采用科学数据支持，通过3D可视化和交互式界面展示吸烟对肺部的危害，以达到科普教育的目的。

This is a dynamic visualization model that simulates the long-term effects of smoking on lung structure and function. The project uses scientific data support and demonstrates the harmful effects of smoking on the lungs through 3D visualization and an interactive interface for educational purposes.

## 主要功能 / Key Features

### 1. 健康肺部基线模型 / Healthy Lung Baseline Model
- 3D肺部结构展示（左右肺叶、支气管、气管）
- 呼吸机制动画（肺部扩张/收缩）
- 正常生理指标（FEV1 100%、肺活量 6000ml）

### 2. 抽烟影响的分阶段模拟 / Phased Simulation of Smoking Effects

#### 短期（1-3年）/ Short-term (1-3 years)
- 支气管痉挛（管径变窄）
- 焦油开始沉积
- FEV1轻微下降
- 肺部颜色变化（焦油影响）

#### 中期（5-10年）/ Medium-term (5-10 years)
- 肺气肿发展（肺泡壁破坏）
- 肺弹性降低
- FEV1显著下降（50-75%）
- 肺容积增加（气体潴留）

#### 长期（20年以上）/ Long-term (20+ years)
- 严重纤维化
- 肿瘤形成风险
- FEV1严重下降（<30%）
- 肺容积减少（纤维化影响）

### 3. 交互式可视化 / Interactive Visualization
- **时间轴滑块**：动态切换不同吸烟年限的肺部状态
- **3D模型**：可旋转、缩放的肺部模型
- **实时数据面板**：显示关键健康指标
  - FEV1（第一秒用力呼气量）
  - 肺活量
  - 肺弹性
  - 肺泡健康度
  - 焦油沉积量
  - PM2.5浓度
  - 纤维化程度
  - 肿瘤大小

## 技术架构 / Technical Architecture

### 后端 / Backend
- **语言**: Python 3.12+
- **核心模块**: `lung_model.py`
  - `LungModel` 类：肺部结构模拟
  - 数学建模：基于医学文献的病理发展模型
  - 数据导出：JSON格式用于前端可视化

### 前端 / Frontend
- **3D渲染**: Three.js (v0.160.0)
- **交互控制**: OrbitControls
- **界面**: 响应式HTML5 + CSS3
- **动画**: 呼吸动画、过渡效果

### 数据模型 / Data Model
```python
{
  "stage": "healthy/short_term/medium_term/long_term",
  "years_smoking": 0-30,
  "lung_volume": float,  # ml
  "fev1_percent": float,  # %
  "elasticity": float,  # 0-1
  "alveoli_health": float,  # 0-1
  "fibrosis_level": float,  # 0-1
  "tar_deposits": float,  # mg
  "pm25_concentration": float,  # μg/m³
  "tumor_size": float,  # mm
  "bronchi_diameter": float,  # relative scale
  "lung_color": [r, g, b]  # RGB values
}
```

## 快速开始 / Quick Start

### 安装要求 / Prerequisites
- Python 3.12 或更高版本
- 现代浏览器（Chrome, Firefox, Safari, Edge）

### 运行步骤 / Running Instructions

#### 方法1：使用Python服务器（推荐）/ Method 1: Using Python Server (Recommended)

```bash
# 进入项目目录
cd lung_visualization

# 运行服务器（会自动生成数据文件）
python3 serve.py

# 或直接执行
./serve.py

# 打开浏览器访问
# http://localhost:8000/index.html
```

#### 方法2：仅生成数据 / Method 2: Generate Data Only

```bash
# 运行模型生成数据
cd lung_visualization
python3 lung_model.py

# 这会生成 lung_model_data.json 文件
# 然后用任何Web服务器打开 index.html
```

#### 方法3：直接打开（无需服务器）/ Method 3: Direct Open (No Server)

```bash
# 如果浏览器允许本地文件访问，可以直接打开
open lung_visualization/index.html
# 或
firefox lung_visualization/index.html
```

## 使用说明 / Usage Guide

### 界面操作 / Interface Controls

1. **时间轴滑块**
   - 拖动滑块选择不同的吸烟年限（0-30年）
   - 自动更新3D模型和数据面板
   - 显示对应阶段的健康描述

2. **3D视图控制**
   - **鼠标左键拖动**：旋转视角
   - **鼠标滚轮**：缩放视图
   - **鼠标右键拖动**：平移视图

3. **数据面板**
   - 实时显示当前阶段的肺功能指标
   - 颜色编码：绿色（正常）、黄色（警告）、红色（危险）
   - 健康状态评估：健康/轻度/中度/严重

### 科学依据 / Scientific Basis

模型基于以下医学研究和数据：
- 世界卫生组织（WHO）吸烟危害报告
- 慢性阻塞性肺病（COPD）发展模型
- 肺癌流行病学数据
- 肺功能测试标准（FEV1、FVC等）

**重要提示**: 本模型用于科普教育，展示的数据是基于统计平均值和文献资料的简化模型，实际个体差异较大。

## 项目结构 / Project Structure

```
lung_visualization/
├── __init__.py           # 模块初始化文件
├── lung_model.py         # 核心Python模型
├── index.html            # 主界面HTML
├── serve.py              # 开发服务器脚本
├── lung_model_data.json  # 自动生成的模型数据
└── README.md             # 本文档
```

## 开发说明 / Development Notes

### 扩展功能 / Extension Ideas

1. **增强模型精度**
   - 导入真实CT扫描数据
   - 使用PyVista创建更精细的3D网格
   - 添加肺泡级别的微观视图

2. **交互增强**
   - 添加对比视图（并排显示健康vs病态）
   - 支持自定义吸烟量（每天cigarettes数量）
   - 添加戒烟后恢复模拟

3. **数据可视化**
   - 使用Plotly添加趋势图表
   - 显示多指标关联分析
   - 导出PDF报告功能

4. **科学验证**
   - 与医学专家合作验证模型
   - 接入真实临床数据库
   - 发表科研论文

### 代码贡献 / Contributing

欢迎提交Issue和Pull Request来改进这个项目！

## 健康警示 / Health Warning

⚠️ **吸烟有害健康！**

本可视化模型展示了吸烟对肺部的严重危害：
- 肺功能持续下降
- 慢性阻塞性肺病（COPD）
- 肺气肿和纤维化
- 肺癌风险显著增加

**建议**：
- 如果您吸烟，请尽早戒烟
- 定期进行肺功能检查
- 咨询医疗专业人士获取帮助

## 许可证 / License

本项目用于教育和科普目的。

## 联系方式 / Contact

如有问题或建议，请通过GitHub Issues联系。

---

**最后更新 / Last Updated**: 2026-02-07
**版本 / Version**: 1.0.0
