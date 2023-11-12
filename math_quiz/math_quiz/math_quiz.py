import random

def generate_random_integer(min, max):
    """
    Generate a random integer.
    """
    return random.randint(min, max)

def generate_random_operator():

    """
    Generate a random math operator
    """
    return random.choice(['+', '-', '*'])

def generate_problem_and_answer():

    """
    Generate a random math problem and its answer
    """
    n1 = generate_random_integer(1, 10)
    n2 = generate_random_integer(1, 5)
    operator = generate_random_operator()

    problem = f"{n1} {operator} {n2}"

    if operator == '+':
        answer = n1 + n2
    elif operator == '-':
        answer = n1 - n2
    else:
        answer = n1 * n2
    return problem, answer
def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        problem, answer = generate_problem_and_answer()
        print(f"\nQuestion: {problem}")

        # Adding error handling for invalid user input
        try:10

        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue  # Skip the rest of the loop and move to the next question
        user_answer = int(input("Your answer: "))
        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
