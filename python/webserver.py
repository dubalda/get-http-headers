from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import logging

PORT = 5002

f= open("index.html","w+")
f.write("<h1>HTTP headers</h1>")
f.close()

class GetHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
          self.path = '/index.html'
        logging.error(self.headers)
        print('TEST User-Agent: ' + self.headers.get('User-Agent'))
        f = open("index.html", "a+")
        for key in self.headers.keys():
            print(key)
            f.write('<br><b>' + key + ':</b> ' + self.headers.get(key))
        f.write('<br><br>')
        f.close()
        SimpleHTTPRequestHandler.do_GET(self)

Handler = GetHandler
httpd = TCPServer(("", PORT), Handler)
print("Started httpserver on port ", PORT)
httpd.serve_forever()
