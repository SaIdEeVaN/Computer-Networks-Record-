import socket 

host = '0.0.0.0'
port = 80

def fib(n):
    a, b = 0, 1
    array = []
    for i in range(n):
        array.append(a)
        a, b = b, a + b
    return array

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

while True:
    data, addr = s.recvfrom(1024)
    n = data.decode()
    res = fib(int(n))
    s.sendto(str(res).encode(), addr)


