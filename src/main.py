import ttkbootstrap as ttk
from pages.mainpage import MainPage

page_data = [MainPage]

class App(ttk.Window):
    def __init__(self):
        super().__init__(themename = "cyborg")
        self.title("Youtube Downloader")

        self.iconphoto(False, ttk.PhotoImage(file = r"./public/icon.png"))

        self.geometry("600x300")
        self.minsize(600, 300)

        self.place_window_center()

        MainPage(self)

        self.mainloop()

    def change_window(self, page):
        temp_page = self.pages[page]
        temp_page.tkraise()

if __name__ == "__main__":
    App()
