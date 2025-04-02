from customtkinter import CTk, CTkCanvas, CTkEntry, CTkImage, CTkFrame, CTkTextbox, CTkButton, StringVar
from utility import get_window_scaling, round_rectangle, load_settings, justify_frame
from message import Message
from message_container import MessageContainer

class Gui():
    def __init__(self):

        self.message_entries = {}

        self.window = CTk()
        self.window.title('Danmu Monitor')
        self.window.after(0, lambda:self.window.state('zoomed'))
        self.window.configure(fg_color = '#BCA1F9')
        # self.window.minsize(width=1280,height=720)
        justify_frame(self.window, 0, 'both')
        
        self.background = CTkFrame(
            self.window,
            corner_radius=25,
            fg_color='#F3ECFF'
        )

        self.background.pack(
            side = "top",
            expand = True,
            fill = 'both',
            padx=(70,20),
            pady=(80,10),
        )
        
        justify_frame(self.background, 0, 'both')
        justify_frame(self.background, 1, 'width')
        justify_frame(self.background, 2, 'width')

        self.content_blocks = []
        self.message_blocks = []
        for i in range(3):
            self.content_blocks.append(
                MessageContainer(self.background, i)
            )
            for j in range(12):
                self.message_blocks.append(
                    Message(self.content_blocks[i], j)
                )

    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    gui = Gui()
    gui.run()