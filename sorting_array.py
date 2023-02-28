# File: sorting_array.py
# Author: Taylor Johnson
# Date: 2021.1.25
# Description: Creates sorting array and has different
#              function that describes sorts, fill and
#              print throughout the class.

from csarray import Array
import random

COLUMN_PER_ROW = 10
FIRST_RANDOM_NO = 1
LAST_RANDOM_NO = 101

class Sorting_array(Array):
    """ Create different fuctions that can sort arrays differently. Also has different
    fill statement that can generate random numbers, increase by one, decrease by one 
    and stay the same.
    """

    def __init__(self, size, default_value = None):
        """ __init__() create an Array Object.

        Parameters
        size              - Number of elements in the array.
        default_value     - The array is initialized to the default value.

        """

        super().__init__(size, default_value)

        self.before_sum = 0
        self.before_sum_sq = 0
        self.after_sum = 0
        self.after_sum_sq = 0

    def fill(self):
        """ Fill the array with random integers. """

        for i in range(self.size):

            self.data[i] = random.randrange(FIRST_RANDOM_NO, LAST_RANDOM_NO)

    def increase_fill(self):
        """ Fill the array with numbers that are increasing. """

        for i in range(self.size):

            self.data[i] = i + 1

    def decrease_fill(self):
        """ Fill the array with numbers that are decreasing . """

        for i in range(1, self.size + 1):

            self.data[-i] = i

    def same_fill(self):
        """ Fill the array with numbers that stay the same. """

        same_number = 6

        for i in range(self.size):

            self.data[i] = same_number

    def print(self,message = None, columns_per_row = 10):
        """ Print out sorting array in a grid. """

        for i in range(self.size):

            # Formats the output.
            print('{:6d}'.format(self.data[i]), end = "")

            # When formating, it switches lines when the remainder is 0.
            if ((i+1) % COLUMN_PER_ROW == 0):
                print()

    def shell_sort(self):
        """ Sort random integers in order using the shell sort.

        The shell sort groups numbers together depending on the size
        of the array, and sorts the first number of every group in order from
        smallest to biggest, then the second number in each group and so on. Once
        it's finished sorting using the shell sort, it calls the insertion sort 
        and sorts the numbers one by one until the numbers are sorted from smallest
        to biggest.

        Example of Shell Sort:

        Array:
        0 1  2 3    4  5 6 7    8  9 10 11   12 13 14 15    16 17 18 19

        Random Numbers:
        9 14 4 20 | 17 3 7 19 | 13 2 18 10 | 16 5  11 12  | 15  8  1  6
        ----------------------------------------------------------------
                  |           |            |              |
        9         | 13        | 15         | 16           | 17
          2       |    3      |    5       |    8         |     14
             1    |      4    |      7     |       11     |        18
               6  |        10 |         12 |          19  |           20

        Sorted Numbers:
        9 2 1 6     13 3 4 10   15 5 7 12    16 8 11 19     17 14 18 20 
        """

        # Set space between two numbers.
        h = 1

        while (h < self.size):

            # Will group the numbers together increasing until h is bigger
            # than size of array.
            h = 3 * h + 1

        while (h > 0):

            # Will group the numbers back together and now decreasing untill
            # h is smaller than the size of array and then will do the insertion sort.
            h = (h - 1) // 3
            self.insertion_sort(h)

    def insertion_sort(self, h = 1):
        """ Sort array in order ascending order.

        Insertion sort does a decrease and conquer method that compairs two numbers and checks to
        see which number is smaller. If the first number is bigger, it takes out the second number, 
        shifts the first number over and places the second number in the first spot. 

        Example:

        | 8 - 2 | _ -> 8 | 2 - 8 |
        |    /  |     /  |       |
        |   2   |    2   |       |

        Example of Insertion Sort:

            1 2 4 5 3
                ^   |
                |   v
                3<--3

            1 2 3 4 5
        """

        for i in range(h, self.size):

            # Takes the number out of the array.
            key = self.data[i]
            j = i

            # Will switch the numbers if one number is larger.
            while j > h - 1 and self.data[j - h] > key:
                self.data[j] = self.data[j - h]
                j = j - h

            self.data[j] = key

    def heap_sort(self):
        """ A heap sort uses a binary tree which fill each and every level 
        besides the last with nodes as far as left as posible. Once it's full,
        it checks for the left and right child, if there is a right child, will will compare 
        the two and the greater child will be swaped and go up the tree. The 
        heap sort will stop when you can't swap any node.
        
        Input data: 5, 1, 11, 10, 8

                        5(0)
                       /   \
                    1(1)   11(2)
                    /   \
                10(3)    8(4)

        Applying Heap Sort:

                        11(0)
                        /  \
                    10(1)  5(2)
                    /   \
                 1(3)    8(4)
         """

        n = self.size

        for k in range((n - 2) // 2, -1, -1):
            self.downheap(n, k)
            
        for m in range(n-1, 0, -1):

            # Swap integer into a placeholder.
            swap_integers = self.data[0]
            self.data[0] = self.data[m]
            self.data[m] = swap_integers
            self.downheap(m, 0)

    def downheap(self, n, k):
        """ While going down the heap to check for the left and right child. 
        If there is a right child, it will compare the left and right child 
        and the bigger one will go up the binary tree. 
        """

        # Takes out number our of the array.
        key = self.data[k]
        is_a_heap = False

        # Checks to see if there is a child.
        while (k <= (n - 2) // 2 and not is_a_heap):

            # Points J at the left child.
            j = 2 * k + 1

            if j + 1 < n:

                #Left Child and Right Child
                if self.data[j] < self.data[j + 1]:
                    j = j + 1

            if self.data[j] > key:

                # Swaps the Children.
                self.data[k] = self.data[j]
                k = j
                    
            else:
                is_a_heap = True

        self.data[k] = key

    def quicksort(self):

        self.quicksortr(0, self.size - 1)

    def quicksortr(self, left, right):
        """ A very quick and efficient sorting algorithum that uses the 
        divid-and-conquor methoid to slipt the code up into different sections.
        
        Example:

        | 8 - 2 | _ -> 8 | 2 - 8 |
        |    /  |     /  |       |
        |   2   |    2   |       |
         """

        if (left < right):

            # Uses recurstion to loop through the partition fucntion
            p = self.partition(left, right)
            self.quicksortr(left, p - 1)
            self.quicksortr(p, right)

    def partition(self, left, right):
        """ Divide the array into sections to make the size of the array smaller and easier to sort. """

        # Pivot takes out the left number in the array.
        pivot = self.data[left]
        i = left
        j = right

        while (i <= j):

            # Checks to see if the left side is less than the pivot and then increments it by 1.
            while (self.data[i] < pivot):
                i = i + 1

            # Checks to see if the right side is greater than the pivot and then decreases it by 1.
            while (self.data[j] > pivot):
                j = j - 1

            if (i <= j):
                self.data[j],self.data[i] = self.data[i], self.data[j]
                i = i + 1
                j = j - 1

        return i

    def check_message(self):
        """ Check to see if the function is true or not and will pring out accordingly. """

        if self.check_correct():
            message = 'Correct'

        else:
            message = 'Error'
        
        return message

    def check_correct(self):
        """ Check to see if the numbers are in order and if the numbers are the same as the array. """

        if self.check_is_ordered() and self.check_same_numbers():
            return True

        else:
            return False

    def check_is_ordered(self):
        """ Check to see if the numbers are in order """

        is_in_order = True

        for i in range(1, self.size):

            if (self.data[i] < self.data[i - 1]):
                is_in_order = False

        return is_in_order

    def check_same_numbers(self):
        """ Check to see if the numbers are the same by compairing the sum before and after and the sum squared. """

        if self.before_sum == self.after_sum and self.before_sum_sq == self.after_sum_sq:
            return True

        else:
            return False

    def compute_sum(self):
        """ Compute the sum of all the numbers in the array. """

        sum = 0
        for i in range(self.size):
            sum = sum + self.data[i]

        return sum

    def compute_sum_sq(self):
        """ Compute the sum squared of all the numbers in the array. """
        
        sum = 0

        for i in range(self.size):
            sum = sum + self.data[i] * self.data[i]

        return sum

    def set_before_sum(self):
        """ Compair the sum of the array and compairs after it's computed. """

        self.before_sum = self.compute_sum()
        self.before_sum_sq = self.compute_sum_sq()

    def set_after_sum(self):
        """ Set the after sum squared with comute some squared. """

        self.after_sum = self.compute_sum()
        self.after_sum_sq = self.compute_sum_sq()