import cv2


class VideoPlayer:
  def __init__(self, title, stream):
    self.__title = title
    self.__stream = stream

    self.__is_playing = False

  def title(self):
    return self.__title

  def stream(self):
    return self.__stream

  def is_playing(self):
    return self.__is_playing

  def play(self):
    self.__is_playing = True

    while self.__is_playing and self.__stream.is_opened():
      image, _ = self.__stream.read()

      cv2.imshow(self.__title, image)

      if cv2.waitKey(5) & 0xFF == 27:
        cv2.destroyAllWindows()
        break

    self.__is_playing = False

  def stop(self):
    self.__is_playing = False
