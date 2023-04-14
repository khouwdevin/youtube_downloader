from tkinter import filedialog
import os

from pytube import YouTube

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class MainPage(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.is_audio = ttk.IntVar()
        self.progress_text = ttk.StringVar()

        label = ttk.Label(text ="Insert video link", font = "TimesNewRoman 18 bold")
        label.pack(pady = 10)

        self.link_input = ttk.Entry(textvariable = ttk.StringVar(), width = 80)
        self.link_input.pack()

        self.checkbutton = ttk.Checkbutton(bootstyle = "round-toggle", variable = self.is_audio, text = "Save only audio")
        self.checkbutton.pack(pady = 10)

        self.button = ttk.Button(text = "Download", command = lambda:self.download_video(self.link_input.get()), bootstyle=(INFO, OUTLINE))
        self.button.pack(pady = 10)

        self.label_progress = ttk.Label(textvariable = self.progress_text, font = "TimesNewRoman 12")
        self.label_progress.pack()

    def download_video(self, link):
        try:
            if (len(link) > 0):
                self.button.configure(state = "disabled", text = "Downloading...")
                self.progress_text.set("Loading...")

                youtube_object = YouTube(link)

                file_type = ["Audio", "*.mp3"] if self.is_audio.get() == 1 else ["Video", "*.mp4"]

                selected_path = os.path.split(filedialog.asksaveasfilename(initialdir = "/", title = "Select folder", confirmoverwrite = True, filetypes = [(file_type[0], file_type[1])], initialfile = youtube_object.title))
                
                if (len(selected_path[0]) > 0):
                    # youtube_object.register_on_progress_callback(self.progress_bar)

                    if (self.is_audio.get() == 1):
                        output = youtube_object.streams.get_audio_only().download(output_path = selected_path[0], filename = selected_path[1] + ".mp3")
                    else:
                        output = youtube_object.streams.get_highest_resolution().download(output_path = selected_path[0], filename = selected_path[1] + ".mp4")
                    
                    self.progress_text.set(f"Success file save to {output}")
                    self.after(5000, lambda:self.progress_text.set(""))
        except:
            self.progress_text.set("An error has occurred")
            self.after(5000, lambda:self.progress_text.set(""))

        self.button.configure(state = "enabled", text = "Download")
        self.is_audio.set(0)
        self.link_input.delete(0, END)

    # def progress_bar(self, stream, chunk, bytes_remaining):
    #     total_size = stream.filesize
    #     bytes_downloaded = total_size - bytes_remaining 
    #     percentage_of_completion = bytes_downloaded / total_size * 100
    #     self.progress_text.set(percentage_of_completion)
    
