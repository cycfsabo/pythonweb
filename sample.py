#!/usr/bin/env python
 
import textwrap
 
from six.moves.BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
 
 
class HelloRequestHandler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        if self.path != '/':
            self.send_error(404, "Object not found")
            return
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Hello World</title>
            </head>
            <body>
                <h1>Hello, World!</h1>
                <p>... Here we are!</p>
                <p>I'm a DevOps Engineer</p>
                <h2>I'm Deploy-server. You have deployed webserver successfully!</h2>
                <h3>Jadon Sancho is red. Here we go!</h3>
                <h3>Done!</h3>
            </body>
            </html>
        ''')
        self.wfile.write(response_text.encode('utf-8'))
 
 
server_address = ('', 8000)
httpd = HTTPServer(server_address, HelloRequestHandler)
httpd.serve_forever()
