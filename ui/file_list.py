import os
import customtkinter as ctk


class FileList(ctk.CTkTextbox):

    def __init__(self, master, open_callback):

        super().__init__(master)

        self.files = []
        self.open_callback = open_callback

        self.bind("<Double-Button-1>", self.open_file)

    def show_files(self, files):

        self.files = files

        self.delete("1.0", "end")

        for f in files:

            name = os.path.basename(f)

            self.insert("end", name + "\n")

    def open_file(self, event):

        line = int(self.index("insert").split(".")[0]) - 1

        if line < len(self.files):

            self.open_callback(self.files[line])