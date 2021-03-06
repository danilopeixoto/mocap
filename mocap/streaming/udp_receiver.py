import socket

from . import MotionDataEncoding


class UDPReceiver:
  def __init__(self, hostname, port, timeout = 1):
    self.__hostname = hostname
    self.__port = port
    self.__timeout = timeout

    self.__address = (self.__hostname, self.__port)

    self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.__socket.bind(self.__address)
    self.__socket.settimeout(self.__timeout)

    self.__encoding = MotionDataEncoding()

  def __enter__(self):
    return self

  def __exit__(self, type, value, traceback):
    self.close()

  def hostname(self):
    return self.__hostname

  def port(self):
    return self.__port

  def timeout(self):
    return self.__timeout

  def close(self):
    self.__socket.close()

  def read(self):
    data, _ = self.__socket.recvfrom(self.__encoding.size())

    return self.__encoding.decode(data)
