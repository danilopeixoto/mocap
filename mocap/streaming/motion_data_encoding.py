import numpy as np


class MotionDataEncoding:
  def __init__(self, precision = float):
    self.__precision = precision

  def __transform_landmark(self, landmark):
    return landmark.x - 0.5, 0.5 - landmark.y, -landmark.z

  def __format(self, landmarks):
    return list(map(self.__transform_landmark, landmarks.landmark))

  def precision(self):
    return self.__precision

  def shape(self):
    return (1, 21, 3)

  def length(self):
    return np.prod(self.shape())

  def size(self):
    return self.length() * np.dtype(self.__precision).itemsize

  def encode(self, landmarks):
    return np.array(
      list(map(self.__format, landmarks)),
      dtype = self.__precision).tobytes()

  def decode(self, data):
    return np.reshape(
      np.frombuffer(data, dtype = self.__precision),
      self.shape())

  def process(self, image, landmarks):
    return image, self.encode(landmarks)
