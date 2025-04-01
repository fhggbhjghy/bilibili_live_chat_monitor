from customtkinter import CTk, CTkCanvas, CTkEntry, CTkImage, CTkFrame, CTkTextbox, CTkButton, StringVar
from utility import get_window_scaling, round_rectangle, load_settings

class Gui():
    def __init__(self):

        self.message_entries = {}

        self.window = CTk()
        self.window.title('Danmu Monitor')
        self.window.after(0, lambda:self.window.state('zoomed'))
        self.window.configure(fg_color = '#BCA1F9')
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        self.window.minsize(width=1280,height=720)
        
        self.background = CTkFrame(
            self.window,
            corner_radius=25,
            fg_color='#F3ECFF'
        )
        self.background.grid(
            row=0,
            column=0,
            padx=(70,20),
            pady=(80,10),
            sticky='nsew'
        )
        
        self.background.grid_rowconfigure(0, weight=1)
        self.background.grid_columnconfigure(0, weight=1)
        self.background.grid_columnconfigure(1, weight=1)
        self.background.grid_columnconfigure(2, weight=1)

        self.content_blocks = []
        self.message_blocks = []
        for i in range(3):
            self.content_blocks.append(
                CTkFrame(
                    self.background,
                    corner_radius=25,
                    fg_color='#F7EDFF',
                    border_color='#D0BCFE',
                    border_width=1
                )
            )
            self.content_blocks[i].grid(
                row=0,
                column=i,
                padx=abs(20-i*20),
                pady=20,
                sticky=('nsew')
            )
            self.content_blocks[i].grid_columnconfigure(0, weight=1)
            for j in range(12):
                padding = (5,5)
                if j == 0:
                    padding = (10,5)
                if j == 11:
                    padding = (5,10)
                self.content_blocks[i].grid_rowconfigure(j, weight=1)
                self.message_blocks.append(
                    CTkButton(
                        self.content_blocks[i],
                        corner_radius=25,
                        text=' ',
                        fg_color='#ECD6FF',
                        hover_color='#908C9A',
                        text_color='#000000',
                        anchor='center'
                    )
                )
                self.message_blocks[i*12+j].grid(
                    row=j,
                    column=0,
                    padx=10,
                    pady=padding,
                    sticky=('nsew')
                )
                button: CTkButton = self.message_blocks[i*12+j]

    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    gui = Gui()
    gui.run()