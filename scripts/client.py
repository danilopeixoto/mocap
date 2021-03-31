import socket

from mocap.streaming import MotionDataEncoding


server_address = ('0.0.0.0', 8000)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
  motion_data_encoding = MotionDataEncoding()

  while True:
    size = sock.sendto(b'0', server_address)

    if size != 1:
      break

    size = motion_data_encoding.size()
    data, _ = sock.recvfrom(size)

    if len(data) == size:
      landmarks = motion_data_encoding.decode(data)
      print(landmarks)
