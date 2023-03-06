import pyttsx3
from Daemon import run_daemon
from Jarvis import run_jarvis
from Curie import run_curie

# Set up pyttsx3 engine
engine = pyttsx3.init()

# Define the different outcomes as a list of tuples
options = [("Run Daemon", lambda: run_daemon(engine)), 
           ("Run Jarvis", lambda: run_jarvis(engine)),
           ("Run Jarvis-.", lambda: run_curie(engine)),
           ("You chose option 3.", lambda: print("You chose option 3."))]

while True:
    user_input = input("Enter gpt for ai: ")
    if user_input in ['g', 'gp', 'gpt']:
        option = input("Choose ai profile (1-3): ")
        # Use a dictionary to map the user's input to the appropriate outcome
        outcomes = {"0": options[0], "1": options[1], "2": options[2], "3": options[3]}
        if option in outcomes:
            outcome = outcomes[option]
            print(outcome[0])
            outcome[1]()  # Call the corresponding function with the pyttsx3 engine
        else:
            print("Invalid option. Please try again.")
    else:
        print("Invalid input. Please try again.")
