import tkinter as tk
import os

from model import verify
from configuration import get_config
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image

config = get_config()

window = tk.Tk()
window.geometry("987x565")
window.title("Voice Verification")

verifyRes = tk.Label(text = "")

def enrollVoice():
    os.system('python record.py --verify False')

def verifyVoice():
    os.system('python record.py')
    global verifyRes
    verifyRes.destroy()
    verifyRes = tk.Label(
        text=verify("./model"),
        foreground="white",  # Set the text color to white
        background="#000fee",  # Set the background color to black
        font = "Fixedsys 24"
    )
    verifyRes.pack(side = BOTTOM, pady = 95)

# Create background
backgroundImg = PhotoImage(file = "./images/background.png")

background = tk.Label(
    image=backgroundImg
    )
background.place(x = 0, y = 0)

# Create enroll voice button
enrollImg = PhotoImage(file = "./images/record.png")    # Create a photoimage object of the image in the path
enrollImg = enrollImg.subsample(1, 1)

enrollBtn = tk.Button(
    image = enrollImg,
    command = enrollVoice
    )
enrollBtn.place(x = 150, y = 375)

enrollText = tk.Label(
        text="Enroll",
        foreground="white",  # Set the text color to white
        background="#000fee",  # Set the background color to black
        font = "Fixedsys 24"
    )
enrollText.place(x = 183, y = 325)

# Create verify voice button
verifyImg = PhotoImage(file = "./images/verify.png")    # Create a photoimage object of the image in the path
verifyImg = verifyImg.subsample(1, 1)

verifyBtn = tk.Button(
    image = verifyImg,
    command = verifyVoice
    )
verifyBtn.place(x = 675, y = 375)

verifyText = tk.Label(
        text="Verify",
        foreground="white",  # Set the text color to white
        background="#000fee",  # Set the background color to black
        font = "Fixedsys 24"
    )
verifyText.place(x = 705, y = 325)

mainloop()
# window.mainloop()