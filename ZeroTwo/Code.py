import ctypes
import os
import time

def change_wallpaper(path):
    abs_path = os.path.abspath(path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, abs_path, 3)

while True:
    change_wallpaper("C:\\Users\\23liot\\Desktop\\ZeroTwo\\WallPaper\\ZeroTwoCircle.jpg")
    time.sleep(0.002)
    change_wallpaper("C:\\Users\\23liot\\Desktop\\ZeroTwo\\WallPaper\\ZeroTwo1.png")
    time.sleep(0.002)
    change_wallpaper("C:\\Users\\23liot\\Desktop\\ZeroTwo\\WallPaper\\ZeroTwo2.jpg")
    time.sleep(0.002)
    change_wallpaper("C:\\Users\\23liot\\Desktop\\ZeroTwo\\WallPaper\\ZeroTwo3.jpeg")
    time.sleep(0.002)
    change_wallpaper("C:\\Users\\23liot\\Desktop\\ZeroTwo\\WallPaper\\ZeroTwo4.webp")
    time.sleep(0.002)
    change_wallpaper("C:\\Users\\23liot\\Desktop\\ZeroTwo\\WallPaper\\ZeroTwo5.jpg")
    time.sleep(0.002)    
    change_wallpaper("C:\\Users\\23liot\\Desktop\\ZeroTwo\\WallPaper\\ZeroTwo6.jpg")
    time.sleep(0.002)    
    change_wallpaper("C:\\Users\\23liot\\Desktop\\ZeroTwo\\WallPaper\\ZeroTwo7.jpg")
    time.sleep(0.002)    
