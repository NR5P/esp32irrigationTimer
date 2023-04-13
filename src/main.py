from server import Server

server = Server()

while True:
  server.reConnect()
  server.serve()