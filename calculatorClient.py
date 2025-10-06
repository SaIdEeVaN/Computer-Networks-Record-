import xmlrpc.client
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/RPC2")
print("XML-RPC Calculator Client")
print("Available operations: add, subtract, multiply, divide")
print("Type 'exit' to quit.\n")
while True:
    try:
        cmd = input("Enter operation (e.g., add 5 3): ").strip()
        if cmd.lower() == 'exit':
            break
        parts = cmd.split()
        if len(parts) != 3:
            print("Invalid input. Format: <operation> <num1> <num2>")
            continue
        op, x, y = parts[0], float(parts[1]), float(parts[2])
        if not hasattr(proxy, op):
            print(f"Unknown operation: {op}")
            continue
        result = getattr(proxy, op)(x, y)
        print(f"Result: {result}\n")
    except Exception as e:
        print(f"Error: {e}\n")
