import os
from tkinter import *

import pytube
from pytube import Playlist


def getLink():
    URL = entryBox.get()
    youtube = pytube.YouTube(URL)
    return youtube


def getPlaylist():
    URL2 = entryBoxRes.get()
    playlist = Playlist(URL2)
    return playlist


def mp4():
    youtube = getLink()
    videomp4 = youtube.streams.get_highest_resolution()
    print(videomp4)


def mp3():
    youtube = getLink()
    try:
        ses = youtube.streams.filter(only_audio=True, abr="160kbps").first()
    except:
        ses = youtube.streams.filter(only_audio=True).first()
    print(ses)
    downloadeFile = ses.download()
    base, ext = os.path.splitext(downloadeFile)
    newFile = base + ".mp3"
    os.rename(downloadeFile, newFile)


def palylistMp4():
    # playlist=getPlaylist()
    URL2 = entryBoxRes.get()
    print(URL2)
    playlist = Playlist(URL2)
    for video in playlist.videos:
        video.streams.get_highest_resolution().download()
        print("ok")


def paylistMp3():
    URL2 = entryBoxRes.get()
    playlist = Playlist(URL2)
    print(URL2)
    for video in playlist.videos:
        try:

            try:
                ses = video.streams.filter(only_audio=True, abr="160kbps").first()
            except:
                ses = video.streams.filter(only_audio=True).first()
            print(ses)
            downloadeFile = ses.download()
            base, ext = os.path.splitext(downloadeFile)
            newFile = base + ".mp3"
            os.rename(downloadeFile, newFile)
        except:
            print("Ses indirilemedi")


# ---------------------------------GUI----------------------------------
master = Tk()
master.title("Ceryunus")
kanvas = Canvas(master, bg="#3d3d3d", height=150, width=300)  # #212121
kanvas.pack()

entryBoxFrame = Frame(master, bg="#3d3d3d")
entryBoxFrame.place(relx=0.02, rely=0.01, relheight=0.25, relwidth=0.96)

mp4Frame = Frame(master, bg="#3d3d3d")
mp4Frame.place(relx=0.02, rely=0.3, relheight=0.25, relwidth=0.48)
mp3Frame = Frame(master, bg="#3d3d3d")
mp3Frame.place(relx=0.51, rely=0.3, relheight=0.25, relwidth=0.48)

lableFrame = Frame(master, bg="#3d3d3d")
lableFrame.place(relx=0.02, rely=0.60, relheight=0.25, relwidth=0.96)
# --------------------------------------------------------------------
entryBox = Entry(entryBoxFrame)
entryBox.place(relx=0.25, rely=0.5, anchor="center")
entryBox.insert(END, "Link")
entryBoxRes = Entry(entryBoxFrame)
entryBoxRes.place(relx=0.75, rely=0.5, anchor="center")
entryBoxRes.insert(END, "Playlist Download")

mp4Button = Button(mp4Frame, text="mp4", command=mp4)
mp4Button.place(relx=0.5, rely=0.5, anchor="center")
mp3Button = Button(mp3Frame, text="mp3", command=mp3)
mp3Button.place(relx=0.5, rely=0.5, anchor="center")

playlistButton1 = Button(lableFrame, text="Playlist Mp4", command=palylistMp4)
playlistButton1.place(relx=0.25, rely=0.5, anchor="center")

playlistButton2 = Button(lableFrame, text="Playlist Mp3", command=paylistMp3)
playlistButton2.place(relx=0.75, rely=0.5, anchor="center")

master.mainloop()
