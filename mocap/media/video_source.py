from queue import Queue
from threading import Thread

import cv2

from .. import utils


class VideoSource:
  def __init__(
      self,
      source,
      size,
      padding,
      buffer_size = 100):
    self.__source = source
    self.__size = size
    self.__padding = padding
    self.__buffer_size = buffer_size

    self.__is_opened = False

    self.__buffer = Queue(maxsize = self.__buffer_size)

    self.__capture = cv2.VideoCapture(self.__source)
    self.__capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.__size[0])
    self.__capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.__size[1])

  def __open(self):
    self.__is_opened = True

    while self.__is_opened:
      if not self.__buffer.full():
        success, image = self.__capture.read()

        if success:
          resized_image = utils.resize(
            cv2.flip(image, 1),
            self.__size,
            self.__padding)

          self.__buffer.put((resized_image, self.__size))
        else:
          self.__is_opened = False

  def source(self):
    return self.__source

  def size(self):
    return self.__size

  def padding(self):
    return self.__padding

  def buffer_size(self):
    return self.__buffer_size

  def is_opened(self):
    return self.__is_opened

  def open(self):
    thread = Thread(target = self.__open, daemon = True)
    thread.start()

  def close(self):
    self.__is_opened = False

  def read(self):
    return self.__buffer.get()
