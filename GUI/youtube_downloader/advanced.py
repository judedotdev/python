import tkinter
import customtkinter as ctk
import yt_dlp
import threading
import time
from googleapiclient.discovery import build

# YouTube Data API setup
YOUTUBE_API_KEY = "YOUR_API_KEY_HERE"
youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)


def get_video_metadata(video_id):
    request = youtube.videos().list(part="snippet,contentDetails", id=video_id)
    response = request.execute()
    if "items" in response and len(response["items"]) > 0:
        video = response["items"][0]
        title = video["snippet"]["title"]
        description = video["snippet"]["description"]
        return title, description
    return None, None


def progress_hook(d):
    if d["status"] == "downloading":
        downloaded = d["downloaded_bytes"]
        total = d["total_bytes"]
        percentage = downloaded / total
        progress_var.set(percentage)
        progress_label.configure(text=f"Downloading: {int(percentage * 100)}%")
    elif d["status"] == "finished":
        progress_var.set(1)
        progress_label.configure(text="Downloading: 100%")
        status_label.configure(text="Download Complete!")


def startDownload():
    try:
        ytLink = link.get()
        video_id = ytLink.split("v=")[-1]
        title, description = get_video_metadata(video_id)

        if title:
            status_label.configure(text=f"Downloading '{title}'...")

        ydl_opts = {
            "format": "best",
            "progress_hooks": [progress_hook],
            "headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
            },
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
link = ctk.CTkEntry(app, width=350, height=40, textvariable=url_var)
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
download = ctk.CTkButton(
    app, text="Download", font=custom_font, command=startDownloadThread
)
download.pack(padx=20, pady=15)

# Status label
status_label = ctk.CTkLabel(app, text="")
status_label.pack(padx=10, pady=(10, 30))  # Adds 40 pixels below

# Frame to contain all the text labels
text_frame = ctk.CTkFrame(app)
text_frame.pack(fill="both", padx=20, pady=5)  # Pack with uniform padding
# Define the bold font
bold_font = ctk.CTkFont(weight="bold")

# ABOUT Label
about_heading = ctk.CTkLabel(
    text_frame,
    text="ABOUT THIS APP:",
    justify="left",
    font=bold_font,
)
about_heading.pack(anchor="w", padx=10)  # Left-align inside the frame
about_body = ctk.CTkLabel(
    text_frame,
    text="This is a simple YouTube video downloader. "
    "\nYou can download videos by inserting the URL of a YouTube video and "
    "clicking the 'Download' button.",
    justify="left",
)
about_body.pack(anchor="w", padx=10, pady=10)  # Left-align inside the frame

# Steps Label
steps_heading = ctk.CTkLabel(
    text_frame,
    text="How to Use the App:",
    justify="left",
    font=bold_font,
)
steps_heading.pack(anchor="w", padx=10)  # Left-align inside the frame
steps_body = ctk.CTkLabel(
    text_frame,
    text="1. Copy the link of the YouTube video you want to download.\n"
    "2. Paste the link in the input field.\n"
    "3. Click the 'Download' button.\n"
    "4. Wait for the download to complete.",
    justify="left",
)
steps_body.pack(anchor="w", padx=10, pady=10)  # Left-align inside the frame

# File Info Label
file_info_head = ctk.CTkLabel(
    text_frame,
    text="Where is the file saved?",
    justify="left",
    font=bold_font,
)
file_info_head.pack(anchor="w", padx=10)  # Left-align inside the frame
file_info_body = ctk.CTkLabel(
    text_frame,
    text="The downloaded file will be saved in the current directory of this app.\n"
    "You can check this folder for the downloaded video file.",
    justify="left",
)
file_info_body.pack(anchor="w", padx=10, pady=10)  # Left-align inside the frame

# Run App
app.mainloop()
