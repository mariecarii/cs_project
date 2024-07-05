## write out questions into a tuple
questions = ("Which operator is used for power? ",
            "How do we check the type of a variable x? ",
            "What is the correct way to write an else if statement? ",
            "How do we access the first element in a list called my_list? ",
            "How do we access the first letter in the first element in a list called my_list? ",
            "What method can we use to add more elements to a list? ",
            "What function can we use to find the length of 'hello'? ",
            "How can we access the last element in a list called user_list? ",
            "What will print(list(range(5,10))) print? ",
            "How would be access the population numbers in total_populations = {'U.S.': 336000000, 'Mexico': 129000000} ",
            "What will print(type(3.14)) print? ",
            "Which statement will stop a loop? ",
            "Strings are immutable ",
            "Lists are mutable ",
            "Tuples are mutable ",
            "Which of the following is a list? ",
            "Which of the following is a tuple? ",
            "What will (list(range(0,100)[10:20:2]) print? ",
            "How can I add 1 to fav_number? ",
            "How do you declare a function called number_randomizer? ",
            )

## write out options into a tuple
choices = ( ("A. ^","B. %","C. **","D. *"),
            ("A. type(x)","B. typeof(x)","C. varType(x)","D. typeOf(x)"),
            ("A. elif","B. else if ","C. Both A & B","D. None"),
            ("A. my_list[1]","B. my_list.firstElement()","C. my_list[a]","D. my_list[0]"),
            ("A. my_list[0]","B. my_list[0][0]","C. my_list[1]","D. my_list[0][1]"),
            ("A. .add()", "B. .addElement()", "C. .extend()", "D. .extendList()"),
            ("A. len('hello')", "B. length('hello')", "C. lenOf('hello')", "D. lengthOf('hello')"),
            ("A. user_list[0]", "B. user_list[-1]", "C. user_list[-2]", "D. user_list[last]"),
            ("A. [5, 6, 7, 8, 9, 10]", "B. [6, 7, 8, 9]", "C. [6, 7, 8, 9, 10]", "D. [5, 6, 7, 8, 9]"),
            ("A. total_populations.keys()", "B. total_populations.values()", "C. total_populations.keyValues()", "D. total_populations.valueItems()"),
            ("A. boolean", "B. int", "C. float", "D. decimal"),
            ("A. pass", "B. stop", "C. break", "D. exit"),
            ("A. True", "B. False"),
            ("A. True", "B. False"),
            ("A. True", "B. False"),
            ("A. ['red', 'blue', 'pink']", "B. {'red', 'blue', 'pink'}", "C. ('red', 'blue', 'pink')", "D. 'red', 'blue', 'pink' " ),
            ("A. ['red', 'blue', 'pink']", "B. {'red', 'blue', 'pink'}", "C. ('red', 'blue', 'pink')", "D. 'red', 'blue', 'pink' " ),
            ("A. [11, 13, 15, 17, 19]", "B. (10, 12, 14, 16, 18", "C. [10, 12, 14, 16, 18, 20]", "D. [10, 12, 14, 16, 18]"),
            ("A. fav_number += 1", "B. fav_number = fav_number + 1 ", "C. Both A & B", "D. fav_number ++"),
            ("A. def number_randomizer(): ", "B. function number_randomizer(): ", "C. declare number_randomizer(): ", "D. myDef number_randomizer(): "),
           )      

## write out answers into a tuple
answers = ("C", "A", "A", "D", "B", "C", "A", "B", "D", "B", "C", "C", "A", "A", "B", "A", "C", "D", "C", "A")

## create a variable for the question number 
question_number = 0 
## create a variable to keep score
score = 0

for question in questions:
    ##this line will provide seperation between questions for a cleaner, more readable look
    ##i used an f string to dynamically change the question number (i did +1 because my question_number count starts at 0 and i dont want Question #0)
    print(f"---------QUESTION #{question_number + 1}---------")
    ##this line will print the question
    print(question)
    ##this line will give the choices for the question. we will know which question because we are using [question_number] for the index
    for choice in choices[question_number]:
        print(choice) 
    ##ask user for a guess and user .upper method incase user inputs selection in lowercase
    user_guess = input("Enter A, B, C, or D: ").upper()
    if user_guess == answers[question_number]:
        score += 1
        print("You're correct!")
    elif user_guess != answers[question_number]:
        print("You're incorrect!")
        print(f"{answers[question_number]} is the answer")
    else:
        print('ERROR')
    ##this line will add 1 to the question number so we can continue to the next question
    question_number += 1
    ##print a new line to create a cleaner, more readable look
    print("\n")

print(f"Your final score: {score}!")