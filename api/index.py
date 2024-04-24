from http.server import BaseHTTPRequestHandler
from utils import add
import sma
from main import identify_wick_parallel

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        print("hello")
        result = add(3,2)
        print(result)
        res = identify_wick_parallel()
        print(res)
        return
