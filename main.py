

flashcards = {}

def process_file(file):
    with open(file, "r") as f:
        qanda = f.read().split("\n\n")
        for qa in qanda:
            flashcards[qa.split("\n")[0]] = qa.split("\n")[1]


def ask_questions(dictionary):
    score = 0
    wrong_questions = {}
    for question, answer in dictionary.items():
        response = input(question + ": ")
        if response.lower() == answer.lower():
            print("Correct!\n")
            score += 1
            if question in wrong_questions:
                del wrong_questions[question]
        else:
            print("Incorrect." + "\nThe correct answer is: " + answer + ".\n")
            if question not in wrong_questions:
                wrong_questions[question] = answer

    print("You scored " + str(score) + " out of " + str(len(dictionary)) + ".")
    return score, wrong_questions


process_file(input("What would you like to revise?: ") + ".txt")

print("\nLet's begin!\n")

score, wrong_questions = ask_questions(flashcards)

while score < len(flashcards) and len(wrong_questions) > 0:
        response = input("Would you like to go over the questions you got wrong? (y/n): ")
        print("\n")
        if response.lower() == "y":
            score, wrong_questions = ask_questions(wrong_questions)
        if response.lower() == "n":
            print("Good luck next time!")
            break

if len(wrong_questions) == 0:
    print("Congratulations! You have mastered the material!")



