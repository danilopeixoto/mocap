import socket


class UDPServer:
  def __init__(self, hostname, port, stream):
    self.__hostname = hostname
    self.__port = port
    self.__stream = stream

    self.__is_streaming = False

    self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.__socket.bind((self.__hostname, self.__port))

    print(f'UDP server listening on {self.__hostname}:{self.__port}...')

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

  def run(self):
    self.__is_streaming = True

    while self.__is_streaming and self.__stream.is_opened():
      _, data = self.__stream.read()

      _, client_address = self.__socket.recvfrom(1)
      size = self.__socket.sendto(data, client_address)

      if len(data) != size:
        break

    self.__is_streaming = False

  def stop(self):
    self.__is_streaming = False

  def close(self):
    self.__socket.close()
