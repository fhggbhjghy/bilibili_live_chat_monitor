from customtkinter import CTkFrame

class MessageContainer():
    def __init__(self, parent, index):
        self.parent = parent
        self.index = index

        self.frame = CTkFrame(
            parent,
            corner_radius=25,
            fg_color='#F7EDFF',
            border_color='#D0BCFE',
            border_width=1
        )

        self.frame.pack(
            side = 'left',
            expand = True,
            fill = 'both',
            padx = abs(20-index*20),
            pady = 20
        )