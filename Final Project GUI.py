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
        Start = Label(self.window,text='Productive Study Methods: ')
        Start.grid(row=0, column=0,sticky=W)
        
        # Listbox
        # 6. Listbox – Scrollable list
        self.study_list = Listbox(self.window, width=20, height=6)
        study_methods = ["Pomodoro", "Active Recall", "Feynman's Technique",
                         "Interleaving", "Dual Coding", "Practice Test"]
        for method in study_methods:
            self.study_list.insert(END,method)
        self.study_list.grid(row=1,column=0)
        
        # Button
        #study = Button(self.window,text='Begin Session')#,command=self.start_session)
        #study.grid(row=2,column=0)
        
        # Study Method Listbox
        self.study_list.bind("<<ListboxSelect>>",self.load_method_options)
        
        self.option_listbox = Listbox(self.window, width=20, height=6)
        self.option_listbox.grid(row=1,column=1)
        
    def load_method_options(self, study_list):
        sel = self.study_list.curselection()
        if len(sel) == 0:
            return

        study_index = sel[0]                
        self.option_listbox.delete(0, END)
        if study_index == 0:          # Pomodoro
            options = ["25/5 Standard",
                       "50/10 Extended",
                       "Custom Timer"]
            
        elif study_index == 1:        # Active Recall
            options = ["Flashcards",
                       "Question Bank",
                       "Self Quiz"]

        elif study_index == 2:        # Feynman
            options = ["Explain Topic",
                       "Teach Concept",
                       "Knowledge Check"]
            
        elif study_index == 3:
            options = ["Mixed Topic Study"]

        elif study_index == 4:
            options = []

        for item in options:
            self.option_listbox.insert(END, item)
            
        self.option_listbox.bind("<<ListboxSelect>>",self.on_option_select)
        
    def on_option_select(self, event):
        sel = self.option_listbox.curselection()
        self.topic_label = Label(self.window, text="Study Topic:")
        self.topic_entry = Entry(self.window, width=30)
        if len(sel) > 0:
            # Remove old widgets
            self.topic_label.grid_forget()
            self.topic_entry.grid_forget()

            # Show new widgets
            self.topic_label.grid(row=4, column=0, sticky=W)
            self.topic_entry.grid(row=4, column=1)

        
product = productivityTracker()
