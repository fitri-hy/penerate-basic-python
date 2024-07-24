import socket

def scan_ports(host, ports):
    open_ports = []
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
    return open_ports

if __name__ == "__main__":
    target_host = "example.com"
    target_ports = [22, 80, 443, 8080]
    open_ports = scan_ports(target_host, target_ports)
    print(f"Open ports on {target_host}: {open_ports}")
