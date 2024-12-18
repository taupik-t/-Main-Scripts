import subprocess

# Path to your executable file
exe_path = r'C:\Users\taupi\Downloads\LKS 2024 (NASIONAL)\Android\2023\Nasional\Backend API\Ezemkofi.Api.exe'

try:
    # Run the executable
    process = subprocess.Popen(exe_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Wait for the process to terminate
    stdout, stderr = process.communicate()

    # Check if there was any error message
    if process.returncode != 0:
        print(f"Error occurred: {stderr.decode('utf-8')}")
    else:
        print("Application ran successfully.")
except FileNotFoundError:
    print("Error: Executable file not found.")
except Exception as e:
    print(f"Error occurred: {str(e)}")
