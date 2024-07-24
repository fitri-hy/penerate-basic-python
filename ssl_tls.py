import ssl
import socket

def check_ssl_tls(host, port):
    context = ssl.create_default_context()
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=host)
    try:
        conn.connect((host, port))
        ssl_info = conn.getpeercert()
        print(f"SSL/TLS Certificate: {ssl_info}")
    except Exception as e:
        print(f"SSL/TLS Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    target_host = "example.com"
    target_port = 443
    check_ssl_tls(target_host, target_port)
