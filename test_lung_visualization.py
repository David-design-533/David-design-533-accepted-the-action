"""
Test suite for lung visualization model
"""

import sys
import os
import json

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lung_visualization.lung_model import LungModel, export_model_data


def test_healthy_baseline():
    """Test healthy lung baseline model."""
    model = LungModel()
    data = model.get_baseline_data()
    
    assert data['years_smoking'] == 0
    assert data['fev1_percent'] == 100
    assert data['lung_volume'] == 6000
    assert data['tar_deposits'] == 0
    assert data['tumor_size'] == 0
    assert data['fibrosis_level'] == 0
    print("✓ Healthy baseline test passed")


def test_short_term_smoking():
    """Test short-term smoking effects (1 year)."""
    model = LungModel()
    data = model.simulate_smoking_stage(1)
    
    assert data['years_smoking'] == 1
    assert data['stage'] == 'short_term'
    assert data['fev1_percent'] < 100  # Should decline
    assert data['tar_deposits'] > 0  # Should have tar accumulation
    assert data['bronchi_diameter'] < 1.0  # Bronchial constriction
    print("✓ Short-term smoking test passed")


def test_medium_term_smoking():
    """Test medium-term smoking effects (10 years)."""
    model = LungModel()
    data = model.simulate_smoking_stage(10)
    
    assert data['years_smoking'] == 10
    assert data['stage'] == 'medium_term'
    assert data['fev1_percent'] <= 50  # Significant decline
    assert data['alveoli_health'] < 1.0  # Alveolar damage
    assert data['elasticity'] < 0.8  # Loss of elasticity
    print("✓ Medium-term smoking test passed")


def test_long_term_smoking():
    """Test long-term smoking effects (30 years)."""
    model = LungModel()
    data = model.simulate_smoking_stage(30)
    
    assert data['years_smoking'] == 30
    assert data['stage'] == 'long_term'
    assert data['fev1_percent'] <= 40  # Severe decline
    assert data['fibrosis_level'] > 0  # Fibrosis present
    assert data['tumor_size'] > 0  # Tumor risk
    print("✓ Long-term smoking test passed")


def test_progressive_damage():
    """Test that damage increases progressively."""
    model = LungModel()
    
    stages = [0, 5, 10, 20, 30]
    prev_tar = 0
    prev_damage = 0
    
    for years in stages:
        data = model.simulate_smoking_stage(years)
        current_damage = 1.0 - data['alveoli_health']
        
        # Tar should increase
        if years > 0:
            assert data['tar_deposits'] > prev_tar
        
        # Damage should increase or stay same (not decrease)
        if years > 0:
            assert current_damage >= prev_damage
        
        prev_tar = data['tar_deposits']
        prev_damage = current_damage
    
    print("✓ Progressive damage test passed")


def test_geometry_generation():
    """Test 3D geometry generation."""
    model = LungModel()
    data = model.simulate_smoking_stage(10)
    geometry = model.generate_lung_geometry(data)
    
    # Should have multiple geometric objects
    assert len(geometry) > 0
    
    # Check structure of geometry objects
    for obj in geometry:
        assert 'type' in obj
        assert 'name' in obj
        assert 'position' in obj
        assert 'color' in obj
        assert 'opacity' in obj
        
        # Validate types
        assert obj['type'] in ['ellipsoid', 'cylinder', 'sphere']
        assert len(obj['position']) == 3
        assert len(obj['color']) == 3
        assert 0 <= obj['opacity'] <= 1
    
    print("✓ Geometry generation test passed")


def test_comparison_data():
    """Test comparison data generation."""
    model = LungModel()
    comparison = model.get_comparison_data()
    
    assert 'time_points' in comparison
    assert 'stages' in comparison
    assert len(comparison['stages']) == len(comparison['time_points'])
    
    # Check each stage
    for stage in comparison['stages']:
        assert 'years' in stage
        assert 'data' in stage
        assert 'geometry' in stage
    
    print("✓ Comparison data test passed")


def test_data_export():
    """Test JSON data export."""
    import tempfile
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_file = f.name
    
    try:
        # Export data
        data = export_model_data(temp_file)
        
        # Verify file exists and is valid JSON
        assert os.path.exists(temp_file)
        
        with open(temp_file, 'r') as f:
            loaded_data = json.load(f)
        
        assert loaded_data == data
        assert 'stages' in loaded_data
        
        print("✓ Data export test passed")
        
    finally:
        # Clean up
        if os.path.exists(temp_file):
            os.remove(temp_file)


def run_all_tests():
    """Run all tests."""
    print("\n" + "="*60)
    print("Running Lung Visualization Model Tests")
    print("="*60 + "\n")
    
    tests = [
        test_healthy_baseline,
        test_short_term_smoking,
        test_medium_term_smoking,
        test_long_term_smoking,
        test_progressive_damage,
        test_geometry_generation,
        test_comparison_data,
        test_data_export
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__} failed: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__} error: {e}")
            failed += 1
    
    print("\n" + "="*60)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("="*60 + "\n")
    
    return failed == 0


if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
