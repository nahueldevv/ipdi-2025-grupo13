import numpy as np
from PIL import Image
from tp01.processing import rgb_to_yiq, yiq_to_rgb   # Reusamos lo ya hecho en tp01


# =====================
# Helpers
# =====================
def to_numpy(img):
  """Convierte PIL.Image a numpy normalizado [0,1]."""
  return np.array(img, dtype=float) / 255.0

def to_image(arr):
  """Convierte numpy normalizado [0,1] a PIL.Image en [0,255]."""
  arr = np.clip(arr, 0, 1)
  return Image.fromarray((arr * 255).astype(np.uint8))


# =====================
# 1 - Cuasi suma y resta en RGB
# =====================
def cuasi_suma_rgb(img1, img2):
  arr1, arr2 = to_numpy(img1), to_numpy(img2)
  res = (arr1 + arr2) / 2.0   # promediada
  return to_image(res)

def cuasi_resta_rgb(img1, img2):
  arr1, arr2 = to_numpy(img1), to_numpy(img2)
  res = (arr1 - arr2 + 1.0) / 2.0   # shift + promediada
  return to_image(res)


# =====================
# 2 - Ídem en YIQ
# =====================
def cuasi_suma_yiq(img1, img2):
  arr1, arr2 = to_numpy(img1), to_numpy(img2)
  yiq1, yiq2 = rgb_to_yiq(arr1), rgb_to_yiq(arr2)
  yiq_res = (yiq1 + yiq2) / 2.0
  rgb_res = yiq_to_rgb(yiq_res)
  return to_image(rgb_res)

def cuasi_resta_yiq(img1, img2):
  arr1, arr2 = to_numpy(img1), to_numpy(img2)
  yiq1, yiq2 = rgb_to_yiq(arr1), rgb_to_yiq(arr2)
  yiq_res = (yiq1 - yiq2 + 1.0) / 2.0
  rgb_res = yiq_to_rgb(yiq_res)
  return to_image(rgb_res)


# =====================
# 3 - Producto y cociente
# =====================
def producto(img1, img2):
  arr1, arr2 = to_numpy(img1), to_numpy(img2)
  res = arr1 * arr2
  return to_image(res)

def cociente(img1, img2):
  arr1, arr2 = to_numpy(img1), to_numpy(img2)
  res = np.divide(arr1, arr2 + 1e-6)   # evitar div/0
  res = np.clip(res, 0, 1)
  return to_image(res)


# =====================
# 4 - Resta absoluta
# =====================
def resta_absoluta(img1, img2):
  arr1, arr2 = to_numpy(img1), to_numpy(img2)
  res = np.abs(arr1 - arr2)
  return to_image(res)


# =====================
# 5 - If-darker y If-lighter
# =====================
def if_darker(img1, img2):
  arr1, arr2 = to_numpy(img1), to_numpy(img2)
  res = np.minimum(arr1, arr2)
  return to_image(res)

def if_lighter(img1, img2):
  arr1, arr2 = to_numpy(img1), to_numpy(img2)
  res = np.maximum(arr1, arr2)
  return to_image(res)
