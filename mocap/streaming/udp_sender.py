import socket


class UDPSender:
  def __init__(self, hostname, port, stream):
    self.__hostname = hostname
    self.__port = port
    self.__stream = stream

    self.__is_streaming = False
    self.__address = (self.__hostname, self.__port)

    self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

  def __enter__(self):
    return self

  def __exit__(self, type, value, traceback):
    return self.close()

  def hostname(self):
    return self.__hostname

  def port(self):
    return self.__port

  def stream(self):
    return self.__stream

  def is_streaming(self):
    return self.__is_streaming

  def send(self):
    self.__is_streaming = True

    while self.__is_streaming and self.__stream.is_opened():
      _, data = self.__stream.read()
      self.__socket.sendto(data, self.__address)

    self.__is_streaming = False

  def stop(self):
    self.__is_streaming = False

  def close(self):
    self.__socket.close()
