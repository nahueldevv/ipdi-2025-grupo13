import numpy as np
from PIL import Image
from tp01.processing import rgb_to_yiq, yiq_to_rgb   # reusamos del TP01


def to_numpy(img):
  return np.array(img, dtype=float) / 255.0

def to_image(arr):
  arr = np.clip(arr, 0, 1)
  return Image.fromarray((arr * 255).astype(np.uint8))


# -----------------------------
# Filtros de luminancia
# -----------------------------
def filtro_raiz(img):
  arr = to_numpy(img)
  yiq = rgb_to_yiq(arr)
  yiq[..., 0] = np.sqrt(yiq[..., 0])
  rgb = yiq_to_rgb(yiq)
  return to_image(rgb)

def filtro_cuadrado(img):
  arr = to_numpy(img)
  yiq = rgb_to_yiq(arr)
  yiq[..., 0] = yiq[..., 0] ** 2
  rgb = yiq_to_rgb(yiq)
  return to_image(rgb)

def filtro_lineal_trozos(img, ymin=0.2, ymax=0.8):
  arr = to_numpy(img)
  yiq = rgb_to_yiq(arr)
  Y = yiq[..., 0]

  Yp = np.zeros_like(Y)
  Yp[Y < ymin] = 0
  Yp[Y > ymax] = 1
  mask = (Y >= ymin) & (Y <= ymax)
  Yp[mask] = (Y[mask] - ymin) / (ymax - ymin)

  yiq[..., 0] = Yp
  rgb = yiq_to_rgb(yiq)
  return to_image(rgb)
