import socket
import datetime

# Services les plus connus
SERVICES = {
    21: "FTP", 22: "SSH", 23: "Telnet",
    25: "SMTP", 53: "DNS", 80: "HTTP",
    110: "POP3", 143: "IMAP", 443: "HTTPS",
    3306: "MySQL", 3389: "RDP", 8080: "HTTP-Alt"
}

def scan_ports(target, start_port, end_port):
    print("-" * 50)
    print(f"Scanning Target: {target}")
    print(f"Time: {datetime.datetime.now()}")
    print("-" * 50)
    
    open_ports = []
    
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                service = SERVICES.get(port, "Unknown")
                print(f"[OPEN] Port {port} --> {service}")
                open_ports.append(port)
            sock.close()
        except:
            pass
    
    # Save résultats f fichier
    with open("scan_report.txt", "w") as f:
        f.write(f"Scan Report\n")
        f.write(f"Target: {target}\n")
        f.write(f"Time: {datetime.datetime.now()}\n")
        f.write(f"Open Ports: {len(open_ports)}\n")
        f.write("-" * 50 + "\n")
        for port in open_ports:
            service = SERVICES.get(port, "Unknown")
            f.write(f"[OPEN] Port {port} --> {service}\n")
    
    print("-" * 50)
    print(f"Scan Complete! {len(open_ports)} open ports found")
    print(f"Report saved: scan_report.txt")
    return open_ports

# Main
target = input("Enter target IP or website: ")
start = int(input("Start port: "))
end = int(input("End port: "))

scan_ports(target, start, end)