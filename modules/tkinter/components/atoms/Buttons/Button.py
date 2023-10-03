import tkinter
from customtkinter import CTkButton


class Button(CTkButton):
    def __init__(self,width:int, height:int, text:str, x_pos:int, y_pos:int, anchor=None):
        super().__init__(self)
        self.button = CTkButton(self, width=width, height=height, text=text).place(
            relx=x_pos, rely=y_pos, anchor=tkinter.CENTER
        )
