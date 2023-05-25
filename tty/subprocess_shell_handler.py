import subprocess

# specify your script path
script_path = "./subprocess_shell.py"

# initiate the subprocess
process = subprocess.Popen(["python3", script_path])

# wait for the process to complete
process.wait()

# check the return code
if process.returncode != 0:
    print("Script exited with error")
else:
    print("Script executed successfully")
