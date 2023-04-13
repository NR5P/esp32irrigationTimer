try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

class Server:
  def __init__(self):
    self.led = Pin(2, Pin.OUT)
    self.ssid = 'taxation_is_theft_2_4'
    self.password = ''
    self.station = network.WLAN(network.STA_IF)
    self.station.active(True)
    self.reConnect()
    self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.s.bind(('', 80))
    self.s.listen(5)


  def web_page(self):
    if self.led.value() == 1:
      gpio_state="ON"
    else:
      gpio_state="OFF"

    with open('main.html', 'r') as file:
      data = file.read().replace('\n', '').replace("|||gpio_state|||",gpio_state)
    return data

  def serve(self):
    conn, addr = self.s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
    led_on = request.find('/?led=on')
    led_off = request.find('/?led=off')
    if led_on == 6:
      print('LED ON')
      self.led.value(1)
    if led_off == 6:
      print('LED OFF')
      self.led.value(0)
    response = self.web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()

  def reConnect(self):
    if self.station.isconnected() == True:
      return
    self.station.connect(self.ssid, self.password)
    while self.station.isconnected() == False:
        pass
    print('Connection successful')
    print(self.station.ifconfig())
