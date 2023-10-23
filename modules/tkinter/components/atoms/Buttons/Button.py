from tkinter import CENTER
from customtkinter import CTkButton


class Button(CTkButton):
    def __init__(self,width:int, height:int, text:str, x_pos:float | int = 0.5, y_pos:float | int = 0.5, anchor=None):
        super().__init__(self)
        self.button = CTkButton(self, width=width, height=height, text=text).place(
            relx=x_pos, rely=y_pos, anchor=CENTER
        )
