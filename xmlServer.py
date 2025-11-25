from xmlrpc.server import SimpleXMLRPCServer

def isPrime(n):
    if n < 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

server = SimpleXMLRPCServer(("0.0.0.0", 10000))
server.register_function(isPrime, "isPrime")
server.serve_forever()
