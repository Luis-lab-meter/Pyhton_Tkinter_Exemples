#https://forgoal.gitbooks.io/python/content/creating-a-tkinter-class-and-waiting-for-a-return-value.html
#2021-05-29 V1

import tkinter as tk
from child import *

class windowMain(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.button = tk.Button(self, text="Click me!", command=self.on_click)
        self.label = tk.Label(self, width=80)
        self.label.pack(side="top", fill="x")
        self.button.pack(pady=20)

    def on_click(self):
        result = WindowSub(self).waitAndGetValue(self)
        self.label.configure(text="your result: %s" % result)

if __name__ == "__main__":
    root = tk.Tk()
    windowMain(root).pack(fill="both", expand=True)
    root.mainloop()
