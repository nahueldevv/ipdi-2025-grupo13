from PIL import Image
import numpy as np

# =====================
# Procesamiento de imagen (YIQ)
# =====================
def rgb_to_yiq(rgb):
  rgb2yiq = np.array([
    [0.299, 0.587, 0.114],
    [0.596, -0.274, -0.322],
    [0.211, -0.523, 0.312]
  ])
  return np.dot(rgb, rgb2yiq.T)

def yiq_to_rgb(yiq):
  yiq2rgb = np.array([
    [1.0, 0.956, 0.621],
    [1.0, -0.272, -0.647],
    [1.0, -1.106, 1.703]
  ])
  return np.dot(yiq, yiq2rgb.T)

def adjust_luminance_saturation(image, a=1.0, b=1.0):
  # Convertir imagen a numpy normalizado
  pixels = np.array(image, dtype=float) / 255.0

  # RGB -> YIQ
  yiq = rgb_to_yiq(pixels)

  # Ajustar Y, I, Q
  yiq[..., 0] *= a
  yiq[..., 1] *= b
  yiq[..., 2] *= b

  # Clamping
  yiq[..., 0] = np.clip(yiq[..., 0], 0, 1)
  yiq[..., 1] = np.clip(yiq[..., 1], -0.5957, 0.5957)
  yiq[..., 2] = np.clip(yiq[..., 2], -0.5226, 0.5226)

  # YIQ -> RGB
  rgb = yiq_to_rgb(yiq)
  rgb = np.clip(rgb, 0, 1)

  # Convertir a imagen PIL
  return Image.fromarray((rgb * 255).astype(np.uint8))
