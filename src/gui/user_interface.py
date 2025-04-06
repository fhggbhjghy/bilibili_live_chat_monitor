from customtkinter import CTk, CTkFrame
from gui.message import Message
from gui.message_container import MessageContainer

class Gui():
    def __init__(self, ban):

        self.message_entries = {}

        self.window = CTk()
        self.window.title('Danmu Monitor')
        self.window.after(0, lambda:self.window.state('zoomed'))
        self.window.configure(fg_color = '#BCA1F9')
        self.window.minsize(width=1280,height=720)
        
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

        self.content_blocks = []
        self.message_blocks = []
        for i in range(3):
            self.content_blocks.append(
                MessageContainer(self.background, i)
            )
            for j in range(12):
                self.message_blocks.append(
                    Message(self.content_blocks[i], j, ban)
                )

    def update(self, id, content):
        message_block: Message = self.message_blocks[id%36]
        message_block.update(content)


    def run(self):
        self.window.mainloop()

def ban(content):
    print(f'banned {content}')
    return True

# if __name__ == '__main__':
#     gui = Gui(ban)
#     gui.run()
