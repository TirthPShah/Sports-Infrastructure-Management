#!/bin/bash

# Script to deploy changes to GitHub

# Check if a commit message is provided
if [ -z "$1" ]; then
  echo "Please provide a commit message."
  exit 1
fi

# Add all changes
git add .

# Commit changes with the provided message
git commit -m "$1"

# Push changes to the 'main' branch (assuming 'main' is your main branch)
git push origin main

# Optionally, you can add more commands here for deployment tasks like restarting services, etc.

echo "Deployment to GitHub completed."
