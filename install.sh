#!/bin/bash

set -e  # Exit on any error

SCRIPT_NAME="diag-generator"
INSTALL_DIR="$HOME/.local/bin"
PYTHON_PACKAGES=("graphviz" "pyfiglet" "termcolor")

echo "🚀 Installing $SCRIPT_NAME..."

# Check if Graphviz is installed
if ! command -v dot &> /dev/null; then
    echo "⚠️ Graphviz is not installed. Installing..."
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo apt update && sudo apt install -y graphviz || sudo dnf install -y graphviz
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        brew install graphviz
    else
        echo "Unsupported OS. Please install Graphviz manually."
        exit 1
    fi
else
    echo "✅ Graphviz is already installed."
fi

# Install required Python packages (inside virtualenv if active)
if [[ -n "$VIRTUAL_ENV" ]]; then
    echo "📦 Installing Python dependencies inside virtual environment..."
    pip install "${PYTHON_PACKAGES[@]}"
else
    echo "📦 Installing Python dependencies system-wide..."
    pip3 install --break-system-packages "${PYTHON_PACKAGES[@]}"  # Use --break-system-packages for newer Python versions
fi

# Ensure the install directory exists
mkdir -p "$INSTALL_DIR"

# Move the script and make it executable
cp final.py "$INSTALL_DIR/$SCRIPT_NAME"
chmod +x "$INSTALL_DIR/$SCRIPT_NAME"

# Ensure ~/.local/bin is in the PATH
if [[ ":$PATH:" != *":$INSTALL_DIR:"* ]]; then
    echo "export PATH=\"$INSTALL_DIR:\$PATH\"" >> "$HOME/.bashrc"
    echo "export PATH=\"$INSTALL_DIR:\$PATH\"" >> "$HOME/.zshrc"
    export PATH="$INSTALL_DIR:$PATH"
    echo "🔧 Added $INSTALL_DIR to your PATH. Restart your terminal or run 'source ~/.bashrc' (or ~/.zshrc)."
fi

echo "🎉 Installation complete! You can now run '$SCRIPT_NAME' from anywhere."

