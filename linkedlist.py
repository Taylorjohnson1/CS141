# File: linkedlist.py
# Author: Taylor Johnson
# Date: 2021.4.11
# Description: Creates the Linked list class that can search, 
#              insert and delete different nodes within the list.
#              Also creates Linked list node that formats the print.

class Linked_list():
    """ Linked list connects all of the nodes together within the list. """

    def __init__(self):
        """ Initialize whats being pointed to first.

        Parameters:
        head:          What is being pointed to first.

        """
        
        self.head = None

    def print(self):
        """ Print out all of the nodes. """

        p = self.head

        while p != None:
            p.print()
            p = p.next

    def insert(self, a_word = None, a_count = 1):
        """ Insert the node into the list. """

        p = self.head
        q = None
        done = False
    
        while not done:

            # If head points to nothing, then it will move on.
            if self.head == None:
                self.head = Linked_list_node(a_word, a_count)
                done = True
                
            # If p points to nothing, then it will move on.
            elif p == None:
                q.next = Linked_list_node(a_word, a_count)
                done = True

            # Check to see if the two words are the same. 
            # If they are, then will add one to the count.
            elif a_word == p.word:
                p.count += 1
                done = True

            # Check to see if the word is less than or equal to the word within
            # the Linked list.
            elif a_word <= p.word:

                # Move pointer from one node to another node.
                if p == self.head:
                    w = Linked_list_node(a_word, a_count)
                    w.next = self.head
                    self.head = w
                    done = True

                # Move pointer from one node to another node.
                else:
                    w = Linked_list_node(a_word, a_count)
                    w.next = q.next
                    q.next = w
                    done = True

            # Set q equal to p and then moves to the next node.
            else:
                q = p
                p = p.next

    def delete(self, a_word):
        """ Delete the node from the list if there are 2 words that are the same. """

        p = self.head
        q = None
        done = False

        while not done:

            # If head points to nothing, then it will move on.
            if self.head == None:
                done = True

            # If p points to nothing, then it will move on.
            elif p == None:
                done = True

            # If there are two of the same words, then it will point to the next
            # node and forget about the other one.
            elif a_word == p.word:

                # If the p and head are both pointing to the same node.
                # it will point to the next node.
                if p == self.head:
                    self.head = p.next
                    done = True

                else:
                    q.next = p.next
                    done = True

            else:
                q = p
                p = p.next

    def search(self, a_word):
        """ Search for words within the list and """

        p = self.head
        q = None
        done = False
        favorite_word = False

        while not done:

            # If head points to nothing, then it will move on.
            if self.head == None:
                done = True

            # If p points to nothing, then it will move on.
            elif p == None:
                done = True

            # Check for the users favorite word.
            elif a_word == p.word:
                favorite_word = True
                done = True

            else:
                q = p
                p = p.next

        return favorite_word

    def distinced_words(self):
        """ Count the distinced number of word within the list. """

        p = self.head
        sum = 0

        while p != None:
            sum = sum + 1
            p = p.next

        return sum

    def total_words(self):
        """ Count the total number of word within the list. """

        p = self.head
        sum = 0

        while p != None:
            sum = sum + p.count
            p = p.next

        return sum

class Linked_list_node():
    """  """

    def __init__(self, a_word = None, a_count = 0):
        """ Initialize the variables for the node.

        Parameters:
        word:          Keeps track of the different words.
        count:         Counts the number of times the word has beed used.
        next:          Moves pointer to the next node.

        """ 
        
        self.word = a_word
        self.count = a_count
        self.next = None

    def print(self):
        """ Print and formates the differnet nodes. """

        print('{:15s} {:15d}'.format(self.word, self.count))
