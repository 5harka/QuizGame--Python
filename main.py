from data import question_data
from question_model import Questions
from quiz_brain import Quizbrain

TEXT_LIST = []
ANSWER_LIST = []

question_bank = []
for test in question_data:

    q_one = test["question"] #Was "text" for the previous dataset
    a_one = test["correct_answer"] #Was "answer" for the previous dataset
    new_question = Questions(q_text  =q_one,q_answer = a_one)
    question_bank.append(new_question)

print(question_bank)

    #if you want to seperate questions and answers here is a cool way to do it (text and answer are in the for loop)
#     TEXT_LIST.append(q_one)
#     ANSWER_LIST.append(a_one)
# print(TEXT_LIST,ANSWER_LIST)

quiz = Quizbrain(q_list= question_bank)

quiz.still_has_questions()
print(quiz.Question_checker)
while quiz.Question_checker == True:
    quiz.still_has_questions()
    if quiz.Question_checker == True:
        quiz.next_question()
    elif quiz.Question_checker == False:
        print(f"\nGAME OVER, Your total Score is {quiz.score}/{quiz.question_number}!")













## How to set up the questions up to 10,
# i = 0
# while i != 10:
#     WhatShowed = input(f"{question_bank[i].text} (True/False)")
#     if WhatShowed == question_bank[i].answer:
#         print("Correct!")
#         i += 1
#         print(f"You got {i} points")
#     else:
#         print("Nice Try, NOW GET IT RIGHT OK!!!")


