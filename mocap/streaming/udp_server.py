import socket

import numpy as np


class UDPServer:
  def __init__(self, hostname, port, stream):
    self.__hostname = hostname
    self.__port = port
    self.__stream = stream

    self.__is_streaming = False

    self.__address = (self.__hostname, self.__port)

    self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.__socket.bind(self.__address)

  def __preprocess_landmark(self, landmark):
    return landmark.x, landmark.y, landmark.z

  def __preprocess(self, landmarks):
    return list(map(self.__preprocess_landmark, landmarks.landmark))

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
      _, landmarks = self.__stream.read()

      data = np.array(
        list(map(self.__preprocess, landmarks)),
        dtype = np.float32).tobytes()

      if len(data) > 0:
        try:
          self.__socket.sendto(data, self.__address)
        except socket.error:
          break

    self.__is_streaming = False

  def stop(self):
    self.__is_streaming = False
