quiz = {
    "question1": {
        "question": "What is the capital of Morocco?",
        "answer": "Rabat"
    },
    "question2": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question3": {
        "question": "What is the capital of Japan?",
        "answer": "Tokyo"
    },
    "question4": {
        "question": "What is the capital of Australia?",
        "answer": "Canberra"
    },
    "question5": {
        "question": "What is the capital of Brazil?",
        "answer": "Brasilia"
    },
    "question6": {
        "question": "What is the capital of Canada?",
        "answer": "Ottawa"
    },
    "question7": {
        "question": "What is the capital of South Africa?",
        "answer": "Pretoria"
    }
}

score = 0
num_questions = len(quiz)

for key, value in quiz.items():
    print(value['question'])
    answer = input("What's your answer: ")

    if answer.lower() == value['answer'].lower():
        print('Correct')
        score = score + 1
        print("Your Score is:" + str(score) + "\n")
    else:
        print("Wrong!")
        print("The answer is :" + value['answer'])
        print("Your score is: " + str(score) + "\n")


print("You got " + str(score)+" out of " +
      str(num_questions) + " questions correctly")
print("Your percenatge is " + str(int(score/num_questions*100))+"%")
