from tkinter import Image
import PIL
import sys
try:
    img = Image.open("foto.png")
except:
    print("cagaste")
img.show()