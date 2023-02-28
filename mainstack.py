# File: mainstack.py
# Author: Taylor Johnson
# Date: 3/27/2021
# Description: Creates functions that translate the expressions to infix to 
#              postfix and sets up the output of the program.

from stack import Stack
from stack import Peek_Stack

def precedence(operator):
    """ Set precedences to an operators. """ 

    result = 0 

    if operator == '(':
        result = 0

    elif operator == '+':
        result = 1

    elif operator == '-':
        result = 1

    elif operator == '*':
        result = 2

    elif operator == '/':
        result = 2

    elif operator == '^':
        result = 3

    return result

def translate(infix_expr):
    """ Convert infix expression to postfix expression. """

    op_stack = Peek_Stack(100)
    postfix_expr = ''

    for infix_char in infix_expr:

    # Checks to see if the charactor is a digit between 0 and 9.
        if infix_char in "0123456789":
            postfix_expr += infix_char

        # Checks for charactor within the infix expression and then pushes it.
        if infix_char == "(":
            op_stack.push(infix_char)

        # Checks for charactor within the infix expression and then pops it out.
        if infix_char == ")":
            while op_stack.peek() != "(":
                postfix_expr += op_stack.pop()   
            op_stack.pop() 

        # Determains weither or not the infix charactor is left associative.
        if infix_char in ('+-*/'):

        # Checks to see if the storage is empty. If not, it pushes the charactor into storage.
            if op_stack.is_empty():
                op_stack.push(infix_char)

            # Checks to see if the charactors precedence in the storage is greater than or equal to the presidence of the charactor.
            else:
                while not op_stack.is_empty() and precedence(op_stack.peek()) >= precedence(infix_char):
                    postfix_expr += op_stack.pop()
                op_stack.push(infix_char)

        # Determains weither or not the infix charactor is right associative.
        if infix_char in ('^'):

            # Checks to see if the storage is empty. If not, it pushes the charactor into storage.
            if op_stack.is_empty():
                op_stack.push(infix_char)

            else:

                # Checks to see if the charactors precedence in the storage is greater than or equal to the presidence of the charactor.
                while not op_stack.is_empty() and precedence(op_stack.peek()) > precedence(infix_char):
                    postfix_expr += op_stack.pop()
                op_stack.push(infix_char)
            
        # Checks to see if the charactor is a space.
        if infix_char == " ":
            pass

    # If the next output slot is empty, move storage to next output slot.
    while not op_stack.is_empty():
        postfix_expr += op_stack.pop()

    return postfix_expr

def loop_question():
    """ Loop through so user can input multiple expressions. """

    user_input = input("Would you like to enter another expression? Yes or No? ")
    
    if user_input == "Yes":
        do_user_input()

    elif user_input == "No":
        print()
        exit

def do_user_input():
    """ Take user input data and turns infix expressions into postfix expression. """

    print()
    print("Infix Expression to Postfix Expression:")
    print()

    infix_expr = input('Enter Infix Expression: ')

    print()
    print('Users Infix Expression:', infix_expr)

    postfix_expr = translate(infix_expr)

    print()
    print("Postfix Expression:", postfix_expr)
    print()

    loop_question()

    print()
    
def do_file_input():
    """ Take users infix expression from text file and transfers the expression into postfix expression. """

    print()
    print("Infix Expression to Postfix Expression:")
    print()

    test_file_name = input('Enter Test File Name: ')

    print()
    print('File Name Tested:', test_file_name)
    print()

    with open(test_file_name) as f:

        for infix_expr in f:
            infix_expr.rstrip('\n')
            postfix_expr = translate(infix_expr)

            print("Infix Expression:", infix_expr)
            print("Postfix Expression:", postfix_expr)
            print()
            

def main():
    """ Call and run the different functions. """

    do_user_input()
    
main()