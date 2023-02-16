import random

LowestNumberRange=int(input("Please enter the lowest of number you want to get the questions from: "))
HighestNumberRange=int(input("Please enter the highest of number you want to get the questions from: "))   
QuestionsNumber=int(input("How many questions do you want? "))  
QuestionArray=[]  
Number=0

def generate_question():
    # Generate two random numbers for the base and exponent
    
    base1 = random.randint(LowestNumberRange, HighestNumberRange)
    exponent1 = random.randint(1, 9)

    base2 = random.randint(LowestNumberRange, HighestNumberRange)
    exponent2 = random.randint(1, 9)    

    # Generate a random operator
    operators = ["+", "-", "x", "÷"]
    operator = random.choice(operators)

    # Generate a random question
    if operator == "+":
        question = f"What is the value of {base1}^{exponent1} + {base2}^{exponent2}?"
        answer=base1**exponent1+base2**exponent2
    elif operator == "x":
        question = f"What is the value of {base1}^{exponent1} * {base2}^{exponent2}?"
        answer=base1**exponent1*base2**exponent2
    elif operator == "÷":
        question = f"What is the value of {base1}^{exponent1} / {base2}^{exponent2}?"
        answer=base1**exponent1/base2**exponent2
    else:
        question = f"What is the value of {base1}^{exponent1} - {base2}^{exponent2}?"
        answer=base1**exponent1+base2**exponent2


    return question

# Generate and print 5 random questions

print("Your questions are: ")
for i in range(QuestionsNumber):
    Number=Number+1
    QuestionArray.append(generate_question())
    print(Number, ". ", QuestionArray[i])

    userAnswer=int(input("What is the answer to this?"))

