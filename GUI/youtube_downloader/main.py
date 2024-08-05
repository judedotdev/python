import tkinter
import customtkinter as ctk
import yt_dlp
import threading
from PIL import Image, ImageTk

def progress_hook(d):
    if d['status'] == 'downloading':
        downloaded = d['downloaded_bytes']
        total = d['total_bytes']
        percentage = downloaded / total
        progress_var.set(percentage)
        progress_label.configure(text=f"Downloading: {int(percentage * 100)}%")
    elif d['status'] == 'finished':
        progress_var.set(1)
        progress_label.configure(text="Downloading: 100%")
        status_label.configure(text="Download Complete!")

def startDownload():
    try:
        ytLink = link.get()
        ydl_opts = {
            'format': 'best',
            'progress_hooks': [progress_hook],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([ytLink])
    except Exception as e:
        status_label.configure(text=f"Error: {str(e)}")
        print(f"Error details: {str(e)}")

def startDownloadThread():
    status_label.configure(text="Downloading...")
    progress_var.set(0)
    progress_label.configure(text="Downloading: 0%")
    thread = threading.Thread(target=startDownload)
    thread.start()

# System Settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# App Frame
app = ctk.CTk()
app.geometry("720x600")
app.title("YouTube Video Downloader")

# UI Elements
title = ctk.CTkLabel(app, text="Insert a YouTube Link")
title.pack(padx=10, pady=5)

# Link Input
url_var = tkinter.StringVar()
link =  ctk.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack(padx=10, pady=10)

# Progress Label
progress_label = ctk.CTkLabel(app, text="Downloading 0%")
progress_label.pack(padx=10, pady=10)

# Progress Bar
progress_var = tkinter.DoubleVar()
progress_bar = ctk.CTkProgressBar(app, variable=progress_var, width=450, height=20)
progress_bar.pack(padx=10)

# Download Button
custom_font = ctk.CTkFont(weight="bold")
download = ctk.CTkButton(app, text="Download", font=custom_font, command=startDownloadThread)
download.pack(padx=20, pady=15)

# Status label
status_label = ctk.CTkLabel(app, text="")
status_label.pack(padx=10)

# Load and display logo
logo_img = Image.open("logo.png")
logo_img = logo_img.resize((320, 320), Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_img)

# Create a Label to display the image
logo_label = tkinter.Label(app, image=logo_photo, bg=None)
logo_label.pack(pady=20)

# Run App
app.mainloop()
