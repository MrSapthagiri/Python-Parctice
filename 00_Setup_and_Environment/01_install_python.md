# 01_install_python.md

# Install Python (Windows)

Purpose: quick steps to install and verify Python on Windows and create a virtual environment.

## 1. Download and install
1. Go to https://www.python.org/downloads/windows and download the latest stable Windows installer (64-bit).
2. Run the installer and **check "Add Python to PATH"** before clicking Install Now.

## 2. Verify installation (PowerShell or Command Prompt)
- python --version
- pip --version
If `python` is not found, use the launcher:
- py -3 --version

## 3. Create and activate a virtual environment
From your project folder:
- Create: python -m venv .venv
- PowerShell activate: .venv\Scripts\Activate.ps1
- Command Prompt activate: .venv\Scripts\activate.bat

Deactivate: deactivate

## 4. Install packages
- pip install <package-name>
- Freeze requirements: pip freeze > requirements.txt

## 5. Notes
- If you forgot "Add Python to PATH", you can reinstall or use the `py` launcher (`py -3`) to run Python.
- For development, use virtual environments per project to avoid global package conflicts.
