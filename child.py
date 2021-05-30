import tkinter as tk

class WindowSub(object):
    def __init__(self, parent):
        self.toplevel = tk.Toplevel(parent)
        self.var = tk.StringVar()
        label = tk.Label(self.toplevel, text="Pick something:")
        om = tk.OptionMenu(self.toplevel, self.var, "one", "two","three", command=self.getValue)
        label.pack(side="top", fill="x")
        om.pack(side="top", fill="x")

    def makeSometing(self, event):
        self.toplevel.deiconify()
        self.toplevel.wait_window()
        value = self.var.get()
        return value

    def getValue(self, event):
        self.toplevel.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    WindowSub(root)
    root.mainloop()