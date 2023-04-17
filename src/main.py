from server import Server
from IrrigatorModel import Irrigator
from db import DB

db = DB()

server = Server()
#irrigators = db.getIrrigators() # get whats in the json file at startup
irrigators = [Irrigator("test", "12:30", 30, 30, 3),Irrigator("test", "12:30", 30, 30, 3),Irrigator("test", "12:30", 30, 30, 3)]

while True:
  server.reConnect() # if lost wifi reconnect
  server.serve(irrigators) # serve web page if connection pass irrigators to serve data
  for irrigator in irrigators: # go through list of irrigators and turn on and off as needed
    irrigator.irrigate()