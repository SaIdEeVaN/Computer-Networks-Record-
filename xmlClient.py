import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://localhost:10000/")

n = int(input("Enter a number: "))

result = server.isPrime(n)

if result:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")