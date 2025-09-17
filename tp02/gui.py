import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
from utils.file_utils import select_image_file, select_save_path
from utils.image_utils import prepare_for_canvas
import tp02.processing as proc


class ImageApp(ctk.CTk):
  def __init__(self):
    super().__init__()

    self.title("Aritmética de píxeles (TP02)")
    self.geometry("1100x750")
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    self.img1 = None
    self.img2 = None
    self.processed_image = None
    self.tk_img1 = None
    self.tk_img2 = None
    self.tk_processed = None

    # Frame de control superior
    control_frame = ctk.CTkFrame(self)
    control_frame.pack(pady=15)

    self.btn_open1 = ctk.CTkButton(control_frame, text="📂 Abrir Imagen 1", command=self.open_image1)
    self.btn_open1.pack(side="left", padx=10)

    self.btn_open2 = ctk.CTkButton(control_frame, text="📂 Abrir Imagen 2", command=self.open_image2)
    self.btn_open2.pack(side="left", padx=10)

    self.btn_save = ctk.CTkButton(control_frame, text="💾 Guardar Resultado", command=self.save_image, state="disabled")
    self.btn_save.pack(side="left", padx=10)

    # Frame de operaciones
    ops_frame = ctk.CTkFrame(self)
    ops_frame.pack(pady=15)

    ctk.CTkLabel(ops_frame, text="Seleccione una operación:").pack(side="left", padx=5)

    self.operations = {
      "Cuasi Suma RGB": proc.cuasi_suma_rgb,
      "Cuasi Resta RGB": proc.cuasi_resta_rgb,
      "Cuasi Suma YIQ": proc.cuasi_suma_yiq,
      "Cuasi Resta YIQ": proc.cuasi_resta_yiq,
      "Producto": proc.producto,
      "Cociente": proc.cociente,
      "Resta Absoluta": proc.resta_absoluta,
      "If Darker": proc.if_darker,
      "If Lighter": proc.if_lighter,
    }

    self.selected_op = ctk.StringVar(value="Cuasi Suma RGB")
    self.dropdown = ctk.CTkOptionMenu(ops_frame, values=list(self.operations.keys()), variable=self.selected_op)
    self.dropdown.pack(side="left", padx=10)

    self.btn_apply = ctk.CTkButton(ops_frame, text="⚙️ Aplicar", command=self.apply_operation)
    self.btn_apply.pack(side="left", padx=10)

    # Frame de imágenes (3 columnas)
    img_frame = ctk.CTkFrame(self)
    img_frame.pack(pady=15, fill="both", expand=True)

    img_frame.columnconfigure(0, weight=1)
    img_frame.columnconfigure(1, weight=1)
    img_frame.columnconfigure(2, weight=1)

    self.lbl_img1 = ctk.CTkLabel(img_frame, text="Imagen 1 no cargada")
    self.lbl_img1.grid(row=0, column=0, padx=10, pady=10)

    self.lbl_img2 = ctk.CTkLabel(img_frame, text="Imagen 2 no cargada")
    self.lbl_img2.grid(row=0, column=1, padx=10, pady=10)

    self.lbl_result = ctk.CTkLabel(img_frame, text="Resultado")
    self.lbl_result.grid(row=0, column=2, padx=10, pady=10)

  def open_image1(self):
    file_path = select_image_file()
    if file_path:
      self.img1 = Image.open(file_path).convert("RGB")
      self.show_images()

  def open_image2(self):
    file_path = select_image_file()
    if file_path:
      self.img2 = Image.open(file_path).convert("RGB")
      self.show_images()

  def show_images(self):
    if self.img1:
      self.tk_img1 = prepare_for_canvas(self.img1)
      self.lbl_img1.configure(image=self.tk_img1, text="")

    if self.img2:
      self.tk_img2 = prepare_for_canvas(self.img2)
      self.lbl_img2.configure(image=self.tk_img2, text="")

    if self.processed_image:
      self.tk_processed = prepare_for_canvas(self.processed_image)
      self.lbl_result.configure(image=self.tk_processed, text="")

  def apply_operation(self):
    if self.img1 and self.img2:
      op_name = self.selected_op.get()
      func = self.operations[op_name]
      self.processed_image = func(self.img1, self.img2)
      self.show_images()
      self.btn_save.configure(state="normal")
    else:
      messagebox.showerror("Error", "Debe cargar dos imágenes primero.")

  def save_image(self):
    if self.processed_image:
      file_path = select_save_path()
      if file_path:
        self.processed_image.save(file_path)
        messagebox.showinfo("Éxito", "Imagen guardada correctamente.")
    else:
      messagebox.showerror("Error", "No hay imagen procesada para guardar.")
