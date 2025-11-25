import socket

host = '0.0.0.0'
port = 80

def isPerfect(n):
    array = []
    for i in range(1, n):
        if n % i == 0:
            array.append(i)
    return sum(array) == n

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

while True:
    data, addr = s.recvfrom(1024)
    n = data.decode()
    s.sendto(isPerfect(int(n)), addr)