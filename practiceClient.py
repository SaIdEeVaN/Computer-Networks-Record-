import socket 

host = 'localhost'
port = 80

n = input("Enter a number: ")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(n.encode(), (host, port))
res, _ = s.recvfrom(1024)

if res:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")