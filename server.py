#https://127.0.0.1:4443
#!/usr/bin/env python
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import json
import ssl
my_json = {
  "count": '2',
  "results": [{"name":"Dayana"},{"name":"Miguel"},{"name":"Iván"}]
}
my_json['count'] = len(my_json['results'])
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
      parsed_path = urlparse(self.path)
      self.send_response(200)
      self.send_header('Content-type', 'application/json')
      self.send_header('Access-Control-Allow-Origin', '*')
      self.end_headers()
      """self.wfile.write(json.dumps({
          'method': self.command,
          'path': self.path,
          'real_path': parsed_path.query,
          'query': parsed_path.query,
          'request_version': self.request_version,
          'protocol_version': self.protocol_version
      }).encode()) """
      self.wfile.write(json.dumps(my_json).encode())
      return
def run(host='localhost', port=4443):
    #server = HTTPServer((host, port), RequestHandler)
    # To generate key and cert files with OpenSSL use following command:
    # openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365
    server = HTTPServer((host, port), RequestHandler)
    server.socket = ssl.wrap_socket (server.socket, 
        keyfile="./key.pem", 
        certfile='./cert.pem', server_side=True)
    print('Starting server at http://'+host+':'+str(port))
    server.serve_forever()
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()