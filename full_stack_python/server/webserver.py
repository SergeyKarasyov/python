from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>Hello!</body></hmtl>"
                self.wfile.write(output)
                print(output)
                return
        except IOError:
            self.send_error(404, "file not found %s".format(self.path))


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webserverHandler)
        print("web server running on a port: {}".format(port))
        server.serve_forever()
    except KeyboardInterrupt:
        print("web server was interrupted by ctrl+c")
        server.socket.close()


if __name__ == '__main__':
    main()
