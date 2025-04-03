from customtkinter import CTkButton

class Message():
    def __init__(self, parent, index, ban):
        self.parent = parent
        self.index = index
        self.bg_fill = ('#ECD6FF', '#FFE2EB', '#908C9A')
        self.bg_selector_index = 0
        self.content = {}
        self.ban = ban

        self.frame = CTkButton(
            parent.frame,
            command=self.onclick,
            corner_radius=25,
            text=' ',
            fg_color=self.bg_fill[self.bg_selector_index],
            hover_color='#908C9A',
            text_color='#000000',
            anchor='center'
        )

        self.bg_selector_index = (self.bg_selector_index+1)%2

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
    
    def update(self, content):
        self.content = content
        self.frame.configure(state="enabled")
        self.display()

    def get_message(self):
        return self.content['structured_message']

    def get_sender(self):
        return (self.content.get('sender_uid', -1), self.content.get('sender_name', 'John Doe'), self.content.get('sender_rank', 0))
    
    def onclick(self):
        # print(self.get_sender())
        if self.ban(self.get_sender()):
            self.frame.configure(fg_color = self.bg_fill[-1])
            self.frame.configure(state="disabled")

    def display(self):
        self.frame.configure(fg_color = self.bg_fill[self.bg_selector_index])
        self.bg_selector_index = (self.bg_selector_index+1)%2
        self.frame.configure(text = self.get_message()) 