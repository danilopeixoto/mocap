import mediapipe as mp
import cv2


class HandTracking:
  def __init__(
      self,
      maximum_number_detections = 1,
      minimum_detection_confidence = 0.5,
      minimum_tracking_confidence = 0.5):
    self.__maximum_number_detections = maximum_number_detections
    self.__minimum_detection_confidence = minimum_detection_confidence
    self.__minimum_tracking_confidence = minimum_tracking_confidence

    self.__hand_model = mp.solutions.hands.Hands(
      max_num_hands = self.__maximum_number_detections,
      min_detection_confidence = self.__minimum_detection_confidence,
      min_tracking_confidence = self.__minimum_tracking_confidence)

  def __enter__(self):
    return self

  def __exit__(self, type, value, traceback):
    self.close()

  def maximum_number_detections(self):
    return self.__maximum_number_detections

  def minimum_detection_confidence(self):
    return self.__minimum_detection_confidence

  def minimum_tracking_confidence(self):
    return self.__minimum_tracking_confidence

  def process(self, image, constraints = None):
    input_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    input_image.flags.writeable = False

    results = self.__hand_model.process(input_image)
    landmarks = results.multi_hand_landmarks or []

    return image, landmarks

  def close(self):
    self.__hand_model.close()
