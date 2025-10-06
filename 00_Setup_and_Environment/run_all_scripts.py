import os
import subprocess
import sys

def run_python_file(file_path):
    """Execute a Python file and capture its output."""
    print(f"\n{'='*50}")
    print(f"Executing: {os.path.basename(file_path)}")
    print(f"{'='*50}")
    
    try:
        # Run the Python file and capture output
        result = subprocess.run(
            [sys.executable, file_path],
            capture_output=True,
            text=True,
            timeout=30  # Set a timeout of 30 seconds
        )
        
        # Print stdout if available
        if result.stdout:
            print("\nOutput:")
            print(result.stdout)
        else:
            print("\nNo output produced.")
            
        # Print stderr if there was an error
        if result.stderr:
            print("\nErrors/Warnings:")
            print(result.stderr)
            
        # Print return code
        print(f"\nReturn code: {result.returncode}")
        
    except subprocess.TimeoutExpired:
        print("\nExecution timed out after 30 seconds.")
    except Exception as e:
        print(f"\nError executing file: {e}")

def main():
    # Get the current directory (where this script is located)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Find all Python files in the directory
    python_files = [f for f in os.listdir(current_dir) 
                   if f.endswith('.py') and f != os.path.basename(__file__)]
    
    if not python_files:
        print("No Python files found in this directory.")
        return
    
    print(f"Found {len(python_files)} Python files to execute.")
    
    # Execute each Python file
    for file_name in sorted(python_files):
        file_path = os.path.join(current_dir, file_name)
        run_python_file(file_path)
    
    print("\nAll files executed successfully.")

if __name__ == "__main__":
    main()