import pyodbc
from question_model import Question
from questinsData import *
from quiz_brain import QuizBrain
from userInterface import QuizInterface


question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


# for question in qu_next_data:
#     question_text = question["question"]
#     question_answer = question["correct_answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

import pyodbc

# def server():
#     join = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL"
#                           " Server};SERVER=LAPTOP-CE0N2UOJ;DATABASE=myQA;Trusted_connection=yes")
#
#     print("insert...")
#     curser = join.cursor()
#     curser.execute("insert into [TBL_qaclass]([firstName],[lastName],[age],[id],[Result])"
#                    f"values('natnael', 'girma', '45', 345234211, {quiz.score * 1000})")
#     curser.commit()
#     print("reading...")
#     curser.execute("select * from cl_work")
#     while 1:
#         row = curser.fetchone()
#         if not row:
#             break
#         print(row)
#
#     curser.close()
#     join.close()
# server()
#
# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score * 10}/{quiz.question_number * 10}")