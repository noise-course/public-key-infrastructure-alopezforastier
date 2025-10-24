import http.server
import ssl

handler = http.server.SimpleHTTPRequestHandler

httpd = http.server.HTTPServer(("127.0.0.1", 8443), handler)

context = ssl.SSLContext(ssl.PROTOCOL_TLS)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("Serving HTTPS on https://localhost:8443")
httpd.serve_forever()
