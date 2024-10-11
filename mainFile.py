from questions_answers import lst_of_questions

def calculations():
    points = 0 

    while True:
        question, correct_answer = lst_of_questions()

        print(question)

        user_answer = int(input("Enter your answer: "))

        if user_answer == correct_answer:
            print("Correct!")
            points +=1
        

        else: 
            print(f"Wrong answer the right answer is {correct_answer}!") 
        
        print(f"These are your current points[{points}]")
        

def menu():
    
    print("Welcome to the Math Game!")

    while True:
        user_input = (input("Write 'start' to start or 'stop' to stop:"))
        
        if user_input.lower() == 'start':
            print("Starting your game...")
            calculations()
    
        elif user_input.lower() == 'stop':
            print(f"Stopping...Goodbye!")
            break
        else: 
            print("Invalid entry, enter either 'stop' or 'start'")


menu()