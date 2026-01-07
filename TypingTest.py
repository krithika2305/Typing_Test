from english_words import english_words_set
from tkinter import *
import tkinter.font as font
import random

score = 0
time = 0
count = 0
after_id = None
words = list(english_words_set)
def startGame():
    global score, time, count, after_id
    score = 0
    time = 0
    count = 0
    after_id = None
    wn = Tk()
    wn.geometry('700x600')
    wn.title('Typing Test By PythonGeeks')
    wn.config(bg='honeydew2')
    def timeFunc():
        global time, score, count, after_id
        if count <= 10:
            time += 1
            timer.configure(text=time)
            after_id = timer.after(1000, timeFunc)
        else:
            if after_id:
                timer.after_cancel(after_id)
            showResults()
    def showResults():
        result_win = Toplevel(wn)
        result_win.geometry("400x300")
        result_win.title("Results")
        result_win.config(bg="lavender")
        result_label = Label(result_win, text="Results", font=('arial', 20, 'bold'),
                             bg="lavender", fg="black")
        result_label.pack(pady=10)
        summary = Label(result_win,
                        text='Time taken = {} \nScore = {} \nMissed = {}'.format(
                            time, score, count - score - 1),
                        font=('arial', 15, 'italic bold'),
                        fg='grey', bg="lavender")
        summary.pack(pady=20)
        exit_btn = Button(result_win, text="Exit", font=('arial', 12, 'bold'),
                          bg="tomato", fg="white", command=wn.destroy)
        exit_btn.pack(side=LEFT, padx=40, pady=20)
        # Continue button
        def restart():
            result_win.destroy()
            wn.destroy()
            startGame()
        cont_btn = Button(result_win, text="Continue", font=('arial', 12, 'bold'),
                          bg="lightgreen", fg="black", command=restart)
        cont_btn.pack(side=RIGHT, padx=40, pady=20)
    def mainGame(event):
        global score, count
        if time == 0:
            random.shuffle(words)
            nextWord.configure(text=words[0])
            userInput.delete(0, END)
            timeFunc()
        if userInput.get() == nextWord['text']:
            score += 1
            scoreboard.configure(text=score)
        count += 1
        if count <= 10:
            random.shuffle(words)
            nextWord.configure(text=words[0])
            userInput.delete(0, END)
    label = Label(wn, text='Typing Test By PythonGeeks', font=('arial', 25, 'italic bold'),
                  fg='gray', width=40)
    label.place(x=10, y=10)
    nextWord = Label(wn, text='Hit enter button to start and after typing the word',
                     font=('arial', 20, 'italic bold'), fg='black')
    nextWord.place(x=30, y=240)
    scorelabel = Label(wn, text='Your Score:', font=('arial', 25, 'italic bold'), fg='red')
    scorelabel.place(x=10, y=100)
    scoreboard = Label(wn, text=score, font=('arial', 25, 'italic bold'), fg='blue')
    scoreboard.place(x=100, y=180)
    timerlabel = Label(wn, text='Time Elapsed:', font=('arial', 25, 'italic bold'), fg='red')
    timerlabel.place(x=450, y=100)
    timer = Label(wn, text=time, font=('arial', 25, 'italic bold'), fg='blue')
    timer.place(x=560, y=180)
    userInput = Entry(wn, font=('arial', 25, 'italic bold'), bd=10, justify='center')
    userInput.place(x=150, y=330)
    userInput.focus_set()
    wn.bind('<Return>', mainGame)
    wn.mainloop()
# Main window
wn = Tk()
wn.geometry('600x600')
wn.title("PythonGeeks Typing Test")
wn.config(bg='LightBlue1')
headingFrame1 = Frame(wn, bg="snow3", bd=5)
headingFrame1.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to \nTyping Test",
                     bg='azure2', fg='black', font=('Courier', 15, 'bold'))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
btn = Button(wn, text="Start", bg='old lace', fg='black',
             width=20, height=2, command=startGame)
btn['font'] = font.Font(size=12)
btn.place(x=200, y=300)
wn.mainloop()
