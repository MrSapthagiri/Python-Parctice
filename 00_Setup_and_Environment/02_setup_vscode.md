# 02_setup_vscode.md

# Setup VS Code for Python (Windows)

Purpose: quick steps to configure Visual Studio Code for Python development, use a virtual environment, enable linting/formatting and debugging.

## 1. Install VS Code and extensions
1. Download VS Code: https://code.visualstudio.com/
2. Install these extensions (Marketplace names):
   - Python (ms-python.python)
   - Pylance (ms-python.vscode-pylance)
   - Jupyter (ms-toolsai.jupyter) — optional for notebooks
3. Install from command line (optional):
   - code --install-extension ms-python.python
   - code --install-extension ms-python.vscode-pylance

## 2. Open your project folder
- In VS Code: File → Open Folder → select your project folder (same folder where you created .venv).

## 3. Create and select the virtual environment
From project folder (PowerShell):
- python -m venv .venv
- .venv\Scripts\Activate.ps1
- pip install -r requirements.txt

In VS Code:
- Ctrl+Shift+P → Python: Select Interpreter → choose .venv\Scripts\python.exe

## 4. Recommended workspace settings (.vscode/settings.json)
Add or update to use the workspace venv, enable linting and formatting:
```json
// filepath: c:\Users\HP\Music\Python Parctice\.vscode\settings.json
{
  "python.defaultInterpreterPath": "${workspaceFolder}\\.venv\\Scripts\\python.exe",
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.analysis.typeCheckingMode": "basic"
}
```

## 5. Linting & formatting
- Install tools in venv: pip install pylint black
- Configure formatter in settings (above) or via workspace config.

## 6. Debugging
- Create a basic launch configuration: Run → Add Configuration... → Python: Current File
- Example snippet (auto-created in .vscode/launch.json):
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Current File",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal"
    }
  ]
}
```

## 7. Testing
- Install pytest: pip install pytest
- Run tests: Ctrl+Shift+P → Python: Run All Tests (configure pytest in settings if needed)

## 8. Useful commands
- Select interpreter: Ctrl+Shift+P → Python: Select Interpreter
- Run a file: Right-click → Run Python File in Terminal
- Open integrated terminal: Ctrl+`

## 9. Notes
- Keep a per-project .venv to avoid global package conflicts.
- Commit .vscode/extensions.json (recommended) but not the virtualenv directory.
