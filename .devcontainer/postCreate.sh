#!/bin/bash
set -e  # Exit on any error

if [ -f "requirements.txt" ]; then
    pip install --upgrade pip
    pip install -r requirements.txt
else
    echo "No requirements.txt found."
fi