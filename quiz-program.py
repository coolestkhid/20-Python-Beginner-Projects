# a dictionary that stores questions and answers
# have a variable that track the score of the player
# loop through the dictionary using the key value pairs
# display each question to the user and allow them to answer
# tell them if they are right or wrong
# show the final results when the quiz is completed

quiz = {
    "question 1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    
    "question 2": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    
    "question 3": {
        "question": "What is the capital of Italy?",
    "answer": "Rome"
    },
    
    "question 4": {
        "question": "What is the capital of Spain?",
    "answer": "Madrid"
    },
    
    "question 5": {
        "question": "What is the capital of Portugal?",
    "answer": "Lisbon"
    },
    
    "question 6": {
        "question": "What is the capital of Switzerland?",
    "answer": "Bern"
    },
    
    "question 7": {
        "question": "What is the capital of Austria?",
    "answer": "Vienna"
    },
} 

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")
    
    if answer.lower() == value['answer'].lower():
        print('Correct')
        score = score + 1
        print("Your score is: " + str(score))
        print(" ")
        print(" ")
        
    else:
        print("Wrong!")
        print("The answer is : " + value['answer'])
        print("Your score is: " + str(score))
        print(" ")
        print(" ")
        
print("You got " + str(score) + " out of 7 questions correctly")
print("Your percentage is " + str(int(score/7 * 100)) + "%")