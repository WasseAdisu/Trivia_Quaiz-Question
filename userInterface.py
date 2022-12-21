import pyodbc
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
all_question = []


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")  # its name
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)  # It controls background color

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=200,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial",)
        )

        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score * 10}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
           # print(self.quiz.next_question())  #########

            join = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL "
                                  "server};SERVER=LAPTOP-CE0N2UOJ;DATABASE=myQA;Trusted_connection=yes")

            create = join.cursor()
            create.execute('CREATE TABLE sami(Questions text)')
            create.execute("INSERT INTO sami VALUES (?)", (self.quiz.next_question()))
            join.commit()
            create.execute('SELECT * FROM sami')
            z = create.fetchall()

        else:
            self.canvas.itemconfig(self.question_text, text="you've finished")  # to continue

            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
