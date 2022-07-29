from re import T
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questions = []

for data in question_data:
    questions.append(Question(data["text"], data["answer"]))

quiz = QuizBrain(questions)

while quiz.still_has_questions():
    quiz.next_question()
else:
    quiz.show_score()
