import mediapipe as mp
import cv2


class HandDrawing:
  def __init__(
      self,
      landmark_color = (255, 0, 255),
      landmark_radius = 4,
      connection_color = (255, 255, 0),
      connection_thickness = 2):
    self.__landmark_color = landmark_color
    self.__landmark_radius = landmark_radius
    self.__connection_color = connection_color
    self.__connection_thickness = connection_thickness

    self.__landmark_spec = mp.solutions.drawing_utils.DrawingSpec(
      self.__landmark_color, cv2.FILLED, self.__landmark_radius)

    self.__connection_spec = mp.solutions.drawing_utils.DrawingSpec(
      self.__connection_color, self.__connection_thickness)

  def landmark_color(self):
    return self.__landmark_color

  def landmark_radius(self):
    return self.__landmark_radius

  def connection_color(self):
    return self.__connection_color

  def connection_thickness(self):
    return self.__connection_thickness

  def process(self, image, landmarks):
    for landmark in landmarks:
      mp.solutions.drawing_utils.draw_landmarks(
        image,
        landmark,
        mp.solutions.hands.HAND_CONNECTIONS,
        self.__landmark_spec,
        self.__connection_spec)

    return image, landmarks
