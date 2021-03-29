from datetime import datetime

import cv2


class FramerateDrawing:
  def __init__(self,
      offset = (10, 10),
      font_size = 10.0,
      font_color = (255, 255, 255)):
    self.__offset = offset
    self.__font_size = font_size
    self.__font_color = font_color

    (_, font_height), _ = cv2.getTextSize(
      'text', cv2.FONT_HERSHEY_SIMPLEX, 1.0, 1)

    self.__font_scale = self.__font_size / font_height

    self.__fps = 0

    self.reset()

  def offset(self):
    return self.__offset

  def font_size(self):
    return self.__font_size

  def font_color(self):
    return self.__font_color

  def fps(self):
    return self.__fps

  def reset(self):
    self.__start_time = datetime.now()
    self.__count = 0

  def update(self):
    elapsed_time = (datetime.now() - self.__start_time).total_seconds()

    self.__fps = self.__count / elapsed_time if elapsed_time > 0 else 0
    self.__count += 1

  def process(self, image, features = None):
    x, y = self.__offset
    height, _, _ = image.shape

    cv2.putText(
      image,
      '{:.0f} fps'.format(self.__fps),
      (x, height - y),
      cv2.FONT_HERSHEY_SIMPLEX,
      self.__font_scale,
      self.__font_color,
      1,
      cv2.LINE_AA)

    self.update()

    return image, features
