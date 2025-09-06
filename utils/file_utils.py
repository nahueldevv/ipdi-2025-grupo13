from tkinter import filedialog

def select_image_file():
  return filedialog.askopenfilename(
    filetypes=[("Archivos de imagen", "*.jpg *.jpeg *.png *.bmp *.gif")]
  )

def select_save_path():
  return filedialog.asksaveasfilename(
    defaultextension=".jpg",
    filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("BMP", "*.bmp")]
  )