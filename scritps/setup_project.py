"""
Simple script to help set up the project structure
Run this after cloning the repository
"""

import os

# Create directory structure
directories = [
    'data/raw',
    'data/processed', 
    'notebooks/exploration',
    'notebooks/experiments',
    'notebooks/demos',
    'src/data',
    'src/models',
    'src/utils',
    'docs',
    'models/saved',
    'models/checkpoints',
    'results/figures',
    'results/metrics',
    'results/reports'
]

def create_directories():
    """Create project directory structure"""
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")
    
    # Create empty __init__.py files for Python packages
    init_files = [
        'src/__init__.py',
        'src/data/__init__.py', 
        'src/models/__init__.py',
        'src/utils/__init__.py'
    ]
    
    for init_file in init_files:
        with open(init_file, 'w') as f:
            f.write('# Empty init file\n')
        print(f"Created file: {init_file}")

create_directories()