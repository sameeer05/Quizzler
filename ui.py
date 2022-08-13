from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        # Creating the score label
        self.score_label = Label(text=f"Score: ", font=("Arial", 12), fg="#FFFFFF", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1, pady=20, padx=20)
        # Creating canvas
        self.question_card = Canvas(height=250, width=300)
        self.question_text = self.question_card.create_text(150, 125, width=280, text="Question", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.question_card.grid(row=1, column=0, columnspan=2, pady=20, padx=20)
        # Creating the buttons
        self.true_pic = PhotoImage(file="images\True.png")
        self.true_button = Button(image=self.true_pic, command=self.ture_pressed)
        self.true_button.grid(row=2, column=0, pady=20, padx=20)

        self.false_pic = PhotoImage(file="images\False.png")
        self.false_button = Button(image=self.false_pic, command=self.false_pressed)
        self.false_button.grid(row=2, column=1, pady=20, padx=20)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.question_card.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.question_card.itemconfig(self.question_text, text=q_text)
        else:
            self.question_card.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def ture_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.question_card.config(bg="green")
        else:
            self.question_card.config(bg="red")
        self.window.after(1000, self.get_next_question)





