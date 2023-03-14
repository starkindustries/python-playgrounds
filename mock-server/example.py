import http.server
import unittest
import threading
import urllib.request

class MockIpifyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """HTTPServer mock request handler"""

    def do_GET(self):  # pylint: disable=invalid-name
        """Handle GET requests"""
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"ip":"1.2.3.42"}')

    def log_request(self, code=None, size=None):
        """Don't log anything"""


class UnitTests(unittest.TestCase):
    """Unit tests for urlopen"""

    def test_urlopen(self):
        """Test urlopen ipify"""
        server = http.server.ThreadingHTTPServer(
            ("127.0.0.1", 9999), MockIpifyHTTPRequestHandler
        )
        with server:
            server_thread = threading.Thread(target=server.serve_forever)
            server_thread.daemon = True
            server_thread.start()

            request = request = urllib.request.Request("http://127.0.0.1:9999/")
            with urllib.request.urlopen(request) as response:
                result = response.read()
            server.shutdown()

        print(f"RESULT: [{result}]")
        self.assertEqual(result, b'{"ip":"1.2.3.42"}')


if __name__ == '__main__':
    unittest.main()