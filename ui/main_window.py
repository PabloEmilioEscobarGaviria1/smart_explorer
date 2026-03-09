import os
import sys
import subprocess
from pathlib import Path

import customtkinter as ctk

from ui.toolbar import Toolbar
from ui.file_list import FileList

from core.file_manager import FileManager
from ai.semantic_search import SemanticSearch
from preview.preview_engine import PreviewEngine


class MainWindow(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.geometry("1100x700")
        self.title("Smart Explorer")

        self.file_manager = FileManager()
        self.search_engine = SemanticSearch()

        self.current_path = str(Path.home())

        self.build_ui()

        self.load_folder(self.current_path)

    def build_ui(self):

        callbacks = {
            "back": self.go_back,
            "refresh": self.refresh,
            "home": self.go_home
        }

        self.toolbar = Toolbar(self, callbacks)
        self.toolbar.pack(fill="x")

        body = ctk.CTkFrame(self)
        body.pack(fill="both", expand=True)

        self.file_list = FileList(body, self.open_file)
        self.file_list.pack(side="left", fill="both", expand=True)

        preview_frame = ctk.CTkFrame(body, width=300)
        preview_frame.pack(side="right", fill="y")

        self.preview = PreviewEngine(preview_frame)

        self.toolbar.search.bind("<Return>", self.search)

    def load_folder(self, path):

        self.current_path = path

        files = self.file_manager.list_files(path)

        self.file_list.show_files(files)

        self.search_engine.index_files(files)

        self.toolbar.path.delete(0, "end")
        self.toolbar.path.insert(0, path)

    def open_file(self, path):

        if os.path.isdir(path):

            self.load_folder(path)

        else:

            self.preview.preview(path)

            if sys.platform.startswith("win"):
                os.startfile(path)

            elif sys.platform.startswith("darwin"):
                subprocess.call(("open", path))

            else:
                subprocess.call(("xdg-open", path))

    def search(self, event=None):

        query = self.toolbar.search.get()

        results = self.search_engine.search(query)

        self.file_list.show_files(results)

    def go_home(self):

        self.load_folder(str(Path.home()))

    def go_back(self):

        parent = os.path.dirname(self.current_path)

        if parent:
            self.load_folder(parent)

    def refresh(self):

        self.load_folder(self.current_path)