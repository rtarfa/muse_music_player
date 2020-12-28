import tkinter as tk
from PIL import Image, ImageTk
#import simpleaudio as sa
from audioplayer import AudioPlayer
from song import song
from playlist import playlist


#when enter a song, looks up on youtube and downloads it using youtube downloader, adds it to your play;ost
#make a list object for songs/playlist; list option can be to play a specofoc song in list, add, or remove

#wave_obj = sa.WaveObject.from_wave_file("better.wav")
#play_obj = wave_obj.play()

curr_song=AudioPlayer("better.wav")

# def pause_music():
#     curr_song.pause()
# def play_music():
#     curr_song.play()
    #def pause_music():
        #play_obj.stop()

    #if play_obj.is_playing():
    # pause = tk.Button(text="II", command=pause_music())
    # pause.place(x=136,y=257)
    # pause.bind("<Button-1>",pause_music())

    #else:

    # play_obj.wait_done()

#tk._test()
window= tk.Tk()
frame = tk.Frame(master=window, width=300, height=300)

image= Image.open("better.jpg")
photo= ImageTk.PhotoImage(image)

cover= tk.Label(image=photo)
cover.image=photo
cover.place(x=47,y=30)

title= tk.Label(text= "Better - Khalid")
title.place(x=100, y=232)
 #foreground="white",background="black"


forward= tk.Button(text=">>")
forward.place(x=190,y=257)
backward= tk.Button(text="<<")
backward.place(x=75,y=257)
#pause= tk.Button(text="II")


play= tk.Button(text=">", command=curr_song.play())
play.place(x=136,y=257)
#
# play.bind("<Button-1>",curr_song.play())

# if event.type==

#items=[frame,title,artist,forward,backward,play]

frame.pack() #sizes window as small as possible

window.mainloop()

#make a queue for music (to go back, front)
#make each song an object w an image, title, etc