from tkinter import filedialog
import os

import threading

from pytube import YouTube
from pytube.exceptions import PytubeError

import ttkbootstrap as ttk
from ttkbootstrap.constants import INFO, OUTLINE

from utils.utils import replace_symbol

class MainPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.is_audio = ttk.IntVar()
        self.progress_text = ttk.StringVar()
        self.link_text = ttk.StringVar()

        self.controller: ttk.Window = controller

        self.link_text.trace("w", self.validation)

        ttk.Label(self,text ="Insert video link", font = "TimesNewRoman 18 bold").pack(pady = 10)

        ttk.Entry(self, textvariable = self.link_text, width = 80).pack()

        self.checkbutton = ttk.Checkbutton(self, bootstyle = "round-toggle", variable = self.is_audio, text = "Save only audio")
        self.checkbutton.pack(pady = 10)

        self.button = ttk.Button(self, text = "Download", bootstyle=(INFO, OUTLINE), command = lambda:threading.Thread(target = self.download_video).start(), state = "disabled")
        self.button.pack(pady = 10)

        self.label_progress = ttk.Label(self, textvariable = self.progress_text, font = "TimesNewRoman 12")
        self.label_progress.pack()

    def validation(self, *args):
        if (len(self.link_text.get()) > 0):
            self.button.configure(state = "enabled")
        else:
            self.button.configure(state = "disabled")

    def download_video(self):
        link = self.link_text.get()

        try:
            if (len(link) > 0):
                file_type = ["Audio", "*.mp3"] if self.is_audio.get() == 1 else ["Video", "*.mp4"]

                youtube_object = YouTube(link)

                title = replace_symbol(youtube_object.title)
                path_temp = filedialog.asksaveasfilename(title = "Choose directory", initialdir = ".", confirmoverwrite = True, defaultextension = "*.*", initialfile = title, filetypes = [(file_type[0], file_type[1])])
                selected_path = os.path.split(path_temp)
                
                if (len(selected_path[0]) > 0):
                    self.progress_text.set("Loading...")
                    self.button.configure(state = "disabled", text = "Downloading...")

                    self.controller.update()

                    if (self.is_audio.get() == 1):
                        output = youtube_object.streams.get_audio_only().download(output_path = selected_path[0], filename = selected_path[1] + ".mp3")
                    else:
                        output = youtube_object.streams.get_highest_resolution().download(output_path = selected_path[0], filename = selected_path[1] + ".mp4")
                    
                    self.progress_text.set(f"Success file save to {output}")
                    self.after(5000, lambda:self.progress_text.set(""))
        except PytubeError:
            self.progress_text.set("Connection error")
            self.after(5000, lambda:self.progress_text.set(""))
        except:
            self.progress_text.set("An error has occurred")
            self.after(5000, lambda:self.progress_text.set(""))

        self.button.configure(state = "enabled", text = "Download")
        self.is_audio.set(0)
        self.link_text.set("")
