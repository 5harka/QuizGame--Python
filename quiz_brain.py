## IMPORTANT TO KNOW   You can use this instead of what I wrote, This will Give a boolean
## response (True/False) which can be used in the while loop. What I did has to have (True/False) to come
## out in the beginning
#    def still_has_questions(self):
#        return self.question_number < len(self.question_list)


class Quizbrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        self.Question_checker = True
        if self.question_number+1 < len(self.question_list):
            self.Question_checker = True
        else:
            self.Question_checker = False


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current_question.text} (True/False):")
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print(f"Correct!! your Score is {self.score} out of {self.question_number} questions")
        else:
            print("Wrong answer")




