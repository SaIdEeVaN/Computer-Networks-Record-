import socket, time

host = "google.com"
port = 80
count = 4
times = []

for i in range(count):
    try:
        s = socket.socket()
        start = time.time()
        s.connect((host, port))
        end = time.time()
        s.close()
        rtt = (end - start) * 1000
        times.append(rtt)
        print(f"Reply from {host}: Time = {rtt:.2f} ms")
    except:
        print("Requested timed out")

print("Min RTT = {:.2f} ms".format(min(times)))
print("Max RTT = {:.2f} ms".format(max(times)))
print("Avg RTT = {:.2f} ms".format(sum(times)/len(times)))


