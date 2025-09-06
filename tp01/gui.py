import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
from utils.file_utils import select_image_file, select_save_path
from utils.image_utils import prepare_for_canvas
from .processing import adjust_luminance_saturation

# =====================
# Interfaz gráfica
# =====================

class ImageApp(ctk.CTk):
  def __init__(self):
    super().__init__()
    self.title("Procesador de Imágenes (YIQ)")
    self.geometry("950x750")
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    self.original_image = None
    self.processed_image = None
    self.tk_image = None
    self.a_value = ctk.DoubleVar(value=1.0)
    self.b_value = ctk.DoubleVar(value=1.0)

    # Frames y botones
    control_frame = ctk.CTkFrame(self)
    control_frame.pack(pady=15)

    self.btn_open = ctk.CTkButton(control_frame, text="📂 Abrir Imagen", command=self.open_image)
    self.btn_open.pack(side="left", padx=10)

    self.btn_save = ctk.CTkButton(control_frame, text="💾 Guardar Imagen", command=self.save_image, state="disabled")
    self.btn_save.pack(side="left", padx=10)

    # Sliders
    sliders_frame = ctk.CTkFrame(self)
    sliders_frame.pack(pady=10)

    ctk.CTkLabel(sliders_frame, text="Coeficiente Luminancia (a)").pack()
    self.slider_a = ctk.CTkSlider(
      sliders_frame,
      from_=0.1,
      to=2.0,
      variable=self.a_value,
      number_of_steps=100,
      command=self.update_image
    )
    self.slider_a.pack(padx=20, pady=5)

    ctk.CTkLabel(sliders_frame, text="Coeficiente Saturación (b)").pack()
    self.slider_b = ctk.CTkSlider(
      sliders_frame,
      from_=0.1,
      to=2.0,
      variable=self.b_value,
      number_of_steps=100,
      command=self.update_image
    )
    self.slider_b.pack(padx=20, pady=5)

    # Canvas
    self.canvas = ctk.CTkCanvas(self, width=850, height=550, bg="gray20", highlightthickness=0)
    self.canvas.pack(pady=10)

  def open_image(self):
    file_path = select_image_file()
    if file_path:
      self.original_image = Image.open(file_path).convert("RGB")
      self.update_image()
      self.btn_save.configure(state="normal")

  def show_image(self, img):
    self.tk_image = prepare_for_canvas(img)
    self.canvas.delete("all")
    self.canvas.create_image(425, 275, image=self.tk_image, anchor="center")

  def update_image(self, *_):
    """Actualiza la imagen usando los valores actuales de los sliders"""
    if self.original_image:
      a = self.a_value.get()
      b = self.b_value.get()
      self.processed_image = adjust_luminance_saturation(self.original_image, a, b)
      self.show_image(self.processed_image)

  def save_image(self):
    if self.processed_image:
      file_path = select_save_path()
      if file_path:
        self.processed_image.save(file_path)
        messagebox.showinfo("Éxito", "Imagen guardada correctamente.")
    else:
      messagebox.showerror("Error", "No hay imagen procesada para guardar.")
