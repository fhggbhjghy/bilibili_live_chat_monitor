from customtkinter import CTk, CTkCanvas, CTkEntry, CTkImage
from utility import get_window_scaling, round_rectangle

class Gui():
    def __init__(self):
        self.window = CTk()
        self.window.after(0, lambda:self.window.state('zoomed'))
        self.w = self.window.winfo_screenwidth()
        self.h = self.window.winfo_screenheight()
        self.window.geometry(f'{self.w}x{self.h}')
        print(f'{self.w}x{self.h}')
        self.window.configure(fg_color = '#D0BCFE')

        scaling = get_window_scaling()

        self.message_entries = {}

        self.canvas = CTkCanvas(
            self.window,
            bg = "#BCA1F9",
            height = self.h*scaling,
            width = self.w*scaling,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)

        self.content_background = round_rectangle(self.canvas,80,60,(80+1410)*scaling,(60+760)*scaling,100,fill="#F3ECFF",outline="")

        
    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    gui = Gui()
    gui.run()