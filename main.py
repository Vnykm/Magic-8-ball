from tkinter import *
import time, Answers, random

def answer():
    return Answers.Answers[random.randint(0, 19)]


class Ball:
    def __init__(self):
        self.win = Tk()
        self.win.minsize(700,700)
        self.win.title('Magic 8-Ball')
        self.win.configure(bg='#000956')
        EBicon = PhotoImage(file='8ball.png')
        self.win.iconphoto(False, EBicon)
        Label(self.win, text="Ask Your Question Below!", bg='#000956', fg='#FFFFFF', font=("Helvetica", 20)).pack(pady=5)
        Entry(self.win, width=40, font=("Helvetica", 20)).pack(pady=5, ipady=5)
        self.pane = Frame(self.win, bg='#000956', width=40)
        self.pane.pack(fill = BOTH, expand = True)
        Button(self.pane,text="Answer", command=self.answer, bg='#000956', font=("Helvetica", 20)).pack(side = LEFT, expand = True, fill = BOTH)
        Button(self.pane, text="Quit", command=exit, bg='#000956', font=("Helvetica", 20)).pack(side = LEFT, expand = True, fill = BOTH)
        Label(self.win, image=EBicon, bg='#000956').pack(pady=5, fill='both', expand='yes')
        self.ballsays = Label(self.win, text="Ask Your Question", bg='#000956', fg='#FFFFFF', font=("Helvetica", 20))
        self.ballsays.pack(pady=5)

        self.win.mainloop()

    def answer(self):
        self.ballsays.config(text='Shaking...')
        time.sleep(1)
        self.ballsays.config(text=random.choice(Answers.Answers))

        
if __name__ == "__main__":
    Run = Ball()

