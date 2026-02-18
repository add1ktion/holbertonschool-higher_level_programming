#!/usr/bin/python3
"""Simple HTTP API: /, /data (JSON), /status (OK), 404 else."""
import http.server
import socketserver
import json

PORT = 8000


class Handler (http.server.BaseHTTPRequestHandler):
    """HTTP request handler for the simple API."""

    def do_GET(self):
        """Handle GET requests for different endpoints."""
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!\n")

        elif self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode() + b"\n")

        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK\n")

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Not Found\n")


if __name__ == "__main__":
    """Start the HTTP server."""
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serveur démarré: http://localhost:{PORT}")
        httpd.server_forever()
