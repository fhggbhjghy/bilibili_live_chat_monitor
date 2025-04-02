from customtkinter import CTkButton

class Message():
    def __init__(self, parent, index):
        self.parent = parent
        self.index = index

        self.frame = CTkButton(
            parent.frame,
            corner_radius=25,
            text=' ',
            fg_color='#ECD6FF',
            hover_color='#908C9A',
            text_color='#000000',
            anchor='center'
        )

        self.frame.pack(
            side = "top",
            expand = True,
            fill = 'both',
            padx = 10,
            pady = self.get_pady()
        )
    
    def get_pady(self):
        if self.index == 0:
            return (10,5)
        if self.index == 11:
            return (5,10)
        return (5,5)