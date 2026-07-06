import socket
import sys

def check_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex(('127.0.0.1', port))
        sock.close()
        return result == 0
    except Exception as e:
        print(f"Error checking port: {e}")
        return False

if __name__ == "__main__":
    port = 7545
    if check_port(port):
        print(f"Port {port} is open - Ganache appears to be running")
        sys.exit(0)
    else:
        print(f"Port {port} is not open - Ganache is not running on port {port}")
        print("Please start Ganache with: ganache-cli --port 7545")
        sys.exit(1)