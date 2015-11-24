import sys
import Tkinter as tk
E=tk.E
W=tk.W
N=tk.N
S=tk.S
def main():
    app = App()
    app.master.title("Sample application")
    app.mainloop()

class App(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky=N+S+E+W)

        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)

        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.__createWidgets()

    def __createWidgets(self):
        self.f1 = tk.Frame(self, height=100, width=200, bg='green')
        self.f1.grid(row=0, sticky=E+W)

        self.f2 = myTestFrame(self, bg='yellow', height=100, width=200)

        self.f3 = tk.Frame( self, bg = "cyan", height = 100, width = 200)
        self.f3.grid(row=2, sticky=E+W)

        self.quitButton = tk.Button(self, text="Quit", command=self.quit)
        self.quitButton.grid(row=4, column=0, sticky=E+W)

class myTestFrame( tk.Frame ):
    def __init__(self, parent, cnf={}, **kw):
        tk.Frame.__init__(self, parent, cnf, **kw)
        self.grid(row=1, sticky=N+S+E+W)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)                
        self.myText = tk.Text(self)
        self.myText.grid(row=0, sticky=N+S+E+W)

if __name__ == "__main__":
    main()
