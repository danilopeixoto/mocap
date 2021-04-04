from mocap.streaming import UDPClient


if __name__ == '__main__':
  with UDPClient('0.0.0.0', 8000) as client:
    while True:
      landmarks = client.read()
      print(landmarks)
