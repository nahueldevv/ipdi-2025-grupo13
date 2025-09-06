from PIL import ImageTk

def prepare_for_canvas(img, max_size=(850, 550)):
  """
  Devuelve una versión redimensionada de la imagen para mostrar en canvas.
  """
  img_copy = img.copy()
  img_copy.thumbnail(max_size)
  return ImageTk.PhotoImage(img_copy)
