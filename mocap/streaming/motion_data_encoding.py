import json


class MotionDataEncoding:
  def __transform_landmark(self, landmark):
    return landmark.x - 0.5, 0.5 - landmark.y, -landmark.z

  def __format(self, landmarks):
    return list(map(self.__transform_landmark, landmarks.landmark))

  def size(self):
    return 2048

  def encode(self, landmarks):
    return json.dumps(list(map(self.__format, landmarks))).encode('utf-8')

  def decode(self, data):
    return json.loads(data.decode('utf-8'))

  def process(self, image, landmarks):
    return image, self.encode(landmarks)
