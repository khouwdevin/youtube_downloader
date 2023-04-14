import ttkbootstrap as ttk

class MainPage(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # label of frame Layout 2
        label = ttk.Label(text ="Insert video link")
        label.pack()

        link_input = ttk.Entry(textvariable = ttk.StringVar())
        link_input.pack()

        parent.change_window("Hello")
         
        # putting the grid in its place by using
        # grid
        # label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button1 = ttk.Button(self, text ="Page 1",
        # command = lambda : controller.show_frame(Page1))
     
        # # putting the button in its place by
        # # using grid
        # button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # ## button to show frame 2 with text layout2
        # button2 = ttk.Button(self, text ="Page 2",
        # command = lambda : controller.show_frame(Page2))
     
        # # putting the button in its place by
        # # using grid
        # button2.grid(row = 2, column = 1, padx = 10, pady = 10)
