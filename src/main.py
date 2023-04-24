from server import Server
from IrrigatorModel import Irrigator
from db import DB
import _thread

db = DB()

server = Server()
irrigators = db.getIrrigators() # get whats in the json file at startup
#irrigators = [Irrigator("test", "12:30", 30, 30, 3),Irrigator("test", "12:30", 30, 30, 3),Irrigator("test", "12:30", 30, 30, 3)]

def runIrrigate():
  while True:
    for irrigator in irrigators: # go through list of irrigators and turn on and off as needed
      irrigator.irrigate()

def runServer(irrigators, server):
  while True:
    server.reConnect() # if lost wifi reconnect
    server.serve(irrigators) # serve web page if connection pass irrigators to serve data

_thread.start_new_thread(runIrrigate,())
_thread.start_new_thread(runServer,(irrigators, server))




