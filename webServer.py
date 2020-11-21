# https://www.youtube.com/watch?v=hFNZ6kdBgO0
from http.server import HTTPServer, BaseHTTPRequestHandler

class Serv(BaseHTTPRequestHandler):

    def do_Get(self):
        if self.path == "/":
            self.path = "/welcome.html"
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, "utf-8"))

httpd = HTTPServer(("localhost", 8080),Serv)
httpd.serve_forever()