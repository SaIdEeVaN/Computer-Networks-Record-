import socket

host = "localhost"
port = 80

n = input("Enter a limit: ")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(n.encode(), (host, port))

res, _ = s.recvfrom(1024)

print(f"Fibonacci series of 1st {n} terms is : {res.decode()}")