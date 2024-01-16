import web_scrap_words as scrap
import random

used_alphabets = set()

def get_random_word(index, data):
    word_list = data['props']['pageProps']['allGames'][index].get("words")
    if word_list:
        random_index = random.randint(0, len(word_list) - 1)
        return word_list[random_index]
    else:
        print(f"No words found for the selected game (index {index}).")
        return None

def display_word(random_word, correct_guesses):
    displayed_word = ""
    for letter in random_word:
        if letter in correct_guesses:
            displayed_word += f"{letter} "
        else:
            displayed_word += "_ "
    return displayed_word.strip()

def play_game(index, data):
    random_word = get_random_word(index, data).lower()
    correct_guesses = set()
    main_word = set(random_word)
    chances = len(random_word) + 1
    
    print(f"\t\nGuess the word. You will have {chances} chances! \n")
    for i in range(len(random_word)):
        print("_ ", end="")
    print("\n")

    while True:
        try:
            user_guess = input("Enter your guess alphabet: ").lower()

            if user_guess not in used_alphabets:
                used_alphabets.add(user_guess)

                if user_guess in random_word:
                    correct_guesses.add(user_guess)
                    print(f"\nThere is '{user_guess}' in word.\n")

                else:
                    chances -= 1
                    print(f"\nThere is no '{user_guess}'.")
                
                print(f"You have {chances} {'chances' if chances > 1 else 'chance'} left! \n")

                displayed = display_word(random_word, correct_guesses)
                print(f"{displayed}")
                    
                if chances == 0:
                    print(f"\nYou failed to guess the word: {random_word}")
                    break
                
                if correct_guesses == main_word:
                    print("\nCongratulations! You guessd the word correctly.\n")
                    break
                
                print(f"\nUsed alphabets: {used_alphabets}\n")

            else:
                print(f"\n{user_guess} already used.\n")
            
        except Exception as e:
            print(f"Error: {e} \n")

def show_game_options(data):
    game_options = data['props']['pageProps']['allGamesNav']
    for index, item in enumerate(game_options, start=1):
        print(f"{index}. {item['h1']:<20}", end="")
    print()
    while True:
        user_mode_choice = int(input("\nEnter the number of corresponding option: "))
        if 1 <= user_mode_choice <= len(game_options):
            return user_mode_choice - 1
        else:
            print("Invalid number!")
    

if __name__ == '__main__':
    json_data = scrap.web_scrap_json_data()
    while True:
        print("\n\t\t\t\tWelcome to Hangman Game\n\t\t\tChoose one of the option below to play game \n")
        index_user_mode_choice = show_game_options(json_data)
        play_game(index_user_mode_choice, json_data)
        play_again = input("\nWant to play again? (y or n): ")
        if play_again != 'y':
            break
        used_alphabets = set()
