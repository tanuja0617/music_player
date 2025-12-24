import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title("MUSIC PLAYER")
canvas.geometry("600x800")
canvas.config(bg='black')

rootpath= "C:\Users\hosur\python p\music player\Music"
pattern="*.mp3"

mixer.init()

def select():
    label.config(text = listBox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listBox.select_clear('active')

def play_next():
    next_song = listBox.curselection()
    next_song= next_song[0]+1
    next_song_name = listBox.get(next_song)
    
    label.config(text = next_song_name)
    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def play_prev():
    next_song = listBox.curselection()
    next_song = next_song[0]-1
    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

photo_a = tk.PhotoImage(file = r"C:\Users\hosur\python p\music player\play_img.png")
photoimage = photo_a.subsample(3, 3)
photo_b = tk.PhotoImage(file = r"C:\Users\hosur\python p\music player\next_img.png")
photoimage = photo_b.subsample(3, 3)
photo_c = tk.PhotoImage(file = r"C:\Users\hosur\python p\music player\prev_img.png")
photoimage = photo_c.subsample(3, 3)
photo_d = tk.PhotoImage(file = r"C:\Users\hosur\python p\music player\stop_img.png")
photoimage = photo_d.subsample(3, 3)


listBox= tk.Listbox(canvas, fg= "cyan", bg= "black", width=100)
listBox.pack(padx = 15, pady = 15)

label = tk.Label(canvas, text ='listBox', bg = 'black', fg = 'yellow')
label.pack(pady = 15)

top = tk.Frame(canvas, bg = "black")
top.pack(padx = 10,pady = 5, anchor = 'center')  

prevButton = tk.Button(canvas, text = "prev", bg = 'black', image = photo_c, borderwidth = 0, command = play_prev)
prevButton.pack(pady = 15, in_ = top, side = 'left')

playButton = tk.Button(canvas, text = "play", bg = 'black', image = photo_a, borderwidth = 0, command = select)
playButton.pack(pady = 15, in_ = top, side = 'left')

stopButton = tk.Button(canvas, text = "stop", bg = 'black', image = photo_d, borderwidth = 0,command = stop )
stopButton.pack(pady = 15, in_ = top, side = 'left' )

nextButton = tk.Button(canvas, text = "next", bg = 'black', image = photo_b, borderwidth = 0, command = play_next)
nextButton.pack(pady = 15, in_ = top, side = 'left')

for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        listBox.insert('end', filename)


canvas.mainloop()
