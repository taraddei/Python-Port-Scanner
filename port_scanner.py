# port_scanner.py

import socket

def scan_ports(target, start_port, end_port):
    print(f"Scanning ports on {target} from {start_port} to {end_port}...")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Timeout for connection attempt
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

if __name__ == "__main__":
    target_host = input("Enter the IP address or hostname to scan: ")
    start = int(input("Enter the starting port number: "))
    end = int(input("Enter the ending port number: "))
    scan_ports(target_host, start, end)
