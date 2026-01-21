#!/bin/bash
# =============================
# Git Cleanup Script
# Removes tracked files that should be ignored
# =============================

echo "Starting Git cleanup..."

# Ensure we are in the project root
PROJECT_ROOT=$(pwd)
echo "Project root: $PROJECT_ROOT"

# List of paths/patterns to untrack
declare -a FILES_TO_UNTRACK=(
    "trash/"
    "nano_backups/"
    "*.py~"
    "*.xlsx~"
    "*.ipynb_checkpoints/"
)

# Loop through and remove from Git cache
for ITEM in "${FILES_TO_UNTRACK[@]}"
do
    if git ls-files --error-unmatch "$ITEM" > /dev/null 2>&1; then
        echo "Untracking: $ITEM"
        git rm -r --cached "$ITEM"
    else
        echo "No tracked files found for: $ITEM"
    fi
done

# Commit the cleanup
git commit -m "Clean up tracked files that should be ignored by .gitignore"

# Show status
git status

echo "Git cleanup done. You can now push to remote safely."
