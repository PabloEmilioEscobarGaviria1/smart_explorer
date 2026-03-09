import customtkinter as ctk


class Toolbar(ctk.CTkFrame):

    def __init__(self, master, callbacks):

        super().__init__(master)

        back = ctk.CTkButton(self, text="⬅", width=40,
                             command=callbacks["back"])
        back.pack(side="left", padx=5)

        refresh = ctk.CTkButton(self, text="⟳", width=40,
                                command=callbacks["refresh"])
        refresh.pack(side="left", padx=5)

        home = ctk.CTkButton(self, text="🏠", width=40,
                             command=callbacks["home"])
        home.pack(side="left", padx=5)

        self.path = ctk.CTkEntry(self)
        self.path.pack(side="left", fill="x", expand=True, padx=5)

        self.search = ctk.CTkEntry(self, placeholder_text="AI поиск")
        self.search.pack(side="right", padx=5)