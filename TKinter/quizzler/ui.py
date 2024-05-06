from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.win = Tk()
        self.win.title('Quizzler')
        self.win.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text='Score = 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.text_label = self.canvas.create_text(150, 125, width=280, text='questions to add', fill=THEME_COLOR, font=('Arial', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        right_img = PhotoImage(file='img/right.png')
        self.right_button = Button(image=right_img, highlightthickness=0, command=self.true)
        self.right_button.grid(row=2, column=1)

        wrong_img = PhotoImage(file='img/wrong.png')
        self.wrong_button = Button(image=wrong_img, highlightthickness=0, command=self.false)
        self.wrong_button.grid(row=2, column=0)

        self.get_next_q()

        self.win.mainloop()

    def get_next_q(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():

            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text_label, text=q_text)
        else:
            self.canvas.itemconfig(self.text_label, text=f"you've reached the end of the quiz\n your score is {self.quiz.score}/10")
            self.right_button.config(state='disabled')
            self.wrong_button.config(state='disabled')
    def true(self):
        is_right = self.quiz.check_answer('True')
        self.get_feed(is_right)

    def false(self):
        is_right = self.quiz.check_answer('False')
        self.get_feed(is_right)

    def get_feed(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.win.after(1000, self.get_next_q)