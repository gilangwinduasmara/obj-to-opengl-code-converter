# Copyright (c) 2020 Gilang Windu Asmara
import re
from Mesh import Mesh
import CodeConverter

import tkinter as tk
from tkinter import filedialog
import tkinter.scrolledtext as tkst


def convert():
    objFile = filedialog.askopenfilename(
        initialdir="/", title="Select file", filetypes=(("obj files", "*.obj"), ("all files", "*.*")))
    obj = open(objFile).read().split('\n')

    objCount = 0
    objects = []

    for i in obj:
        if(i.startswith('o ')):
            a = Mesh()
            a.setName(i.split()[1])
            objects.append(a)
            print('Mesh:', i.split()[1])
        if(i.startswith('v ')):
            _, x, y, z = i.split()
            objects[len(objects)-1].addVertex(x, y, z)
            print('push to vertexs', x, y, z, len(objects)-1)
    print(len(objects))
    for o in objects:
        for x in CodeConverter.CPP(o):
            app.setOutput(x)


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.output = tkst.ScrolledText(master=self,
                                        wrap=tk.WORD,
                                        width=60,
                                        height=20)
        self.select = tk.Button(self, text="Select obj file", fg="black",
                                command=convert)
        self.select.pack(side="bottom")
        self.output.pack(side="right")

    def setOutput(self, text):
        self.output.insert(tk.INSERT, text)


root = tk.Tk()
app = Application(master=root)


app.mainloop()
