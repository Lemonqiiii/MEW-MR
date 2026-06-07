#!/bin/bash
# Medical Review Framework — Setup Script
set -e

echo "=== Medical Review Framework Setup ==="

# Check Python
python3 --version || { echo "Python 3.10+ required"; exit 1; }

# Install dependencies
echo "Installing dependencies..."
pip install -r scripts/requirements.txt

# Create default directories
mkdir -p data manuscript/figures docs/papers docs/search-results knowledge harness/reports

echo ""
echo "Setup complete!"
echo ""
echo "Next steps:"
echo "  1. Edit config.yaml with your topic and target journal"
echo "  2. Run: claude"
echo "  3. Say '1' or 'search' to begin literature search"
echo ""
echo "Documentation: docs/GETTING_STARTED.md"
