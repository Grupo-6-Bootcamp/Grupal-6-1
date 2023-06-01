import http.server
import socketserver

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Bienvenidos a TeLoVendo')
        
with socketserver.TCPServer(('', 8000), MyHandler) as httpd:
    print('Servidor activo en el puerto 8000...')
    httpd.serve_forever()