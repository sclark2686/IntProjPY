"""
This is the main file for my integration project.
This project is a physics study helper.
"""

__author__ = "Samuel Clark"

import math


# I used concepts we learned in class as well as
# http://arve0.github.io/example_lessons/python/lessons/Quiz/Quiz.html
# https://en.wikibooks.org/wiki/Python_Programming/Conditional_Statements
# for help with formatting the questions neatly


def concept_question():
    """
    This function utilizes a concept or word question taken from my physics
    class. The function presents a question and gives and answer based on an
     answer the user inputs.
    input
    """
    print("Here's your first concept question!")
    print("A plane traveling horizontally to the right at")
    print("100 m/s flies past a helicopter that is going")
    print("straight up at 20 m/s. From the helicopter’s")
    print("perspective, the plane’s direction and speed are: ")
    print("                                                   ")
    print("A.  right and up, more than 100 m/s. ")
    print("B.  right and up, less than 100 m/s. ")
    print("C.  right and down, more than 100 m/s. ")
    print("D.  right and down, less than 100 m/s. ")
    print("E.  right and down, 100 m/s.")

    answer = input()

    if answer == "C" or "c":
        print("Good Job!")
    else:
        print("The correct answer is C")

    closing_question()


def math_question():
    """
    This is a complete math question taken from my Physics class.
    """
    print("Here's your first math question!")
    print("                                ")
    print("There will be __ parts to this question")
    print("                                    ")
    print("How fast (in rpm) must a centrifuge rotate if a")
    print("particle 9.00 cm from the axis of rotation is to experience an")
    print("acceleration of 115,000 g’s?")

    print("How many variables are needed to answer the question?")

    answer_math_1 = input()
    if answer_math_1 == "4":
        print("correct!  you need radius, centripetal acceleration, gravity")
        print("and rotations per minute")
    else:
        print("The correct answer is 4,  you need radius, centripetal ")
        print("acceleration, gravity, and rotations per minute")

    print("which formula should you use?")
    answer_math_2 = input()
    if answer_math_2 == "Centripetal acceleration":
        print("correct!")
    else:
        print("the correct answer is Centripetal acceleration")

    print("Set up the problem, how do you begin?")
    answer_math_3 = input()
    if answer_math_3 == "rw^2 = 115,000 g's":
        print("correct!")
    else:
        print("to begin solving, take Centripetal acceleration set it equal")
        print(" to 115,000 g's")
    print("convert your variables to meters and plug them in")
    print(".enter your answer")

    answer_math_4 = input()
    if answer_math_4 == ".09*w^2=115,000 g's":
        print("correct!")
    else:
        print("incorrect, it should be .09*w^2=115,000 g's")

    print("solve for w and answer the problem")

    answer_math = 3538.68

    answer_math_5 = int(input())
    if answer_math_5 == answer_math:
        print("correct!")
    else:
        print("Incorrect the answer is 3538.68")

    print("dont forget to put your answer in radians!")

    radians = 60 / (2 * 3.14159)
    answer_math *= radians
    print(answer_math)

    closing_question()


def formula_quiz():
    """
    This is a  quiz that will aid the studier in memorizing useful physics
    formulas. The formula's and formula names are commonly used but were
    specifically taken from
    https://www.toppr.com/guides/physics-formulas/basic-physics-formula/.
    The function will ask the user to match the formula's to names one by one.
    The function will then give a score at the end based on right and wrong
    answers. If the user score is low enough it will print a statement telling
    the user to study harder.
    """

    # Average Speed         S = d/t
    # Acceleration          a = (v-u)/t
    # Density               p = m/V
    # Newton’s Second Law   F = ma
    # Power                 P = W/t
    # Weight                W = mg
    # Pressure              P = F/A
    # Kinetic Energy        E = (1/2)mv^2
    # Ohms Law              V = IxR
    # Frequency             f = V/λ

    print("Welcome to the formula quiz!. This section will ask 10 jeopardy ")
    print("style questions based on 10 commonly used physics formulas. Just")
    print("type the name of the formula when you see the equation and move on")
    print("to the next one. You'll get a score at the end.")

    definitions = ["Average Speed", "Acceleration", "Density",
                   "Newton’s Second Law", "Power", "Weight", "Pressure",
                   "Kinetic Energy", "Ohms Law", "Frequency"]

    # formulas = ['S = d/t', 'a = (v-u)/t', 'p = m/V', 'F = ma', 'P = W/t',
    #            'W = mg', 'P = F/A', 'E = (1/2)mv^2',
    #             'V = IxR', 'f = V/λ']

    quiz_decision = input("Before we start would you like to review the"
                          "definitions first? ")

    if quiz_decision == "yes":
        print("Here are the Definitions")
        for x in definitions:
            print(x)
            print("Time for the quiz!")
    else:
        print("Time for the quiz! ")
        print("                      ")

    print("                         ")

    a = input("what is S = d/t: ")
    b = input("what is a = (v-u)/t: ")
    c = input("what is p = m/V: ")
    d = input("what is F = ma: ")
    e = input("what is P = W/t: ")
    f = input("what is W = mg: ")
    g = input("what is P = F/A: ")
    h = input("what is E = (1/2)mv^2: ")
    j = input("what is V = IxR: ")
    k = input("what is f = V/λ: ")

    score = 0

    if a == "Average Speed":
        score += 10
    else:
        score += 0
    if b == "Acceleration":
        score += 10
    else:
        score += 0
    if c == "Density":
        score += 10
    else:
        score += 0
    if d == "Newton’s Second Law":
        score += 10
    else:
        score += 0
    if e == "Power":
        score += 10
    else:
        score += 0
    if f == "Weight":
        score += 10
    else:
        score += 0
    if g == "Pressure":
        score += 10
    else:
        score += 0
    if h == "Kinetic Energy":
        score += 10
    else:
        score += 0
    if j == "Ohms Law":
        score += 10
    else:
        score += 0
    if k == "Frequency":
        score += 10
    else:
        score += 0

    if score <= 50:
        print("you need to review these terms!")
    elif score == 60:
        print("Study harder!")
    elif score == 70:
        print("Could be better!")
    elif score == 80:
        print("Good job!")
    elif score == 90:
        print("Great Job!")
    else:
        print("Perfect score!")

    print("you made a" + " " + str(score) + " " + "out of 100")

    closing_question()


