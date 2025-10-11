#!/usr/bin/env python3
"""
Setup script for espanso configurations in heme-texts project.
This script creates symlinks from the git-tracked configs to the espanso config directory.
"""

import os
import sys
from pathlib import Path

def setup_espanso_configs():
    """Create symlinks for espanso configurations."""
    
    # Paths
    project_root = Path(__file__).parent.parent
    espanso_configs_dir = project_root / "espanso-configs"
    espanso_home = Path.home() / ".config" / "espanso" / "config"
    
    # Ensure espanso config directory exists
    espanso_home.mkdir(parents=True, exist_ok=True)
    
    # List of config files to symlink
    config_files = [
        "citrix.yml",
        # Add more config files here as needed
    ]
    
    print(f"Setting up espanso configurations...")
    print(f"Source: {espanso_configs_dir}")
    print(f"Target: {espanso_home}")
    
    for config_file in config_files:
        source = espanso_configs_dir / config_file
        target = espanso_home / config_file
        
        if not source.exists():
            print(f"Warning: {source} does not exist, skipping...")
            continue
            
        # Remove existing file/symlink if it exists
        if target.exists() or target.is_symlink():
            target.unlink()
            
        # Create symlink
        target.symlink_to(source)
        print(f"✓ Created symlink: {config_file}")
    
    print("\nEspanso configuration setup complete!")
    print("You may need to restart espanso for changes to take effect:")
    print("  espanso restart")

if __name__ == "__main__":
    setup_espanso_configs()
