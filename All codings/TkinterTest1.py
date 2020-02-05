import tkinter as tk
from tkinter import filedialog
import os

try:
    root = tk.Tk()
    apps = []

    if os.path.isfile('logs.txt'):
        with open('logs.txt', 'r') as f:
            tempImages = f.read()
            tempImages = tempImages.split(',')
            apps = [x for x in tempImages if x.strip()]


    def addApp():
        for widget in frame.winfo_children():
            widget.destroy()

        filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                              filetypes=(("Image Files", "*.png *.jpg *gif"), ("allfiles", "*.*")))

        apps.append(filename)
        print(filename)
        for app in apps:
            label = tk.Label(frame, text=app, bg="green")
            label.pack()


    def runApps():
        for app in apps:
            os.startfile(app)


    canvas = tk.Canvas(root, height=400, width=400, bg="#263D42")
    canvas.pack()

    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    openFile = tk.Button(root, text="Import Photos", padx=10, pady=5, fg='white', bg="#263D42", command=addApp)
    openFile.pack()

    openApp = tk.Button(root, text="View Image", padx=10, pady=5, fg='white', bg="#263D42", command=runApps)
    openApp.pack()

    for app in apps:
        label = tk.Label(frame, text=app)
        label.pack()

    root.mainloop()

    with open('logs.txt', 'w') as f:
        for app in apps:
            f.write(app + ',')

except Exception as e:
    print(e)
