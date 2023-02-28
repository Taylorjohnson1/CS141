# csarray.py
# Don Sylwester
# 2016.01.13
# This file defines an Array class with the usual behaviors
# of an array.
#
# Usage
# from csarray import Array

class Array(object):
    """ Implement an Array object with fixed size

    The array class supports setting and getting values from
    the array with zero-based indexing.
    """

    # Instance variables (private)
    # data holds the elements of the array
    # size number of elts in the array

    def __init__(self,size,default_value=None):
        """__init()__ creates an Array object

        Parameters
        size               Number of elects in the array
        default_value      The array is initialized to the default value

        Usage
        a = Array(10)
        a[4] = 3 + a[5]
        b = len(a)
        for i in a ...
        """

        self.data = list()
        self.size = size
        self.default_value = default_value
        self.data = [default_value for i in range(size)]

        # Alternate method to initialize the array contents
        # for i in range(size):
        #   self.data.append(default_value)

    def __setitem__(self,index,new_value):
        """ Set the datum with subscript index to new_value. """
        self.data[index] = new_value

    def __getitem(self,index):
        """ Retrieve the datum with subscript index. """
        return self.data[index]

    def __len__(self):
        """ Return the number of datums in data. """
        return len(self.data)

    def __iter__(self):
        """ Return an iterator for the array. """
        return iter(self.data)
