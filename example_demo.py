#!/usr/bin/env python3
"""
Example demonstration of the lung visualization model.
This script generates a comprehensive comparison report.
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from lung_visualization.lung_model import LungModel


def print_stage_comparison():
    """Print a detailed comparison of all stages."""
    print("\n" + "="*80)
    print(" 肺部变化可视化模型 - 阶段对比报告 ".center(80, "="))
    print("="*80 + "\n")
    
    model = LungModel()
    stages = [
        (0, "健康基线"),
        (1, "吸烟1年"),
        (5, "吸烟5年"),
        (10, "吸烟10年"),
        (20, "吸烟20年"),
        (30, "吸烟30年")
    ]
    
    print("╔" + "═"*78 + "╗")
    print("║" + " 关键健康指标对比表 ".center(78) + "║")
    print("╠" + "═"*78 + "╣")
    print(f"║ {'阶段':<12} │ {'FEV1':<8} │ {'肺活量':<10} │ {'肺弹性':<8} │ {'肺泡健康':<8} │ {'纤维化':<8} ║")
    print("╠" + "─"*78 + "╣")
    
    for years, label in stages:
        data = model.simulate_smoking_stage(years)
        print(f"║ {label:<12} │ {data['fev1_percent']:>6.1f}% │ {data['lung_volume']:>8.0f}ml │ "
              f"{data['elasticity']*100:>6.1f}% │ {data['alveoli_health']*100:>6.1f}% │ "
              f"{data['fibrosis_level']*100:>6.1f}% ║")
    
    print("╚" + "═"*78 + "╝\n")
    
    # Damage indicators
    print("╔" + "═"*78 + "╗")
    print("║" + " 损伤指标对比表 ".center(78) + "║")
    print("╠" + "═"*78 + "╣")
    print(f"║ {'阶段':<12} │ {'焦油沉积':<14} │ {'PM2.5浓度':<14} │ {'肿瘤大小':<12} ║")
    print("╠" + "─"*78 + "╣")
    
    for years, label in stages:
        data = model.simulate_smoking_stage(years)
        print(f"║ {label:<12} │ {data['tar_deposits']:>10.0f} mg │ "
              f"{data['pm25_concentration']:>10.1f} μg/m³ │ {data['tumor_size']:>9.1f} mm ║")
    
    print("╚" + "═"*78 + "╝\n")
    
    # Detailed stage descriptions
    print("\n" + "─"*80)
    print(" 详细阶段描述 ".center(80, "─"))
    print("─"*80 + "\n")
    
    for years, label in stages:
        data = model.simulate_smoking_stage(years)
        print(f"\n【{label}】")
        print(f"  描述: {data['description']}")
        print(f"  支气管直径: {data['bronchi_diameter']*100:.1f}% (相对健康值)")
        print(f"  肺部颜色: RGB({data['lung_color'][0]:.2f}, "
              f"{data['lung_color'][1]:.2f}, {data['lung_color'][2]:.2f})")
        
        # Health assessment
        if data['fev1_percent'] >= 80:
            health = "✓ 健康"
            color = "\033[92m"  # Green
        elif data['fev1_percent'] >= 60:
            health = "⚠ 轻度受损"
            color = "\033[93m"  # Yellow
        elif data['fev1_percent'] >= 40:
            health = "⚠⚠ 中度受损"
            color = "\033[93m"  # Yellow
        else:
            health = "✗ 严重受损"
            color = "\033[91m"  # Red
        
        print(f"  健康评估: {color}{health}\033[0m")  # Reset color
    
    print("\n" + "="*80 + "\n")


def print_health_warnings():
    """Print health warnings and recommendations."""
    print("\n" + "╔" + "═"*78 + "╗")
    print("║" + " ⚠️  健康警示 ⚠️ ".center(78) + "║")
    print("╠" + "═"*78 + "╣")
    print("║                                                                              ║")
    print("║  🚭 吸烟有害健康！本模型基于医学研究数据，展示吸烟对肺部的危害。              ║")
    print("║                                                                              ║")
    print("║  主要危害：                                                                  ║")
    print("║    • 肺功能持续下降，呼吸困难                                                ║")
    print("║    • 慢性阻塞性肺病（COPD）风险增加                                          ║")
    print("║    • 肺气肿和肺纤维化                                                        ║")
    print("║    • 肺癌风险显著增加（吸烟20年+）                                           ║")
    print("║                                                                              ║")
    print("║  建议：                                                                      ║")
    print("║    ✓ 尽早戒烟可显著改善预后                                                 ║")
    print("║    ✓ 定期进行肺功能检查                                                     ║")
    print("║    ✓ 咨询医疗专业人士获取戒烟帮助                                           ║")
    print("║    ✓ 保持健康生活方式，加强锻炼                                             ║")
    print("║                                                                              ║")
    print("╚" + "═"*78 + "╝\n")


def generate_visualization_data():
    """Generate and save visualization data."""
    from lung_visualization.lung_model import export_model_data
    
    print("\n生成可视化数据文件...")
    output_file = 'lung_visualization/lung_model_data.json'
    export_model_data(output_file)
    print(f"✓ 数据已导出到: {output_file}")
    print(f"  文件大小: {os.path.getsize(output_file) / 1024:.1f} KB")
    
    # Count geometric objects
    import json
    with open(output_file, 'r') as f:
        data = json.load(f)
    
    total_objects = sum(len(stage['geometry']) for stage in data['stages'])
    print(f"  包含 {len(data['stages'])} 个阶段，共 {total_objects} 个3D几何对象")


def main():
    """Main demonstration function."""
    print("\n")
    print("█" * 80)
    print("█" + " " * 78 + "█")
    print("█" + " 肺部变化可视化模型 - 示例演示 ".center(78) + "█")
    print("█" + " Lung Visualization Model - Example Demonstration ".center(78) + "█")
    print("█" + " " * 78 + "█")
    print("█" * 80)
    
    # Print comparison
    print_stage_comparison()
    
    # Print health warnings
    print_health_warnings()
    
    # Generate visualization data
    generate_visualization_data()
    
    # Instructions
    print("\n" + "─"*80)
    print(" 如何使用可视化界面 ".center(80, "─"))
    print("─"*80 + "\n")
    print("1. 启动Web服务器:")
    print("   cd lung_visualization")
    print("   python3 serve.py")
    print("")
    print("2. 打开浏览器访问:")
    print("   http://localhost:8000/index.html")
    print("")
    print("3. 使用时间轴滑块切换不同吸烟年限，观察肺部变化")
    print("   - 拖动鼠标旋转3D模型")
    print("   - 滚轮缩放视图")
    print("   - 查看右侧数据面板了解详细指标")
    print("\n" + "─"*80 + "\n")


if __name__ == '__main__':
    main()
