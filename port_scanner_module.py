import socket

def range_port_scanner(target_ip, start_port, end_port):
    print(f"\n[+] Scanning {target_ip} from port {start_port} to {end_port}")
    
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"[OPEN] Port {port}")
        s.close()
