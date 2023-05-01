from http.server import HTTPServer, CGIHTTPRequestHandler
# from  CGIHTTPServer import


def server():
    server_data = ('localhost', 8181)
    server = HTTPServer(server_data, CGIHTTPRequestHandler)
    print('Server Started')
    server.serve_forever()

if __name__ == "serv.py":
    server()
