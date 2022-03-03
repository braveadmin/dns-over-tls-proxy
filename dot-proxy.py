import socket
import ssl

# requests are handled here
def requestHandle(data, addr, DNS, DOT_PORT):
    tls_conn_sock = tls_connection(DNS, DOT_PORT)
    tcp_result = sendQuery(tls_conn_sock, data)
    return tcp_result

# Create an SSL context with Cloudflare ----------------------
def tls_connection(DNS, DOT_PORT):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)
    context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    context.verify_mode = ssl.CERT_REQUIRED
    context.load_verify_locations('/etc/ssl/certs/ca-certificates.crt')
    wrappedSocket = context.wrap_socket(sock, server_hostname=DNS)
    wrappedSocket.connect((DNS, DOT_PORT))
    return wrappedSocket

# Send the query to Cloudflare DNS server -------------------
def sendQuery(tls_conn_sock, data):
    tls_conn_sock.send(data)
    result = tls_conn_sock.recv(1024)
    tls_conn_sock.close()
    return result

# Main function --------------------------------------------
if __name__ == '__main__':
    PORT = 53
    HOST = socket.gethostbyname(socket.gethostname())
    DOT_PORT = 853
    DNS = '1.1.1.1'

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(10)
    while True:
        conn, addr = server.accept()
        data = conn.recv(1024)
        result = target=requestHandle(data, addr, DNS, DOT_PORT)
        conn.sendto(result, addr)
except Exception as e:
    print(e)
    server.close()
