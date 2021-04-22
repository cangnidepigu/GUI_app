import tkinter as tk
from tkinter import Widget, filedialog, Text
import os

# it is kind of like a body in HTML, u attach what to want to it
root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]


        
def addApp():
    # destroys everything before adding new one, it prevents from double records

    for widget in frame.winfo_children():
        widget.destroy()


    filename= filedialog.askopenfilename(initialdir="/", title="Select File", 
    filetypes=(("executables", "*exe"), ("all files", "*.*")))

    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

# i dont know what im doing with my life
def runApps():
    for app in apps:
        os.startfile(app)

# basically what it says
canvas = tk.Canvas(root, height=500, width=700, bg="orange")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relx=0.1, rely=0.1, relheight=0.7)

openFile = tk.Button(root, text="Open File", padx=50, pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=50, pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()


for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()


# in oreder to run it just use it
root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')