import paramiko

ssh = paramiko.SSHClient()

# It's a good idea to automatically add the server's SSH key (you might also manually verify it)
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the remote server
ssh.connect('0.0.0.0', port=2222, username='test', password='password')

# Execute a command (returns stdin, stdout, stderr)
stdin, stdout, stderr = ssh.exec_command('ls')

# Print the output of the command
print(stdout.read().decode())

print("Command completed! Closing ssh session..")

# Close the connection
ssh.close()
