# File: searchtree.py
# Author: Taylor Johnson
# Date: 2021.4.27
#
# Description: Creates the Search_tree class and also the Search_tree_node class. 
# Search tree deals with sorting and count the nodes so the nodes can
# be put into order alphabetically. While the search tree node keeps
# track of everything that is inside the node.
#
# Usage:
# from searchtree import Search_tree

class Search_tree():
    """ Connect all of the nodes together within the list. """ 

    def __init__(self):
        """ Create the parameters for the Search_tree.

        Usage:
        root:          Root points the the node at the top of the tree.
        count:         Counts the number of times the word has beed used.
        """

        self.root = None
        self.count = 0

    def traverse(self):
        """ Start the recursion for the traverse. """

        self.traverse_r(self.root)

    def traverse_r(self, ptr):
        """ Traverse the subtree rooted at ptr. """

        # Use recursion to cycle throught the tree.
        if ptr:
            self.traverse_r(ptr.left)
            ptr.print()
            self.traverse_r(ptr.right)

    def insert(self, a_word):
        """ Start the recursion for the insert. """ 
    
        self.insert_r(self.root, a_word)

    def insert_r(self, ptr, a_word = None):
        """ Inserts a node in a binary search tree rooted ptr. """

        # Pointer isn't pointing to anything, then move on to the next node.
        if self.root is None:
            w = Search_tree_node(a_word)
            self.root = w
        
        # Count the number of time a word has been used.
        elif a_word == ptr.word:
            ptr.count += 1

        # Move the pointer from one node onto the next.
        elif a_word < ptr.word:
            if ptr.left is None:
                w = Search_tree_node(a_word)
                ptr.left = w

            else:
                self.insert_r(ptr.left, a_word)

        # Move the pointer from one node onto the next.
        else:
            if ptr.right is None:
                w = Search_tree_node(a_word)
                ptr.right = w

            else:
                self.insert_r(ptr.right, a_word)

    def tally(self):
        """ Start the recursion for the tally of the nodes within the tree. """
        
        return self.tally_r(self.root)

    def tally_r(self, ptr):
        """ Count the number of nodes within the tree rooted at ptr. """ 

        if ptr is None:
            return 0
        else:
            return self.tally_r(ptr.left) + 1 + self.tally_r(ptr.right)

    def total_tally(self):
        """ Start the recurstion for the total tally of the words. """
        
        return self.total_tally_r(self.root)

    def total_tally_r(self, ptr):
        """ Count the total number of words. """ 

        if ptr is None:
            return 0

        else:
            return self.total_tally_r(ptr.left) + ptr.count + self.total_tally_r(ptr.right)

class Search_tree_node():
    """ """

    def __init__(self, a_word):
        """ Create the parameters for the Search_tree_node.

        Parameters:
        a_word         - The word withing the node.

        Usage:
        word:          - Keeps track of the different words.
        left:          - Left side of the search tree.
        right:         - Right side of the search tree.
        count:         - Counts the number of time the word is in the list.
        """

        self.word = a_word
        self.left = None
        self.right = None
        self.count = 1

    def print(self):
        """ Print and formates the differnet nodes. """

        print('{:15s} {:15d}'.format(self.word, self.count))
