import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog

class MyFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title('Simple Editor')

        # メニューをつくる
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.openfile)
        filemenu.add_command(label="Save as...", command=self.saveas)
        filemenu.add_command(label="Exit", command=self.master.destroy)
        menubar.add_cascade(label="File", menu=filemenu)
        self.master.config(menu=menubar)

        self.editbox = tk.Text(self)
        self.editbox.pack()

    def openfile(self):
        filename = tkinter.filedialog.askopenfilename()
        if filename:
            tkinter.messagebox.showinfo("Filename", "Open: "+filename)
            with open(filename, 'r') as file:
                text = file.read()
            self.editbox.delete('1.0', tk.END)
            self.editbox.insert('1.0', text)
        else:
            tkinter.messagebox.showinfo("Filename", "Canceled")

    def saveas(self):
        filename = tkinter.filedialog.asksaveasfilename()
        if filename:
            with open(filename, 'w') as file:
                text = file.write(self.editbox.get('1.0', tk.END))
            tkinter.messagebox.showinfo("Filename", "Saved AS:" + filename)
        else:
            tkinter.messagebox.showinfo("Filename", "Canceled")

root = tk.Tk()
f = MyFrame(root)
f.pack()
f.mainloop()
