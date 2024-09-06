import ctypes
import os

def change_wallpaper(path):
    abs_path = os.path.abspath(path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, abs_path, 3)

imageSelector = int(input("What wallpaper do you want to use? (1,2,3,4) "))
if imageSelector == 1:
    change_wallpaper("C:\\Users\\23liot\\Desktop\\ZeroTwoVirus\\WallPaper\\ZeroTwoCircle.jpg")
elif imageSelector == 2:
    change_wallpaper("C:\\Users\\23liot\\Desktop\\ZeroTwoVirus\\WallPaper\\ZeroTwo1.png")
elif imageSelector == 3:
    change_wallpaper("C:\\Users\\23liot\\Desktop\\ZeroTwoVirus\\WallPaper\\ZeroTwo2.jpg")
elif imageSelector == 4:
    change_wallpaper("C:\\Users\\23liot\\Desktop\\ZeroTwoVirus\\WallPaper\\ZeroTwo3.jpeg")
