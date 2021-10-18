import random
from gen_numbers import *

MIN_QUESTIONS = 10
MIN_ACCURACY = 0.9

num_questions = 0
num_correct = 0
while num_questions < MIN_QUESTIONS or num_correct/num_questions < MIN_ACCURACY:
    rand = random.random()
    correct_answer = 0
    if rand < 0.33:
        num1 = random.randint(0, 50)
        num2 = random.randint(0, 50)
        correct_answer = number_names[num1+num2]
        print(number_names[num1] + " زائد " + number_names[num2] + " يساوي ... ؟")
    elif rand < 0.66:
        num1 = random.randint(50, 100)
        num2 = random.randint(0, 50)
        correct_answer = number_names[num1-num2]
        print(number_names[num1] + " ناقص " + number_names[num2] + " يساوي ... ؟")
    else:
        num1 = random.randint(0, 20)
        num2 = random.randint(0, int(num1/100))
        correct_answer = number_names[num1*num2]
        print(number_names[num1] + " في " + number_names[num2] + " يساوي ... ؟ ")
    answer = input()
    if answer == correct_answer:
        num_correct += 1
        print("Correct!")
    else:
        print("Incorrect! Correct answer: " + correct_answer)
    num_questions += 1
    if num_questions % 5 == 0:
        print("Total correct: " + str(num_correct) + ", accuracy: " + str(num_correct/num_questions))

print("Congratulations! You have achieved above 90 percent accuracy.")
