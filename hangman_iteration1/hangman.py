#TIP: use random.randint to get a random word from the list
import random


def read_file(file_name):
    """
    open file and read lines as words
    """
    file = open(file_name,"r")
    arr = file.readlines()
    return arr


def select_random_word(words):
    """
    select random word from list of file
    """
    index = random.randint(0,len(words) - 1)
    word_list =list(words[index])
    word_list_index = random.randint(0,len(word_list)-2)
    print("Guess the word: ",end="")
    for i in range(len(word_list)):
        word_list[word_list_index] = '_'
        print( word_list[i],end="")
    
    return words[index]


def get_user_input():
    """
    get user input for answer
    """
    user_input = input("\n" + "Guess the missing letter: ")
    return user_input


def run_game(file_name):
    """
    This is the main game code.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: '+word)


if __name__ == "__main__":
    run_game('short_words.txt')

 
