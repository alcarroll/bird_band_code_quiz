import random
import csv

# Start quiz function
def start_quiz():
    print("Welcome to the bird band quiz!")
    print("Generating answers...")
    generate_answers()

# Generate correct answer function
def generate_answers():
    # Select correct answer and add to the possible answers list
    game_species = random.choice(full_species_data)
    correct_answer_species = game_species[1]
    correct_answer_banding_code = game_species[0]
    possible_answers = [correct_answer_banding_code]

    # Grab random incorrect entries from the full species data
    wrong_answer_count = 0
    while wrong_answer_count <= 2:
        new_multiple_choice_answer = random.choice(full_species_data)
        wrong_answer = (new_multiple_choice_answer[0])
        possible_answers.append(wrong_answer)
        wrong_answer_count += 1

    # Randomize answer order
    random.shuffle(possible_answers)

    # Call prompt for answer function
    answer_prompt(correct_answer_banding_code,correct_answer_species,possible_answers)

# Prompt for answer function
def answer_prompt(correct_answer_banding_code,correct_answer_species,possible_answers):
    print (f"\n\nWhat is the banding code for " + correct_answer_species + "?\n")
    print(f"A: " + possible_answers[0])
    print(f"B: " + possible_answers[1])
    print(f"C: " + possible_answers[2])
    print(f"D: " + possible_answers[3])
    player_answer = input("\nYour answer: ")
    check_answer(correct_answer_banding_code,possible_answers,player_answer)

# Check answer function
def check_answer(correct_answer,possible_answers,player_answer):
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
    print("\n\nWould you like to play again?")
    play_again = input("Y/Yes N/No\n")
    if play_again.lower() == "y" or play_again.lower() == "yes":
        generate_answers()
    elif play_again.lower() == "n" or play_again.lower() == "no":
        exit()
    else:
        print("Invalid selection. Exiting.")
        exit()


# Populate full_species_data list with data from bird_info.csv file
file = open("bird_info.csv", "r")
full_species_data = list(csv.reader(file, delimiter=","))
file.close()

start_quiz()



