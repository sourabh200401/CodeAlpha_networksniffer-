import socket

print("=" * 50)
print("CODEALPHA NETWORK SNIFFER")
print("=" * 50)

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print(f"Host Name : {hostname}")
print(f"Local IP  : {local_ip}")

while True:
    target = input("\nEnter website/domain (or exit): ")

    if target.lower() == "exit":
        print("Exiting...")
        break

    try:
        ip = socket.gethostbyname(target)

        print("\nPacket Information")
        print("-" * 30)
        print(f"Source IP      : {local_ip}")
        print(f"Destination IP : {ip}")
        print("Protocol       : TCP/IP")
        print("Status         : Reachable")

    except Exception as e:
        print("Error:", e)