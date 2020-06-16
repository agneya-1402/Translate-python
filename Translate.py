import tkinter as tk
from googletrans import Translator

win=tk.Tk()
win.title("Translator")
win.geometry("200x70")

def translation():
    word=entry.get()
    translator=Translator(service_urls=["translate.google.com"])
    translation1=translator.translate(word,dest="ru")
    label1=tk.Label(win,text=f"Translated into Russian :{translation1.text}",bg="yellow")
    label1.grid(row=2,column=0)

label=tk.Label(win,text="Enter word :")
label.grid(row=0,column=0,sticky="W")

entry=tk.Entry(win)
entry.grid(row=1,column=0)

button=tk.Button(win,text="Translate",command=translation,activebackground="green",bg="red",fg="white")
button.grid(row=1,column=2)

win.mainloop()