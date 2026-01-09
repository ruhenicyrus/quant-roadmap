#!/usr/bin/env python3
"""
safe_delete.py
Move files and folders to project trash folder safely with confirmation and timestamp
Usage:
    python safe_delete.py file1.py folder1 file2.txt ...
"""

import os
import sys
from datetime import datetime
import shutil

# Define trash folder
TRASH_DIR = os.path.expanduser('~/Documents/quant-roadmap/trash')

# Ensure trash folder exists
os.makedirs(TRASH_DIR, exist_ok=True)

# Check if arguments were passed
if len(sys.argv) < 2:
    print("Usage: python safe_delete.py <file_or_folder1> [file_or_folder2 ...]")
    sys.exit(1)

# Process each file/folder
for path in sys.argv[1:]:
    # Absolute path
    abs_path = os.path.abspath(os.path.expanduser(path))

    if not os.path.exists(abs_path):
        print(f"⚠ File or folder does not exist: {abs_path}")
        continue

    # Confirm before trashing
    response = input(f"Trash '{abs_path}'? [y/N]: ").strip().lower()
    if response != 'y':
        print(f"Skipped: {abs_path}")
        continue

    # Timestamped name
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    base_name = os.path.basename(abs_path)
    dest_path = os.path.join(TRASH_DIR, f"{timestamp}_{base_name}")

    # Move file or folder
    try:
        shutil.move(abs_path, dest_path)
        print(f"✅ Trashed: {abs_path} → {dest_path}")
    except Exception as e:
        print(f"❌ Failed to trash {abs_path}: {e}")

