from queue import Queue
from threading import Thread
from functools import reduce


class ComputeStream:
  def __init__(self, stream, buffer_size = 100):
    self.__stream = stream
    self.__buffer_size = buffer_size

    self.__is_opened = False

    self.__buffer = Queue(maxsize = self.__buffer_size)
    self.__stages = []

  def __process_stage(self, args, stage):
    return stage.process(*args)

  def __process(self):
    self.__is_opened = True

    while self.__is_opened and self.__stream.is_opened():
      if not self.__buffer.full():
        inputs = self.__stream.read()

        outputs = reduce(
          self.__process_stage,
          self.__stages,
          inputs)

        self.__buffer.put(outputs)

    self.__is_opened = False

  def stream(self):
    return self.__stream

  def buffer_size(self):
    return self.__buffer_size

  def is_opened(self):
    return self.__is_opened

  def add_stage(self, stage):
    self.__stages.append(stage)

  def remove_stage(self, stage):
    self.__stages.remove(stage)

  def has_stage(self, stage):
    return stage in self.__stages

  def process(self):
    thread = Thread(target = self.__process, daemon = True)
    thread.start()

  def close(self):
    self.__is_opened = False

  def read(self):
    return self.__buffer.get()
