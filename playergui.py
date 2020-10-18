#!/bin/python3

import os
import random
import pygame_sdl2 as pygame
import multiprocessing
import tkinter as tk
from tkinter import *

pygame.mixer.init()

directory = os.environ['HOME'] + '/Music'
os.chdir(directory)
playlist = os.listdir() 

choice = 1
app = Tk()
icon = PhotoImage(file='Your file')
app.tk.call('wm', 'iconphoto', app._w, icon)
app.title("Player")
app.geometry('800x600')
scrollbar = Scrollbar(app)
scrollbar.pack(side = RIGHT, fill = Y)
filename = Listbox(app, highlightcolor = "black", fg = "white", bd = '20px', height = '20', width = '40', yscrollcommand = scrollbar.set, selectmode = SINGLE)
filename.pack()

for i in range(0):
	filename.insert(END, str(i))
filename.pack(side = LEFT, fill = BOTH)
scrollbar.config(command = filename.yview)

for music_file in playlist:
	position = 0
	filename.insert(position, music_file)
	position = position + 1

def play_music():
    pygame.mixer.music.load(filename.get(ACTIVE))
    var.set(filename.get(ACTIVE))
    pygame.mixer.music.play()	
playbutton = Button(app, text="Play ", command=play_music)
playbutton.pack(fill="x")

var = StringVar()
musictitle = Label(app, textvariable=var)
musictitle.pack() 

def pause_music():
	pygame.mixer.music.pause()
playbutton = Button(app, text="Stop ", command=pause_music)
playbutton.pack(fill="x")

def unpause_music():
	pygame.mixer.music.unpause()
playbutton = Button(app, text="Resume ", command=unpause_music)
playbutton.pack(fill="x")

def mute_music():
	pygame.mixer.music.set_volume(0.0)
playbutton = Button(app, text="Mute ", command=mute_music)
playbutton.pack(fill="x")

def unmute_music():
	pygame.mixer.music.set_volume(1.0)
playbutton = Button(app, text="Unmute ", command=unmute_music)
playbutton.pack(fill="x")

def random_music():
    filename = random.choice(playlist)
    pygame.mixer.music.load(filename)
    var.set(filename)
    pygame.mixer.music.play()
playbutton = Button(app, text="Play random music ", command=random_music)
playbutton.pack(fill="x")

"""
Currently, autoplay is not working
def autoplay_music(): 
    autoplay = False
    m = multiprocessing.Process(target=playlist, args=(choice,))
    m.start()
    if autoplay == True and pygame.mixer.music.get_busy() == 0:
        filename = random.choice(playlist)
        pygame.mixer.music.load(filename)
        var.set(filename)
        pygame.mixer.music.play()
        autoplay = not autoplay
playbutton = Button(app, text="Autoplay on", command=autoplay_music)
playbutton.pack(fill="x")

def autoplay_off_music():
    autoplay = not autoplay
    if autoplay == False and pygame.mixer.music.get_busy() == 0:
        pygame.mixer.music.pause()
playbutton = Button(app, text="Autoplay off", command=autoplay_off_music)
playbutton.pack(fill="x")
"""
app.mainloop()	
