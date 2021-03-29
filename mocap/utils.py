import numpy as np
from PIL import Image, ImageOps


def resize(image, size, padding = False):
  image = Image.fromarray(image)
  image = ImageOps.pad(image, size) if padding else ImageOps.fit(image, size)

  return np.asarray(image)
