from tkinter import *

#define my frame?
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        #Woah, a menu!? No way??!!!!
        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)

        self.pack(fill=BOTH, expand=1)
        
        #buttons???
        newButton = Button(self, text="SAY HELLO", command=self.hello)
        newButton.place(x=30, y=0)

        leaveButton = Button(self, text='EXIT', command=self.clickExitButton)
        leaveButton.place(x=0, y=0)


    def hello(self):
        print("HELLO!!")

    def clickExitButton(self):
        exit()




#start tkinter
root = Tk()
app = Window(root)

#title for window
root.wm_title("TKINT WINDOW")

#size for window
root.geometry('400x400')


root.mainloop()
