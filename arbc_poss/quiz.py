import random

MIN_QUESTIONS = 10
MIN_ACCURACY = 0.9

def weighted_dict(filename):
    dict = {}
    f = open(filename)
    total_weight = 0
    for line in f:
        items = line.split(",")
        arabic = items[0]
        english = items[1]
        weight = float(items[2])
        dict[arabic] = [english, weight]
        total_weight += weight
    for word in dict:
        dict[word][1] = dict[word][1]/total_weight
    return dict

def weighted_random(dict):
    rand = random.random()
    cumsum = 0
    for key in dict:
        cumsum += dict[key][1]
        if cumsum > rand:
            return key
    return "---"

def arabic_possessive(noun, suffix):
    if noun[-1] == "ة":
        return noun[:-1] + "ت" + suffix
    else:
        return noun + suffix

noun_dict = weighted_dict("nouns.txt")
suffix_dict = weighted_dict("suffixes.txt")


num_questions = 0
num_correct = 0
while num_questions < MIN_QUESTIONS or num_correct/num_questions < MIN_ACCURACY:
    noun = weighted_random(noun_dict)
    suffix = weighted_random(suffix_dict)
    eng_noun = noun_dict[noun][0]
    eng_poss = suffix_dict[suffix][0]
    print(eng_poss + " " + eng_noun + " = ?")
    correct_answer = arabic_possessive(noun, suffix)
    answer = input()
    if answer == correct_answer:
        num_correct += 1
        print("Correct!")
    else:
        print("Incorrect! Correct answer: " + correct_answer)
    num_questions += 1
    if num_questions % 5 == 0:
        print("Total correct: " + str(num_correct) + ", accuracy: " + str(num_correct/num_questions))

