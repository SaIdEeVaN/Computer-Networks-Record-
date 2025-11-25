from scapy.all import sniff, Ether, IP, TCP, UDP, ICMP
from datetime import datetime
def process_packet(packet):
    print("=" * 80)
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    if Ether in packet:
        ether = packet[Ether]
        print(f"Ethernet: {ether.src} -> {ether.dst} | Type: {hex(ether.type)}")
    if IP in packet:
        ip = packet[IP]
        print(f"IP: {ip.src} -> {ip.dst} | Protocol: {ip.proto} | TTL: {ip.ttl}")
        if TCP in packet:
            tcp = packet[TCP]
            print(f"TCP: {tcp.sport} -> {tcp.dport} | Flags: {tcp.flags} | Seq: {tcp.seq}")
        elif UDP in packet:
            udp = packet[UDP]
            print(f"UDP: {udp.sport} -> {udp.dport}")
        elif ICMP in packet:
            icmp = packet[ICMP]
            print(f"ICMP: Type {icmp.type} Code {icmp.code}")
    payload = bytes(packet.payload)
    if payload:
        max_len = 128
        display = payload[:max_len]
        print(f"Payload ({len(payload)} bytes):")
        print(display.hex(' ', 1))
        if len(payload) > max_len:
            print(f"... (truncated {len(payload) - max_len} bytes)")
    print()
def main():
    print("Starting packet capture. Press Ctrl+C to stop.")
    sniff(prn=process_packet, store=False)
if __name__ == "__main__":
    main()
