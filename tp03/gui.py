import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
from utils.file_utils import select_image_file, select_save_path
from utils.image_utils import prepare_for_canvas
import tp03.processing as proc


class ImageApp(ctk.CTk):
  def __init__(self):
    super().__init__()
    self.title("TP03 - Operaciones de luminancia")
    self.geometry("950x700")
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    self.img = None
    self.processed_image = None
    self.tk_img = None
    self.tk_processed = None

    # Frame superior
    control_frame = ctk.CTkFrame(self)
    control_frame.pack(pady=10)

    self.btn_open = ctk.CTkButton(control_frame, text="📂 Abrir Imagen", command=self.open_image)
    self.btn_open.pack(side="left", padx=10)

    self.btn_save = ctk.CTkButton(control_frame, text="💾 Guardar Resultado", command=self.save_image, state="disabled")
    self.btn_save.pack(side="left", padx=10)

    # Menú de filtros
    ops_frame = ctk.CTkFrame(self)
    ops_frame.pack(pady=10)

    ctk.CTkLabel(ops_frame, text="Filtro:").pack(side="left", padx=5)

    self.operations = {
      "Raíz (sqrt)": proc.filtro_raiz,
      "Cuadrado (Y^2)": proc.filtro_cuadrado,
      "Lineal a trozos": proc.filtro_lineal_trozos,
    }

    self.selected_op = ctk.StringVar(value="Raíz (sqrt)")
    self.dropdown = ctk.CTkOptionMenu(ops_frame, values=list(self.operations.keys()), variable=self.selected_op)
    self.dropdown.pack(side="left", padx=10)

    self.btn_apply = ctk.CTkButton(ops_frame, text="⚙️ Aplicar", command=self.apply_operation)
    self.btn_apply.pack(side="left", padx=10)

    # Frame imágenes
    img_frame = ctk.CTkFrame(self)
    img_frame.pack(pady=10, fill="both", expand=True)

    img_frame.columnconfigure(0, weight=1)
    img_frame.columnconfigure(1, weight=1)

    self.lbl_original = ctk.CTkLabel(img_frame, text="Original")
    self.lbl_original.grid(row=0, column=0, padx=10, pady=10)

    self.lbl_result = ctk.CTkLabel(img_frame, text="Procesada")
    self.lbl_result.grid(row=0, column=1, padx=10, pady=10)

  def open_image(self):
    file_path = select_image_file()
    if file_path:
      self.img = Image.open(file_path).convert("RGB")
      self.show_images()

  def show_images(self):
    if self.img:
      self.tk_img = prepare_for_canvas(self.img)
      self.lbl_original.configure(image=self.tk_img, text="")

    if self.processed_image:
      self.tk_processed = prepare_for_canvas(self.processed_image)
      self.lbl_result.configure(image=self.tk_processed, text="")

  def apply_operation(self):
    if self.img:
      op_name = self.selected_op.get()
      func = self.operations[op_name]
      self.processed_image = func(self.img)
      self.show_images()
      self.btn_save.configure(state="normal")
    else:
      messagebox.showerror("Error", "Debe cargar una imagen primero.")

  def save_image(self):
    if self.processed_image:
      file_path = select_save_path()
      if file_path:
        self.processed_image.save(file_path)
        messagebox.showinfo("Éxito", "Imagen guardada correctamente.")
