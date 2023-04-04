from http.server import BaseHTTPRequestHandler, HTTPServer

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if not is_authenticated(self):
            self.send_response(302)
            self.send_header("Location", "https://example.com/")
            self.end_headers()
            return
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello, world!")

def is_authenticated(request_handler):
    # implement your authentication logic here
    return False # return True if authenticated, False otherwise

if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, MyRequestHandler)
    sockname = httpd.socket.getsockname()
    print(f"Server started on {sockname[0]}:{sockname[1]}")
    httpd.serve_forever()
