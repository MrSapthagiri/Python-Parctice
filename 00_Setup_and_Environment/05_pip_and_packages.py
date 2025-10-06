# 05_pip_and_packages.py
"""
This script demonstrates how to use pip, Python's package installer,
and explains basic package management concepts.
"""

# ===== Introduction to pip =====
print("===== Introduction to pip =====")
print("pip is the standard package manager for Python.")
print("It allows you to install and manage additional packages that are not part of the Python standard library.")
print("pip comes pre-installed with Python 2 >=2.7.9 or Python 3 >=3.4 downloaded from python.org")

# ===== Basic pip commands =====
print("\n===== Basic pip commands =====")
print("1. Check pip version:")
print("   pip --version")
print("\n2. Install a package:")
print("   pip install package_name")
print("\n3. Install a specific version:")
print("   pip install package_name==1.0.0")
print("\n4. Upgrade a package:")
print("   pip install --upgrade package_name")
print("\n5. Uninstall a package:")
print("   pip uninstall package_name")
print("\n6. List installed packages:")
print("   pip list")
print("\n7. Show package info:")
print("   pip show package_name")

# ===== Requirements files =====
print("\n===== Requirements files =====")
print("You can store dependencies in a requirements.txt file:")
print("package_name==1.0.0")
print("another_package>=2.0.0")
print("\nInstall all packages from requirements.txt:")
print("pip install -r requirements.txt")

# ===== Virtual Environments =====
print("\n===== Virtual Environments =====")
print("Virtual environments allow you to have isolated Python environments for different projects.")
print("\nCreate a virtual environment:")
print("python -m venv myenv")
print("\nActivate virtual environment:")
print("- Windows: myenv\\Scripts\\activate")
print("- macOS/Linux: source myenv/bin/activate")
print("\nDeactivate virtual environment:")
print("deactivate")

# ===== Popular Python packages =====
print("\n===== Popular Python packages =====")
packages = [
    "numpy - Numerical computing",
    "pandas - Data analysis and manipulation",
    "matplotlib - Data visualization",
    "requests - HTTP library",
    "flask - Web framework",
    "django - Web framework",
    "scikit-learn - Machine learning",
    "tensorflow - Machine learning",
    "pytest - Testing framework"
]

for package in packages:
    print(f"- {package}")

print("\n===== End of pip and packages tutorial =====")