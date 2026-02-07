"""
Setup configuration for Lung Visualization Model
肺部可视化模型安装配置
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the long description from README
this_directory = Path(__file__).parent
long_description = (this_directory / "lung_visualization" / "README.md").read_text(encoding='utf-8')

setup(
    name="lung-visualization",
    version="1.0.0",
    author="David Design",
    description="Interactive 3D lung visualization model showing smoking effects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/David-design-533/David-design-533-accepted-the-action",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Healthcare Industry",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Visualization",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        # No external dependencies required
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "lung-viz-serve=lung_visualization.serve:main",
            "lung-viz-demo=example_demo:main",
        ],
    },
    package_data={
        "lung_visualization": ["*.html", "*.md"],
    },
    include_package_data=True,
    zip_safe=False,
)
