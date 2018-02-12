from http.server import BaseHTTPRequestHandler, HTTPServer
import importlib
# module = importlib.import_module('controlers')
import controleurs

base_html = """<!DOCTYPE html>
<html>
  <head>
    <title>Mini-Serveur</title>
    <style>
      input {
        padding: 4px 12px;
        border: 1px solid #ddd;
        border-radius: 4px;
        margin-bottom: 10px;
      }
    </style>
  </head>
  <body>
    <nav>
      <a href="/">Home</a> |
      <a href="/login">Login</a> |
      <a href="/register">Register</a>
    </nav>
    {body}
  </body>
</html>
"""

# HTTPRequestHandler class
class MiniHTTPServerRequestHandler(BaseHTTPRequestHandler):

  paths = {
    "/": "HomeController",
    "/login": "LoginController",
    "/register": "RegisterController"
  }

  # GET
  def do_GET(self):
        if not self.path in self.paths.keys():
            self.send_response(404)
            self.end_headers()
            return

        controller_class = self.paths[self.path]
        print(controller_class)
        class_ = getattr(controleurs, controller_class)
        instance = class_()
        html = instance.do_GET()

        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        # Send message back to client
        message = base_html.replace("{body}", html)

        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

  # POST: copier-coller en grande partie de do_GET:
  #   - on a ajouté deux lignes au début
  #   - on renvoie au client ce qu'il nous a envoyé (message = post_body)
  def do_POST(self):

        if not self.path in self.paths.keys():
            self.send_response(404)
            self.end_headers()
            return

        # Cette ligne récupère le(s) header(s) content-length
        # Même s'il n'y en a qu'un, get_all() renvoie une liste d'un élément
        content_len_headers = self.headers.get_all('content-length')

        # Si cette liste est vide, on ne peut pas continuer, car on ne sait pas combien
        # d'octets on doit lire : on renvoie une réponse avec code 400 (Bad Request)
        if not content_len_headers:
            self.send_response(400)
            self.end_headers()
            return

        # On convertit en entier la valeur string contenue dans le header content-type
        content_len = int(content_len_headers[0])
        # On lit ce nombre d'octets dans la requête
        post_body = self.rfile.read(content_len)
        # On convertit en chaîne le body
        body_str = str(post_body, 'utf-8')



        controller_class = self.paths[self.path]
        print(controller_class)
        class_ = getattr(controleurs, controller_class)
        instance = class_()
        html = instance.do_POST(body_str)



        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        # On renvoie cela tel quel au client
        message = base_html.replace("{body}", html)

        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

def run():
  print('starting server...')

  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('127.0.0.1', 8081)
  httpd = HTTPServer(server_address, MiniHTTPServerRequestHandler)
  print('running server...')
  httpd.serve_forever()

run()