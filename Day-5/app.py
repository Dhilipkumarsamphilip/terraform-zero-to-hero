from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Hello, Chris Paul Matthew!")
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=SimpleHandler):
    server_address = ('0.0.0.0', 80)
    httpd = server_class(server_address, handler_class)
    print("Starting HTTP server on port 80...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
