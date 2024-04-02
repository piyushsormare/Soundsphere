import os
import pygame
from tkinter import Tk, Label
from PIL import Image, ImageTk

# Initialize Pygame for music
pygame.mixer.init()

# Music and wallpaper directory (organized by mood)
mood_directories = {
    'happy': {'music': 'path/to/happy/music', 'wallpaper': 'path/to/happy/wallpapers'},
    'sad': {'music': 'path/to/sad/music', 'wallpaper': 'path/to/sad/wallpapers'},
    # Add more moods as needed
}

def play_music(mood):
    """Play music for the given mood."""
    music_path = mood_directories[mood]['music']
    for song in os.listdir(music_path):
        # Only play the first file found for demo purposes
        pygame.mixer.music.load(os.path.join(music_path, song))
        pygame.mixer.music.play()
        break

def display_wallpaper(mood):
    """Display a wallpaper for the given mood."""
    wallpaper_path = mood_directories[mood]['wallpaper']
    for wallpaper in os.listdir(wallpaper_path):
        # Only display the first file found for demo purposes
        root = Tk()
        img = Image.open(os.path.join(wallpaper_path, wallpaper))
        img = img.resize((800, 600), Image.ANTIALIAS)  # Resize to fit the window
        imgTk = ImageTk.PhotoImage(img)
        Label(root, image=imgTk).pack()
        root.mainloop()
        break

def main():
    mood = input("Enter your mood (happy, sad, etc.): ")
    if mood in mood_directories:
        play_music(mood)
        display_wallpaper(mood)
    else:
        print("Mood not recognized. Please try again.")

if __name__ == "__main__":
    main()
