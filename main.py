# File: main.py
# Author: Taylor Johnson
# Date: 2021.4.27
#
# Description: Creates functions that can read from 
# a text file and also creates the programs output.

from searchtree import Search_tree

def readfile(x, file_name):
    """ Read the file that the user inputs. """
    
    with open(file_name,'r') as f:

        for a_line in f:
            
            for a_word in a_line.split():

                x.insert(a_word)

def program_output():
    """ Output the program so it easy for the user to use. """

    x = Search_tree()

    print()

    print("Search Tree Word Count:")

    print()

    print('This word count program will read the words from a file inserted by the user.')
    print('and will  input the words in lexographic order and the number of times the')
    print('word was in the file.')

    print()

    file_name = input("Insert file name: ")

    print()

    readfile(x, file_name)
    x.traverse()

    print()

    print("Total Words Processed: ",x.tally())

    print()

    print("Total Words Counted: ",x.total_tally())

    print()

    user_question = input("Would you like to insert another file? (Yes/No): ")

    if user_question == "Yes":
        program_output()
        
    elif user_question == "yes":
        program_output()

    else:
        print()
        print('Goodbye!')
        print()


def main():
    """ Run the program. """

    program_output()

main()