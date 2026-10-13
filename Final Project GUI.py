from tkinter import *

class productivityTracker:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('805x300')
        self.window.title('Productive Study Session')
        
        self.create_widgets()
        
        self.window.mainloop()

    def create_widgets(self):
        # Label
        Start = Label(self.window,text='Productive Study Method: ')
        Start.grid(row=0, column=0,sticky=W)
        
        # Listbox
        # 6. Listbox – Scrollable list
        lb = Listbox(self.window, width=20, height=6)
        lb.insert(1, "Pomodoro")
        lb.insert(2, "Active Recall")
        lb.insert(3, "Feynman's Technique")
        lb.insert(4, "Interleaving")
        lb.insert(5, "Dual Coding")
        lb.insert(6, "Practice Test")
        lb.grid(row=2,column=1)
               
        # Button
        study = Button(self.window,text='Begin Session')#,command=self.start_session)
        study.grid(row=3,column=1)

        
product = productivityTracker()