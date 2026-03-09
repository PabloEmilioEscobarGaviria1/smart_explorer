from PIL import Image
import customtkinter as ctk


class PreviewEngine:

    def __init__(self, frame):

        self.frame = frame
        self.label = ctk.CTkLabel(frame, text="")
        self.label.pack()

    def preview(self, path):

        try:

            if path.lower().endswith(("png", "jpg", "jpeg")):

                img = Image.open(path)
                img = img.resize((250, 250))

                photo = ctk.CTkImage(light_image=img, dark_image=img)

                self.label.configure(image=photo, text="")
                self.label.image = photo

            else:
                self.label.configure(text="Preview not available")

        except:
            self.label.configure(text="Preview error")