def angular_momentum_calculator(iav, ca, t):
    """
    This function is a calculator for angular momentum with constant
    acceleration.
    """
    # iav is the initial angular velocity
    # ca is the centripetal acceleration
    # t is the time

    final_angular_velocity = iav + ca * t
    print("the final angular velocity is", final_angular_velocity)


angular_momentum_calculator(4, 5, 6)


def motion_calculator():
    """
    This is a motion calculator. It uses the equation for linear motion with
    constant acceleration to solve for a variable.
    """
    print("This is a calculator for motion with constant acceleration")
    print("the formula for motion with constant acceleration is ")
    print("(xf) = (xi) + (v)(t)+.5(a)(t)^2")

    motion_calc = True
    while motion_calc:

        solve_for = input("Enter the variable you would like to solve for "
                          " or q to quit: ")
        if solve_for == "xf":
            xi = int(input("what is your initial position?: "))
            v = int(input("What is your velocity?: "))
            t = int(input("what is your time?: "))
            a = int(input("what is your acceleration?: "))

            xf = (xi + v * t + .5 * a * (t ** 2))
            print("the final position is ", xf)

        elif solve_for == "xi":
            xf = int(input("What is your final position?: "))
            v = int(input("What is your velocity?: "))
            t = int(input("what is your time?: "))
            a = int(input("what is your acceleration?: "))

            xi = (xf - v * t + .5 * a * (t ** 2))
            print("the initial position is ", xi)

        elif solve_for == "v":
            xf = int(input("What is your final position?: "))
            xi = int(input("what is your initial position?: "))
            t = int(input("what is your time?: "))
            a = int(input("what is your acceleration?: "))

            v = (xf - xi - ((a * (t ** 2)) * .5)) / t
            print("the velocity is ", v)

        elif solve_for == "t":
            xf = int(input("What is your final position?: "))
            xi = int(input("what is your initial position?: "))
            v = int(input("What is your velocity?: "))
            a = int(input("what is your acceleration?: "))

            p = (-v + math.sqrt((v ** 2) - 4 * .5 * a * (xf - xi)) / a)
            q = (-v - math.sqrt((v ** 2) - 4 * .5 * a * (xf - xi)) / a)

            print("the time is ", max(p, q))

        elif solve_for == "a":
            xf = int(input("What is your final position?: "))
            xi = int(input("what is your initial position?: "))
            v = int(input("What is your velocity?: "))
            t = int(input("what is your time?: "))

            a = (2 * (xf - xi - v * t) / (t ** 2))
            print("the acceleration is ", a)

        elif solve_for == "q":
            motion_calc = False
            print("Come back when you want to solve for a variable")
            closing_question()

        else:
            print("Invalid selection")
            closing_question()


def closing_question():
    """
    this is a function that will be called at the end of each question in order
    to ask if the user wants to continue or not
    """

    close = input("would you like to continue studying? Type yes to continue"
                  " Type anything else to close ")
    if close == "yes":
        navigation_question()
    else:
        print("Goodbye for now!")
        exit()


print("Welcome to Sam's Physics Study Helper. What's your name?")

name = str(input())
print("hello," + " " + name + "!" + " " + "Are you ready to learn Physics?")

option_1 = str(input())
if option_1 == "yes":
    print("Great!")
if option_1 == "no":
    print("come back later when you're ready")
    exit()


def navigation_question():
    """
    main function to navigate the study helper
    """
    print("Choose a math question, concept question or formula quiz")
    print("You can also use a linear and angular motion calculator")
    print("type concept for a concept question")
    print("type math for a math question ")
    print("Type quiz for a a formula quiz")
    print("type motion calculator for a linear motion calculator")

    question_main = str(input())
    if question_main == "concept":
        concept_question()
    elif question_main == "math":
        math_question()
    elif question_main == "quiz":
        formula_quiz()
    elif question_main == "motion calculator":
        motion_calculator()
    else:
        print("Invalid Selection.")
        closing_question()


navigation_question()
