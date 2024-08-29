import random
import csv

def start_quiz():
    """Welcome message and game mode selection"""
    # Welcome message and mode prompt
    print("\nWelcome to the bird band quiz!")
    print("\nPlease select a game mode:\n 1: Guess species name from banding codes\n "
          "2: Guess banding codes from species names")
    game_mode = input("\nGame mode selection: ")
    # Entering letters causes validation issues but the variable needs to be an int in generate_answers()
    # there's probably a better workaround than this - possibly set it as a string everywhere else?
    game_mode = str(game_mode)
    if game_mode == "1":
        print("Species guess mode enabled!")
        generate_answers(game_mode)
    elif game_mode == "2":
        print("Banding guess mode enabled!")
        generate_answers(game_mode)
    else:
        print("Invalid selection, please try again")
        start_quiz()
    # Setting game mode back to int because kludge
    game_mode = int(game_mode)
    generate_answers(game_mode)

def generate_answers(game_mode):
    """Generate correct and incorrect answers."""
    # Generate correct answers
    game_species = random.choice(full_species_data)
    correct_species_answer = game_species[1]
    possible_species_answers = [correct_species_answer]
    correct_banding_answer = game_species[0]
    possible_banding_answers = [correct_banding_answer]

    # Grab random incorrect entries from the full species data
    wrong_species_answer_count = 0
    while wrong_species_answer_count <= 2:
        new_species_answer = random.choice(full_species_data)
        possible_species_answers.append(new_species_answer[1])
        wrong_species_answer_count += 1

    wrong_banding_answer_count = 0
    while wrong_banding_answer_count <= 2:
        new_banding_answer = random.choice(full_species_data)
        possible_banding_answers.append(new_banding_answer[0])
        wrong_banding_answer_count += 1

    # Randomize answer orders
    random.shuffle(possible_species_answers)
    random.shuffle(possible_banding_answers)

    # Call prompt for answer function
    if game_mode == 1:
        species_answer_prompt(correct_species_answer, correct_banding_answer, possible_species_answers, game_mode)
    elif game_mode == 2:
        banding_answer_prompt(correct_species_answer, correct_banding_answer, possible_banding_answers, game_mode)

def species_answer_prompt(correct_species_answer, correct_banding_answer, possible_species_answers, game_mode):
    """Displaying possible answer options and collecting user's answer for species mode"""
    # Species mode answer output
    print(f"\n\nWhat is the species that uses this banding code: " + correct_banding_answer + "?\n")
    print(f"A: " + possible_species_answers[0])
    print(f"B: " + possible_species_answers[1])
    print(f"C: " + possible_species_answers[2])
    print(f"D: " + possible_species_answers[3])
    # Set variables to be passed to universal check answer function
    player_answer = input("\nYour answer: ")
    correct_answer = correct_species_answer
    possible_answers = possible_species_answers
    check_answer(player_answer, correct_answer, possible_answers, game_mode)

def banding_answer_prompt(correct_species_answer, correct_banding_answer, possible_banding_answers, game_mode):
    """Displaying possible answer options and collecting user's answer for banding mode"""
    # Banding mode answer output
    print(f"\n\nWhat is the banding code for this species: " + correct_species_answer + "?\n")
    print(f"A: " + possible_banding_answers[0])
    print(f"B: " + possible_banding_answers[1])
    print(f"C: " + possible_banding_answers[2])
    print(f"D: " + possible_banding_answers[3])
    # Set variables to be passed to universal check answer function
    player_answer = input("\nYour answer: ")
    correct_answer = correct_banding_answer
    possible_answers = possible_banding_answers
    check_answer(player_answer, correct_answer, possible_answers, game_mode)

def check_answer(player_answer, correct_answer, possible_answers,game_mode):
    """Evaluating answers and displaying results then prompting for additional play options"""
    # Evaluating answer and outputting result
    if player_answer.lower() == "a" and possible_answers[0] == correct_answer:
        print("Correct!")
    elif player_answer.lower() == "b" and possible_answers[1] == correct_answer:
        print("Correct!")
    elif player_answer.lower() == "c" and possible_answers[2] == correct_answer:
        print("Correct!")
    elif player_answer.lower() == "d" and possible_answers[3] == correct_answer:
        print("Correct!")
    else:
        print(f"Nope! The correct answer was: " + correct_answer)

    # Prompt to play again
    play_again_prompt(game_mode)

def play_again_prompt(game_mode):
    """Prompt to play again. Used as a separate function to allow for error handling"""
    print("\n\nWould you like to play again?")
    play_again = input("y = yes\nn = no\nc = change mode\n:")
    if play_again.lower() == "y" or play_again.lower() == "yes":
        generate_answers(game_mode)
    elif play_again.lower() == "c" or play_again.lower() == "change":
        start_quiz()
    elif play_again.lower() == "n" or play_again.lower() == "no":
        print("Goodbye and happy birding!")
        exit()
    else:
        print("Invalid selection, please try again.")
        play_again_prompt()

# Populate full_species_data list with data from bird_info.csv file
file = open("bird_info.csv", "r")
full_species_data = list(csv.reader(file, delimiter=","))
file.close()

# Call start quiz function
start_quiz()