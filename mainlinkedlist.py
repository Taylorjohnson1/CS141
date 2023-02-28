# File: linkedlist.py
# Author: Taylor Johnson
# Date: 2021.4.11
# Description: Creates the read file function so it can read the users
#              file. Also creates the programs output so it's looks
#             more user friendly.

from linkedlist import Linked_list

def readfile(x, file_name):
    """ Read the file that the user inputs. """
    
    with open(file_name,'r') as f:

        for a_line in f:
            
            for a_word in a_line.split():

                x.insert(a_word)

def program_output():
    """ Output the program so it easy for the user to use. """

    x = Linked_list()

    print()

    print('Singly-Linked List Word Count:')

    print()

    print('This word count program will read the words from a file inserted by the user.')
    print('and will  input the words in lexographic order and the number of times the')
    print('word was in the file.')

    print()

    file_name = input("Insert file name: ")

    print()

    users_word = input("What's your favorite word?: ")

    print()

    readfile(x, file_name)
    x.delete("a")
    x.delete("an")
    x.delete("and")
    x.delete("the")
    x.print()
    
    print() 

    print("Total Number of Distinced Words:", x.distinced_words())

    print()

    print("Total Numbers of Words:", x.total_words())

    print()

    if x.search(users_word):
        print('Your favorite word "{}" is in the list.'.format(users_word))
        print()

    else:
        print('Your favorite word "{}" is not in the list.'.format(users_word))
        print()

    user_question = input("Would you like to insert another file? (Yes/No): ")

    if user_question == "yes":
        program_output()

    elif user_question == "Yes":
        program_output()

    else:
        print()
        print('Goodbye!')
        print()

def main():
    """ Run the program. """

    program_output()

main()