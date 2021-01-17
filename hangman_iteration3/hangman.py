import random
import sys

def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()


def get_user_input():
    return input('Guess the missing letter: ')


def ask_file_name():
    file_name = input("Words file? [leave empty to use short_words.txt] : ")
    if not file_name:
        return 'short_words.txt'
    return file_name


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    return word


# TODO: Step 1 - update to randomly fill in one character of the word only
def random_fill_word(word):
    word = list(word) #converting word to list
    list_dashes = [ "_" for i in range(len(word)) ]
    index = random.randint(0,len(word)-1)
    list_dashes[index] = word[index]
    updated = ""
    for i in range(len(list_dashes)):
        updated += list_dashes[i]
    return updated



# TODO: Step 1 - update to check if character is one of the missing characters
def is_missing_char(original_word, answer_word, char):
    answer_word = list(answer_word)
    original_word = list(original_word)
    for i in range(len(original_word)-1):
        if answer_word[i] == original_word[i]:
            if len(original_word) == 1:
                pass
            else:
                del original_word[i]
                continue
        elif char in original_word:
            return True
    return False


# TODO: Step 1 - fill in missing char in word and return new more complete word
def fill_in_char(original_word, answer_word, char):
    original_word = list(original_word)
    answer_word = list(answer_word)
    new = ""
    for i in range(len(original_word)):
        if original_word[i] == char:
            answer_word[i] = char
    for i in range(len(answer_word)):
            new += answer_word[i]
    return new 


def do_correct_answer(original_word, answer, guess):
    answer = fill_in_char(original_word, answer, guess)
    print(answer)
    return answer


# TODO: Step 4: update to use number of remaining guesses
def do_wrong_answer(answer, number_guesses):
    print('Wrong! Number of guesses left: '+str(number_guesses))
    if number_guesses < 5:
        draw_figure(number_guesses)

      

# TODO: Step 5: draw hangman stick figure, based on number of guesses remaining
def draw_figure(number_guesses):
    a = [["{}{}{}".format("/----","\n|   0\n|  /|\\\n|   |\n|  / \\\n","_______")],
     ["{}{}{}".format("/----","\n|   0\n|  /|\\\n|   |\n|\n","_______")],
     ["{}{}{}".format("/----","\n|   0\n|  /|\\\n|\n|\n","_______")],
     ["{}{}{}".format("/----","\n|   0\n|\n|\n|\n","_______")],
     ["{}{}{}".format("/----","\n|\n|\n|\n|\n","_______")]
     ]
    print(a[number_guesses][0])
    return 
# TODO: Step 2 - update to loop over getting input and checking until whole word guessed
# TODO: Step 3 - update loop to exit game if user types `exit` or `quit`
# TODO: Step 4 - keep track of number of remaining guesses
def run_game_loop(word, answer):
    print("Guess the word: "+answer)
    guesses = 4
    while word != answer:
        guess = get_user_input()
        if is_missing_char(word, answer, guess):
            answer = do_correct_answer(word, answer, guess)
        elif guess == "exit" or guess == "quit":
            print("Bye!")
            break
        elif guesses > 0:
            do_wrong_answer(answer, guesses)
            guesses -= 1
        else:
            do_wrong_answer(answer,0)
            print("Sorry, you are out of guesses. The word was: " + word)
            break
    return
            
    
  


# TODO: Step 6 - update to get words_file to use from commandline argument
if __name__ == "__main__":
    try:
        if len(sys.argv) == 2:
            words_file = sys.argv[1]
        elif len(sys.argv)-1 == 0:
            words_file = ask_file_name() 
        words = read_file(words_file)
        selected_word = select_random_word(words)
        current_answer = random_fill_word(selected_word)

        run_game_loop(selected_word, current_answer)
    except FileNotFoundError:
        print("file not found")

