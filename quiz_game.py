"""
        This is a quiz game which asks 10 general knowledge questions and 
        created in the scope of the Capstone Project by following the below instructions


        Implementation Help/Steps:
        Step 1: Set up the project
        Create a new Python file called "quiz_game.py" and open it in your
        preferred code editor.
        Step 2: Prepare the quiz questions
        Define a list of questions, each containing a question statement and
        multiple choices for answers.
        Each question should have a correct answer associated with it.
        Step 3: Display the instructions
        Print a welcome message and instructions for the quiz game.
        Step 4: Iterate through the questions
        Loop through each question from the list prepared in Step 2.
        Display the question statement and multiple choices to the user.
        Prompt the user to select their answer.
        Step 5: Check the answer.
        Compare the user's answer with the correct answer for the current
        question.
        Keep track of the user's score by awarding a point for each correct
        answer.
        Step 6: Display the result.
        Print the user's score at the end of the quiz.
        Step 7: Challenge: Add a timer.
        For an additional challenge, students can implement a timer for each
        question, allowing users a limited amount of time to answer.
"""

class Contest:
    def __init__(self):
        self.status = False
        self.questions = [
            {
                'question': "What is the capital of France",
                'options': ["Nice", "Marseille", "Paris", "Lille"],
                'correct_answer': "Paris",
                'value': 1  # Easy question
            },
            {
                'question': "What is the biggest continent in the world?",
                'options': ["Antarctica", "Asia", "North America", "Africa"],
                'correct_answer': "Asia",
                'value': 2  # Easy question
            },
            {
                'question': "What is the chemical symbol for gold?",
                'options': ["Au", "Ag", "Fe", "Cu"],
                'correct_answer': "Au",
                'value': 3  # Easy question
            },
            {
                'question': "Which acid is in vinegar?",
                'options': ["Acetic", "Sulfuric", "Citric", "Oxalic"],
                'correct_answer': "Acetic",
                'value': 4  # Easy question
            },
            {
                'question': "Which planet is closest to the Sun?",
                'options': ["Mars", "Venus", "Jupiter", "Mercury"],
                'correct_answer': "Mercury",
                'value': 5  # Easy question
            },
            {
                'question': "Which is not an element in the periodic table?",
                'options': ["Americium", "Volcium", "Lawrencium", "Francium"],
                'correct_answer': "Volcium",
                'value': 6  # Easy question
            },
            {
                'question': "Which musical instrument is known as the 'king of instruments'?",
                'options': ["Piano", "Violin", "Trumpet", "Guitar"],
                'correct_answer': "Piano",
                'value': 4  # Easy question
            },
            {
                'question': "Who is the author of the famous novel 'Pride and Prejudice'?",
                'options': ["Jane Austen", "William Shakespeare", "F. Scott Fitzgerald", "George Orwell"],
                'correct_answer': "Jane Austen",
                'value': 7  # Moderate question
            },
            {
                'question': "Which country is known for the Taj Mahal?",
                'options': ["India", "Egypt", "China", "Brazil"],
                'correct_answer': "India",
                'value': 6  # Moderate question
            },
            {
                'question': "What is the capital city of Australia?",
                'options': ["Sydney", "Melbourne", "Canberra", "Perth"],
                'correct_answer': "Canberra",
                'value': 6  # Moderate question
            },
            {
                'question': "What is the largest ocean on Earth?",
                'options': ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
                'correct_answer': "Pacific Ocean",
                'value': 8  # Moderate question
            },
            {
                'question': "Who painted the Mona Lisa?",
                'options': ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"],
                'correct_answer': "Leonardo da Vinci",
                'value': 7  # Moderate question
            },
            {
                'question': "Which scientist developed the theory of relativity?",
                'options': ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "Marie Curie"],
                'correct_answer': "Albert Einstein",
                'value': 9  # Difficult question
            },
            {
                'question': "What is the largest mammal in the world?",
                'options': ["Blue whale", "Elephant", "Giraffe", "Lion"],
                'correct_answer': "Blue whale",
                'value': 10  # Difficult question
            },
            {
                'value': 1,
                'question': "What is the capital of the UK?",
                'correct_answer': "London",
                'options': ["Berlin", "Paris", "London", "Neptune"]
            },
            {
                'value': 2,
                'question': "What is a Kilt",
                'correct_answer': "A garment resembling a wrap-around knee-length skirt",
                'options': [
                "A type of dagger",
                "A Japanese term for a plummer",
                "A type of dog",
                "A garment resembling a wrap-around knee-length skirt"
                ],
            },
            {
                'value': 3,
                'question': "How many sides does an octagon have?",
                'correct_answer': "8",
                'options': ["6", "8", "9", "10"],
            },
            {
                'value': 4,
                'question': "What is a trowel?",
                'correct_answer': "A tool used in gardening",
                'options': [
                "An old spelling of troll",
                "A mixture used in plastering",
                "A type of robe",
                "A tool used in gardening"
                ],
            },
            {
                'value': 5,
                'question': "In darts what is a slang term for hitting a double 3?",
                'correct_answer': "Basement",
                'options': ["Six O'Clock Rock", "Basement", "Bed end", "A Clock Fall"],
            },
            {
                'value': 6,
                'question': "What is pyrography?",
                'correct_answer': "A way of decorating materials through burn marks",
                'options': [
                "An early way of studying the sun",
                "An ancient form glass blowing",
                "An Incan dance",
                "A way of decorating materials through burn marks"
                ],
            },
            {
                'value': 7,
                'question': "What is a peanut classified as?",
                'correct_answer': "A legume",
                'options': ["A legume", "A nut", "A herb", "A fruit"],
            },
            {
                'value': 8,
                'question': "In computer science what is a nibble?",
                'correct_answer': "4 bits",
                'options': [
                "An early slang term for a cable failure",
                "A form of low level programming language",
                "4 bits",
                "An unsolvable problem"
                ],
            },
            {
                'value': 9,
                'question': "How many official languages does Switzerland have?",
                'correct_answer': "4",
                'options': ["3", "4", "5", "7"],
            },
            {
                'value': 10,
                'question': "What was the nationality of the ancient Greek figure 'Polydamna'",
                'correct_answer': "Egyptian",
                'options': ["Egyptian", "Greek", "Dorian", "Persian"],
            },
            {
                'value': 11,
                'question': "How many handles does a tyg drinking vessel usually have",
                'correct_answer': "3",
                'options': ["1", "2", "3", "0"],
            },
            {
                'value': 12,
                'question': "Who was the mother of King Edward II of England",
                'correct_answer': "Isabella of France",
                'options': [
                "Eleanor Countess of Ponthieu",
                "Jean d'Armagnac",
                "Violant of Bar",
                "Isabella of France"
                ],
            },
            {
                'value': 13,
                'question': "Where was the RSPB first established",
                'correct_answer': "Manchester",
                'options': ["London", "Manchester", "Oxford", "Norwich"],
            },
            {
                'value': 14,
                'question': "How many Apollo space missions did NOT make it to the moon?",
                'correct_answer': "11",
                'options': ["9", "10", "11", "12"],
            },
            {
                'value': 15,
                'question': "In which Abbey is 11th Century Nobleman Eadulf Rus burried?",
                'correct_answer': "Jedburgh",
                'options': ["Jedburgh", "Melrose", "Holyrood", "Hexham"],
            }
        ]

    def start(self):
        greetings = input('Welcome to the contest! Do you want to join the contest? Y or N: ')

        if greetings.lower() == 'y':
            print('''
                Thanks for joining. There will be 10 questions and 
                each question will have different points according to question difficulty level, 
                the points of the questions will be displayed
            ''')
            self.status = True
        elif greetings.lower() == 'n':
            print('''
               Don't worry! we will be around if you change your mind :)
            ''')
        else:
            input('Your request is not recognized.')

    def ask_questions(self, questions):
        total_points = 0
        for question in questions:
            print(question['question'])
            print(f"This question is worth {question['value']} points")
            for i, option in enumerate(question['options']):
                print(f"{i+1}) {option}")

            user_response = input("Type the number of your choice: ")

            while user_response not in ['1','2','3','4']:
                print("That is not a valid answer")
                user_response = input("Type the number of your choice: ")
            if user_response == str(question['options'].index(question['correct_answer']) + 1):
                total_points += question['value']
                print("Correct!")
                print(f"Your total is now {total_points}")
            else:
                print("Incorrect!")
                print(f"The correct answer was option: {str(question['options'].index(question['correct_answer']) + 1)}")
                print(f"Your total is currently {total_points} points")
        print("Quiz completed!")
        print(f"Your total is: {total_points} points\nCongratulations!")
    
    def run(self):    
        while self.status:
            self.ask_questions(self.questions)
            self.status = False

contest = Contest()
contest.start()
contest.run()
