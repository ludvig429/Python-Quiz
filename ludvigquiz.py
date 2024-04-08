# Quiz App - Tutorial for Learn IT

# Questions and possible answers as well as the define for which answer is correct. Make note of the formatting and placement of symbols
questions = [
    {
        "question": "How many siblings do i have?",
        "options": ["A: 1", "B: 2", "C: 4", "D: 78"],
        "answer": "A"
    },

{
        "question": "How old am i?",
        "options": ["A: 18", "B: 17", "C: 19", "D: 20"],
        "answer": "C"
    },

{
        "question": "What is my current favorite artist?",
        "options": ["A: Drake", "B: Metallica", "C: Korn", "D: Taylor Swift"],
        "answer": "B"
    },

{
        "question": "What is my current favorite videogame?",
        "options": ["A: Apex Legends", "B: Fortnite", "C: GTA5", "D: EA Sports FC24"],
        "answer": "A"
    },

{
        "question": "How many pets do i currently have?",
        "options": ["A: 1", "B: 2", "C: 3", "D: 0"],
        "answer": "D"
    },

{
        "question": "What is my middle name?",
        "options": ["A: Oscar", "B: Mattias", "C: Johan", "D: I dont have one"],
        "answer": "B"
    },

{
        "question": "When is my birthday?",
        "options": ["A: 1 March", "B: 18 January", "C: 24 December", "D: 19 January"],
        "answer": "B"
    },

{
        "question": "What is my favorite movie?",
        "options": ["A: Pulp Fiction", "B: The Hangover", "C: The Dark Knight", "D: Inception"],
        "answer": "A"
    },

{
        "question": "What is my favorite TV-Series?",
        "options": ["A: Breaking Bad", "B: Lucifer", "C: Lost", "D: South Park"],
        "answer": "C"
    },

{
        "question": "What is my favorite subject in school?",
        "options": ["A: English", "B: Math", "C: History", "D:  I dont have one"],
        "answer": "D"
    },
    # You can remove this comment or move it down and add more questions. You should enclose each question in their own {} brackets.
]

# This function will define the quiz code on launch
def run_quiz(questions):
    score = 0  # Initialize score to 0 and create a variable "score" to store the value of correct answers

    # Loop through all the questions. This will follow all the questions above until finished
    for question in questions:
        print("\n" + question["question"])  # Print the question
        for option in question["options"]:
            print(option)  # Print all the answer options

        # Get the user's answer
        user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()

        # Check if the user's answer is correct
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1  # Increment score if correct
        else:
            print("Wrong answer.")

    # Print the final score from the stored variable
    print(f"\nYou got {score} out of {len(questions)} questions correct!")

# Run the quiz
run_quiz(questions)