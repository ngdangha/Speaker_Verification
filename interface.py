from tkinter import *
import tkinter
from tkinter.ttk import *
from PIL import ImageTk, Image
window = Tk()
window.geometry("987x565")
window.title("Voice Verification")
image1 = Image.open("D:\XLTN\image2.png")
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=0, y=0)
#text.tag_add("here", "1.0", "1.4")
# recordBtn = Button(window, text = 'Record')
# recordBtn.place(relx=0.5, rely=0.8, anchor=CENTER)

# Create a photoimage object of the image in the path
photo = PhotoImage(file = "D:/XLTN/record.png")
photoimage = photo.subsample(1, 1)
Button(window, image = photoimage,).pack(side = BOTTOM, pady = 70)
mainloop()
# window.mainloop()