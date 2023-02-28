# File: stack.py
# Author: Taylor Johnson
# Date: 3/27/2021
# Description: Makes different classes and function that helps translate the infix
#              expression to postfix expressions.

from csarray import Array

class Stack(Array):
    """ Create different fuctions that can help translate infix expressions to postfix expressions. """ 
    
    def __init__(self, size, default_value = None):
        """ ___init___() creates the stack object. """

        super().__init__(size, default_value)

        self.top = -1 

    def push(self, push_op):
        """ Push infix charactor into the storage. """

        self.top = self.top + 1
        self.data[self.top] = push_op

    def pop(self):
        """ Pop infix charactor out of storage. """

        temp = self.data[self.top]
        self.top = self.top - 1
        return temp
        
    def is_empty(self):
        """ Check to see if storage is empty. """

        return(self.top == -1)

class Peek_Stack(Stack):
    """ Create a function that is easier to take the operator out of storage. """

    def __init__(self, size, default_value = None):
        """ ___init___() creates the peek_stack object. """

        super().__init__(size, default_value)   

    def peek(self):
        """ Return the last operator in the storage. """ 

        temp = self.pop()
        self.push(temp)
        return temp