import tkinter as tk
from PIL import Image, ImageTk
import simpleaudio as sa


def play_music(event):
    wave_obj = sa.WaveObject.from_wave_file("better.wav")
    play_obj = wave_obj.play()

    def pause_music(event):
        play_obj.stop()

    if play_obj.is_playing():
        pause = tk.Button(text="II", command=pause_music())
        pause.place(x=136,y=257)
        pause.bind("<Button-1>",pause_music)
    # play_obj.wait_done()

#tk._test()
window= tk.Tk()
frame = tk.Frame(master=window, width=300, height=300)

image= Image.open("better.jpg")
photo= ImageTk.PhotoImage(image)

cover=tk.Label(image=photo)
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


play= tk.Button(text=">", command=play_music)
play.place(x=136,y=257)

play.bind("<Button-1>",play_music)

# if event.type==

#items=[frame,title,artist,forward,backward,play]

frame.pack() #sizes window as small as possible



window.mainloop()

#make a queue for music (to go back, front)
#make each song an object w an image, title, etc