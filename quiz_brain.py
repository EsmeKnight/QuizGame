class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.questions_list = question_list
        self.score = 0
        #question_list is questions list object in main.py

    def still_has_questions(self):
        return self.question_number <= len(self.questions_list) - 1

    # using the self attribute here means i can grab data from the init
    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)? ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower()[0] == correct_answer.lower()[0]:
            print("Correct")
            self.score += 1
        else:
            print(f"Wrong, the correct answer is: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
    
    def show_score(self):
        print(f"Your final score is: {self.score}/{self.question_number}")