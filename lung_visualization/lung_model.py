"""
Lung Model Module
Implements the core lung structure and smoking effect simulation.
"""

import json
import math
from typing import Dict, List, Tuple


class LungModel:
    """Base class for lung structure and simulation."""
    
    def __init__(self):
        """Initialize healthy lung baseline model."""
        # Lung structure parameters
        self.total_alveoli = 300_000_000  # Approximately 300 million alveoli
        self.healthy_lung_volume = 6000  # ml (Total Lung Capacity)
        self.healthy_fev1 = 100  # FEV1 as percentage of predicted
        self.lung_elasticity = 1.0  # 0-1 scale
        
        # Tissue health parameters
        self.healthy_alveoli_ratio = 1.0  # Ratio of healthy alveoli
        self.fibrosis_level = 0.0  # 0-1 scale
        self.tar_deposits = 0.0  # mg
        self.pm25_concentration = 0.0  # μg/m³
        self.tumor_size = 0.0  # mm
        
        # Visualization data
        self.bronchi_diameter = 1.0  # Relative scale
        self.lung_color = [1.0, 0.8, 0.8]  # RGB: Healthy pink
        
    def get_baseline_data(self) -> Dict:
        """Get healthy lung baseline data."""
        return {
            'stage': 'healthy',
            'years_smoking': 0,
            'lung_volume': self.healthy_lung_volume,
            'fev1_percent': self.healthy_fev1,
            'elasticity': self.lung_elasticity,
            'alveoli_health': self.healthy_alveoli_ratio,
            'fibrosis_level': self.fibrosis_level,
            'tar_deposits': self.tar_deposits,
            'pm25_concentration': self.pm25_concentration,
            'tumor_size': self.tumor_size,
            'bronchi_diameter': self.bronchi_diameter,
            'lung_color': self.lung_color,
            'description': '健康肺部基线模型 - 正常的呼吸功能和结构'
        }
    
    def simulate_smoking_stage(self, years: int) -> Dict:
        """
        Simulate lung changes after years of smoking.
        
        Args:
            years: Number of years of smoking (1, 5, 10, 20, 30, etc.)
            
        Returns:
            Dictionary containing simulated lung parameters
        """
        if years <= 0:
            return self.get_baseline_data()
        
        # Reset to baseline before calculating new stage
        self.healthy_lung_volume = 6000
        self.healthy_fev1 = 100
        self.lung_elasticity = 1.0
        self.healthy_alveoli_ratio = 1.0
        self.fibrosis_level = 0.0
        self.tar_deposits = 0.0
        self.pm25_concentration = 0.0
        self.tumor_size = 0.0
        self.bronchi_diameter = 1.0
        self.lung_color = [1.0, 0.8, 0.8]
        
        # Calculate progressive damage based on years
        # Short-term effects (1-3 years)
        if years <= 3:
            stage = 'short_term'
            description = '短期吸烟影响（1-3年）- 支气管痉挛，焦油开始沉积'
            
            # Bronchial constriction
            self.bronchi_diameter = max(0.7, 1.0 - years * 0.1)
            
            # Tar accumulation (approximately 70mg tar per pack per day)
            self.tar_deposits = years * 365 * 20 * 0.07  # 20 cigarettes/day
            
            # PM2.5 exposure
            self.pm25_concentration = years * 15
            
            # Slight FEV1 decline
            self.healthy_fev1 = 100 - years * 2
            
            # Color change (yellowing from tar)
            self.lung_color = [1.0, 0.8 - years * 0.05, 0.8 - years * 0.1]
            
        # Medium-term effects (5-10 years)
        elif years <= 10:
            stage = 'medium_term'
            description = f'中期吸烟影响（{years}年）- 肺气肿开始，肺泡壁破坏'
            
            # Progressive bronchial damage
            self.bronchi_diameter = max(0.5, 1.0 - years * 0.08)
            
            # Continued tar accumulation
            self.tar_deposits = years * 365 * 20 * 0.07
            
            # Emphysema development (alveolar destruction)
            destruction_rate = (years - 3) * 0.05
            self.healthy_alveoli_ratio = max(0.5, 1.0 - destruction_rate)
            
            # Increased lung volume due to trapped air
            self.healthy_lung_volume = 6000 + (years - 3) * 100
            
            # Lung elasticity loss
            self.lung_elasticity = max(0.4, 1.0 - years * 0.06)
            
            # FEV1 decline accelerates
            self.healthy_fev1 = max(50, 100 - years * 5)
            
            # PM2.5 accumulation
            self.pm25_concentration = years * 20
            
            # Color changes (greyish from tissue damage)
            self.lung_color = [0.7, 0.6 - years * 0.03, 0.6 - years * 0.04]
            
        # Long-term effects (20+ years)
        else:
            stage = 'long_term'
            description = f'长期吸烟影响（{years}年）- 严重纤维化，肿瘤形成风险'
            
            # Severe bronchial damage
            self.bronchi_diameter = max(0.3, 1.0 - years * 0.05)
            
            # Massive tar accumulation
            self.tar_deposits = years * 365 * 20 * 0.07
            
            # Severe alveolar destruction
            destruction_rate = min(0.7, 0.5 + (years - 10) * 0.02)
            self.healthy_alveoli_ratio = max(0.2, 1.0 - destruction_rate)
            
            # Fibrosis development
            self.fibrosis_level = min(0.8, (years - 10) * 0.03)
            
            # Greatly reduced lung volume from fibrosis
            volume_loss = self.fibrosis_level * 1500
            self.healthy_lung_volume = max(3500, 6000 - volume_loss + (years - 10) * 50)
            
            # Severe elasticity loss
            self.lung_elasticity = max(0.2, 1.0 - years * 0.04)
            
            # Severe FEV1 decline
            self.healthy_fev1 = max(30, 100 - years * 3.5)
            
            # High PM2.5 concentration
            self.pm25_concentration = min(500, years * 25)
            
            # Tumor formation (probabilistic, represented by size)
            if years >= 20:
                # Tumor risk increases with years
                tumor_probability = min(0.5, (years - 20) * 0.02)
                self.tumor_size = tumor_probability * 30  # 0-15mm
            
            # Color changes (dark grey, fibrous regions)
            grey_level = max(0.3, 0.7 - years * 0.01)
            self.lung_color = [grey_level, grey_level - 0.1, grey_level - 0.05]
        
        return {
            'stage': stage,
            'years_smoking': years,
            'lung_volume': round(self.healthy_lung_volume, 1),
            'fev1_percent': round(self.healthy_fev1, 1),
            'elasticity': round(self.lung_elasticity, 2),
            'alveoli_health': round(self.healthy_alveoli_ratio, 2),
            'fibrosis_level': round(self.fibrosis_level, 2),
            'tar_deposits': round(self.tar_deposits, 1),
            'pm25_concentration': round(self.pm25_concentration, 1),
            'tumor_size': round(self.tumor_size, 1),
            'bronchi_diameter': round(self.bronchi_diameter, 2),
            'lung_color': [round(c, 2) for c in self.lung_color],
            'description': description
        }
    
    def generate_lung_geometry(self, stage_data: Dict) -> List[Dict]:
        """
        Generate simplified 3D geometry data for visualization.
        
        Args:
            stage_data: Stage simulation data from simulate_smoking_stage()
            
        Returns:
            List of geometric objects representing lung structure
        """
        geometry = []
        
        # Main lung lobes (simplified as ellipsoids)
        # Right lung (3 lobes)
        for i, (y_offset, scale) in enumerate([(0.3, 0.35), (0, 0.3), (-0.3, 0.35)]):
            geometry.append({
                'type': 'ellipsoid',
                'name': f'right_lobe_{i+1}',
                'position': [0.4, y_offset, 0],
                'scale': [0.25 * stage_data['elasticity'], 
                         0.4 * scale * stage_data['elasticity'], 
                         0.3 * stage_data['elasticity']],
                'color': stage_data['lung_color'],
                'opacity': 0.8
            })
        
        # Left lung (2 lobes)
        for i, (y_offset, scale) in enumerate([(0.2, 0.4), (-0.2, 0.4)]):
            geometry.append({
                'type': 'ellipsoid',
                'name': f'left_lobe_{i+1}',
                'position': [-0.4, y_offset, 0],
                'scale': [0.25 * stage_data['elasticity'], 
                         0.4 * scale * stage_data['elasticity'], 
                         0.3 * stage_data['elasticity']],
                'color': stage_data['lung_color'],
                'opacity': 0.8
            })
        
        # Bronchi (simplified as cylinders)
        bronchi_radius = 0.03 * stage_data['bronchi_diameter']
        
        # Main bronchi
        for x_pos, name in [(0.4, 'right_bronchus'), (-0.4, 'left_bronchus')]:
            geometry.append({
                'type': 'cylinder',
                'name': name,
                'position': [x_pos, 0.5, 0],
                'radius': bronchi_radius,
                'height': 0.4,
                'color': [0.9, 0.7, 0.7],
                'opacity': 1.0
            })
        
        # Trachea
        geometry.append({
            'type': 'cylinder',
            'name': 'trachea',
            'position': [0, 0.8, 0],
            'radius': bronchi_radius * 1.2,
            'height': 0.3,
            'color': [0.9, 0.7, 0.7],
            'opacity': 1.0
        })
        
        # Tumor visualization (if present)
        if stage_data['tumor_size'] > 0:
            # Random position in right upper lobe (common location)
            geometry.append({
                'type': 'sphere',
                'name': 'tumor',
                'position': [0.5, 0.3, 0.1],
                'radius': stage_data['tumor_size'] / 100,  # Scale to visualization units
                'color': [0.2, 0.2, 0.2],
                'opacity': 0.9
            })
        
        # Fibrosis regions (if present)
        if stage_data['fibrosis_level'] > 0.1:
            # Show fibrotic patches
            num_patches = int(stage_data['fibrosis_level'] * 10)
            for i in range(num_patches):
                angle = (i / num_patches) * 2 * math.pi
                x = 0.3 * math.cos(angle)
                z = 0.2 * math.sin(angle)
                
                geometry.append({
                    'type': 'sphere',
                    'name': f'fibrosis_patch_{i}',
                    'position': [x, -0.2, z],
                    'radius': 0.05,
                    'color': [0.5, 0.5, 0.6],
                    'opacity': 0.7
                })
        
        return geometry
    
    def get_comparison_data(self, year_points: List[int] = None) -> Dict:
        """
        Generate comparison data for multiple time points.
        
        Args:
            year_points: List of years to compare (default: [0, 1, 5, 10, 20, 30])
            
        Returns:
            Dictionary with comparison data for all time points
        """
        if year_points is None:
            year_points = [0, 1, 5, 10, 20, 30]
        
        comparison = {
            'time_points': year_points,
            'stages': []
        }
        
        for years in year_points:
            stage_data = self.simulate_smoking_stage(years)
            geometry = self.generate_lung_geometry(stage_data)
            
            comparison['stages'].append({
                'years': years,
                'data': stage_data,
                'geometry': geometry
            })
        
        return comparison


def export_model_data(output_file: str = 'lung_model_data.json'):
    """
    Export complete lung model data to JSON file for web visualization.
    
    Args:
        output_file: Output JSON file path
    """
    model = LungModel()
    comparison_data = model.get_comparison_data()
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(comparison_data, f, ensure_ascii=False, indent=2)
    
    return comparison_data


if __name__ == '__main__':
    # Demo: Generate and print lung model data
    print("Lung Visualization Model - Demo")
    print("=" * 50)
    
    model = LungModel()
    
    # Test different stages
    for years in [0, 1, 5, 10, 20, 30]:
        print(f"\n吸烟 {years} 年:")
        data = model.simulate_smoking_stage(years)
        print(f"  FEV1: {data['fev1_percent']}%")
        print(f"  肺活量: {data['lung_volume']} ml")
        print(f"  焦油沉积: {data['tar_deposits']} mg")
        print(f"  肿瘤大小: {data['tumor_size']} mm")
        print(f"  描述: {data['description']}")
    
    # Export full data
    print("\n导出模型数据...")
    export_model_data()
    print("已导出到 lung_model_data.json")
