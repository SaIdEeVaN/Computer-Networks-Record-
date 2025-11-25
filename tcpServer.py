import socket
import math

host = "0.0.0.0"
port = 80

def isPrime(n):
    # Handle the definition of prime numbers: must be greater than 1
    if n <= 1:
        return False
    
    # Handle the only even prime number (2)
    if n == 2:
        return True
    
    # Optimization: All even numbers greater than 2 are not prime
    if n % 2 == 0:
        return False

    # Check for factors from 3 up to the square root of n, skipping even numbers
    # math.isqrt(n) is the integer square root, we add 1 to include it in the range
    limit = math.isqrt(n)
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
            
    return True

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen(3)

    while True:
        conn, addr = s.accept()
        print("Connected: ", addr)

        with conn:
            data = conn.recv(1024).decode()
            if not data:
                break

            n = int(data)
            res = isPrime(n)

            conn.send(str(res).encode())

            