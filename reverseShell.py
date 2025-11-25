import paramiko
hostname = "google.com"
username = "Sai Dixit"
key_filename = "/home/you/.ssh/id_ed25519"
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, username=username, key_filename=key_filename)
stdin, stdout, stderr = client.exec_command("uname -a && whoami")
print("STDOUT:")
print(stdout.read().decode())
print("STDERR:")
print(stderr.read().decode())
client.close()
