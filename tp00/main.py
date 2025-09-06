import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


class ImageApp(ctk.CTk):
  def __init__(self):
    super().__init__()

    # Configuración de ventana
    self.title("Reductor de Resolución de Imágenes")
    self.geometry("900x650")
    ctk.set_appearance_mode("dark")      # "light" o "dark"
    ctk.set_default_color_theme("blue")  # otros: "green", "dark-blue"

    # Variables para imágenes
    self.original_image = None
    self.processed_image = None
    self.tk_image = None

    # Tamaño máximo para mostrar en el canvas
    self.canvas_width = 800
    self.canvas_height = 500

    # Frame de botones
    btn_frame = ctk.CTkFrame(self)
    btn_frame.pack(pady=15)

    self.btn_open = ctk.CTkButton(btn_frame, text="📂 Abrir Imagen", command=self.open_image)
    self.btn_open.pack(side="left", padx=10)

    self.btn_process = ctk.CTkButton(btn_frame, text="⚙️ Reducir Resolución", command=self.process_image, state="disabled")
    self.btn_process.pack(side="left", padx=10)

    self.btn_save = ctk.CTkButton(btn_frame, text="💾 Guardar Imagen", command=self.save_image, state="disabled")
    self.btn_save.pack(side="left", padx=10)

    # Canvas para mostrar imágenes
    self.canvas = ctk.CTkCanvas(self, width=self.canvas_width, height=self.canvas_height, bg="gray20", highlightthickness=0)
    self.canvas.pack(pady=10)

  def open_image(self):
    file_path = filedialog.askopenfilename(
      filetypes=[("Archivos de imagen", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )
    if file_path:
      self.original_image = Image.open(file_path).convert("RGB")
      self.processed_image = self.original_image.copy()
      self.show_image(self.processed_image)
      self.btn_process.configure(state="normal")
      self.btn_save.configure(state="normal")

  def show_image(self, img):
    # Redimensionar solo para mostrar en el canvas, no afecta la imagen real
    img_copy = img.copy()
    img_copy.thumbnail((self.canvas_width, self.canvas_height), Image.Resampling.LANCZOS)
    self.tk_image = ImageTk.PhotoImage(img_copy)
    self.canvas.delete("all")
    self.canvas.create_image(self.canvas_width//2, self.canvas_height//2, image=self.tk_image, anchor="center")

  def process_image(self):
    if self.processed_image:
      width, height = self.processed_image.size
      # Reducimos la resolución a la mitad de la original
      new_size = (max(1, width // 2), max(1, height // 2))
      self.processed_image = self.processed_image.resize(new_size, Image.Resampling.LANCZOS)
      self.show_image(self.processed_image)
      messagebox.showinfo("Procesado", f"Resolución reducida a {new_size[0]}x{new_size[1]}")
    else:
      messagebox.showerror("Error", "Primero abre una imagen.")

  def save_image(self):
    if self.processed_image:
      file_path = filedialog.asksaveasfilename(
        defaultextension=".jpg",
        filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("BMP", "*.bmp")]
      )
      if file_path:
        # Guardar JPEG con calidad 85% para reducir peso
        if file_path.lower().endswith((".jpg", ".jpeg")):
          self.processed_image.save(file_path, format="JPEG", quality=85, optimize=True)
        else:
          self.processed_image.save(file_path)
        messagebox.showinfo("Éxito", "Imagen guardada correctamente.")
    else:
      messagebox.showerror("Error", "No hay imagen para guardar.")


if __name__ == "__main__":
  app = ImageApp()
  app.mainloop()
