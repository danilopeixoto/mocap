class WebRTCServer:
  def __init__(self, hostname, port, stream):
    self.__hostname = hostname
    self.__port = port
    self.__stream = stream

  def hostname(self):
    return self.__hostname

  def port(self):
    return self.__port

  def stream(self):
    return self.__stream

  def run(self):
    while True:
      pass
