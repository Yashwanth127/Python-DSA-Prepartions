import subprocess
import sys

def scan_network(ip_range):
    print("Network scan using nmap (run on Kali Linux):")
    result = subprocess.run(['nmap', '-sn', ip_range], capture_output=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python network_scanner.py 192.168.1.0/24")
    else:
        scan_network(sys.argv[1])