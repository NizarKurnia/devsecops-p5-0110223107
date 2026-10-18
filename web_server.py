import http.server
import socketserver

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"=== Web Server Berjalan di port {PORT} ===")
        print("Buka http://localhost:8000 di browser Anda.")
        httpd.serve_forever()