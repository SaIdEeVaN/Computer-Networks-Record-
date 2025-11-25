import socket 

host = "localhost"
port = 80

n = input("Enter a limit: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.send(n.encode())
    res = s.recv(1024).decode()

if res:
    print(f"{n} is prime number")
else:
    print(f"{n} is not a prime number")