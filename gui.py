import tkinter as tk
from tkinter import filedialog, Text
import os


root = tk.Tk()
apps = []

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir="/", title="Select Files", 
                                            filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root, height=400, width=400, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.7, relheight=0.7, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=5, pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack() 

runApps = tk.Button(root, text="Run Apps", padx=5, pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack() 

root.mainloop()