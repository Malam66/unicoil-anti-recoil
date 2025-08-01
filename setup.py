#!/usr/bin/env python3
"""
Setup script for UniCoil Anti-Recoil System
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="unicoil-anti-recoil",
    version="1.3.0",
    author="UniCoil Team",
    author_email="contact@unicoil.com",
    description="Universal Anti-Recoil Control System for Gaming",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/unicoil-anti-recoil",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/unicoil-anti-recoil/issues",
        "Documentation": "https://github.com/yourusername/unicoil-anti-recoil/wiki",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Games/Entertainment",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
        ],
    },
    entry_points={
        "console_scripts": [
            "unicoil=universal_antirecoil_app:main",
            "unicoil-launcher=launcher:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.json", "*.lua", "*.bat"],
    },
    keywords="gaming, anti-recoil, mouse-control, automation",
    license="MIT",
    platforms=["Windows"],
) 