status = False  

greetings = input('Welcome to the contest! Do you want to join the contest? Y or N  : ' )

if greetings.lower() == 'y':
    print('''
        Thanks for joining. There will be 10 questions and each questions will have different points, 
        the points of the questions will be displayed
    ''')
    status = True
elif greetings.lower() == 'n':
    print('''
       Don't worry! we will be around if you change your mind:)
    ''')
else:
    input('Your request is not recognised.')



def ask_questions(questions):
    total_points = 0
    for question in questions:
            print(question['question'])
            for i, option in enumerate(question['options']):
                print(f"{i+1}) {option}")

            user_response = input("Type the number of your choice : ")
            if user_response ==str(question['options'].index(question['correct_answer']) + 1):
                total_points += question['value']
                print("Correct!")
            else:
                print("Incorrect!")
    print("Contest completed!")
    print(f"You got: {total_points} points")


questions = [
    {
        'question': "What is the chemical symbol for gold?",
        'options': ["Au", "Ag", "Fe", "Cu"],
        'correct_answer': "Au",
        'value': 3  # Easy question
    },
    {
        'question': "Which planet is closest to the Sun?",
        'options': ["Mars", "Venus", "Jupiter", "Mercury"],
        'correct_answer': "Mercury",
        'value': 5  # Easy question
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
    }
]

while status:
    ask_questions(questions)
    status = False