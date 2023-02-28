# File: sorts.py
# Author: Taylor Johnson
# Date: 2021.1.25
# Description: Calls different functions from different files and puts
#              them all together to print out the output.

from sorting_array import Sorting_array

SIZE_OF_ARRAY = 100
FIRST_RANDOM_NO = 1
LAST_RANDOM_NO = 101

def do_insertion_sort():
    """ Call functions from other files to do the insertion sort. """

    test_array = Sorting_array(SIZE_OF_ARRAY)

    print()
    print()
    print("Insertion Sort:")
    print()
    print("Random Integers:")
    print()

    test_array.fill()
    test_array.print()
    
    print()
    print()

    test_array.insertion_sort()
    test_array.print()

def do_shell_sort():
    """ Call functions from other files to do the shell sort. """

    test_array = Sorting_array(SIZE_OF_ARRAY)

    print()
    print()
    print("Shell Sort:")
    print()
    print("Random Integers:")
    print()

    test_array.fill()
    test_array.print()

    print()
    print("Sorted Integers:")
    print()

    test_array.shell_sort()
    test_array.print()

def do_heap_sort():
    """ Call functions from other files to do the heap sort. """

    test_array = Sorting_array(SIZE_OF_ARRAY)

    print()
    print()
    print("Heap Sort:")
    print()
    print("Random Integers:")
    print()

    test_array.fill()
    test_array.print()

    print()
    print("Sorted Integers:")
    print()

    test_array.heap_sort()
    test_array.print()

    # Checking to see if it will sort when the numbers increase by 1.
    print()
    print("Increasing Integers By 1:")
    print()

    test_array.increase_fill()
    test_array.print()

    print()
    print("Sorted Integers:")
    print()

    test_array.heap_sort()
    test_array.print()

    # Checking the sort when the numbers are all the same.
    print()
    print("Sorting The Same Number:")
    print()

    test_array.same_fill()
    test_array.print()

    print()
    print("Sorted Integers:")
    print()

    test_array.heap_sort()
    test_array.print()

    # Checking to see if it will sort when the numbers decrease by 1.
    print()
    print("Decreasing Integers By 1:")
    print()

    test_array.decrease_fill()
    test_array.print()

    print()
    print("Sorted Integers:")
    print()

    test_array.heap_sort()
    test_array.print()

def do_quick_sort():
    """ Call functions from other files to do the quick sort. """

    test_array = Sorting_array(SIZE_OF_ARRAY)

    print()
    print()
    print("Quick Sort:")
    print()
    print("Random Integers:")
    print()

    test_array.fill()
    test_array.print()

    print()
    print("Sorted Integers:")
    print()

    test_array.quicksort()
    test_array.print()

    # Checking to see if it will sort when the numbers increase by 1.
    print()
    print("Increasing Integers By 1:")
    print()

    test_array.increase_fill()
    test_array.print()

    print()
    print("Sorted Integers:")
    print()

    test_array.quicksort()
    test_array.print()

    # Checking the sort when the numbers are all the same.
    print()
    print("Sorting The Same Number:")
    print()

    test_array.same_fill()
    test_array.print()

    print()
    print("Sorted Integers:")
    print()

    test_array.quicksort()
    test_array.print()

    # Checking to see if it will sort when the numbers decrease by 1.
    print()
    print("Decreasing Integers By 1:")
    print()

    test_array.decrease_fill()
    test_array.print()

    print()
    print("Sorted Integers:")
    print()

    test_array.quicksort()
    test_array.print()

    print()

def do_complete_test():
    """ Perfom a complete test of all sort routines.

    Use a variety of sizes, fill orders and check routines
    to exercise and test four sort routines.
    """

    # Defines the test protocols/situations.
    test_sizes = [20, 60, 120, 240]
    test_sorts = ["Insertion Sort", "Shell Sort", "Heap Sort", "Quick Sort"]
    test_fills = ["Random", "Increasing", "Decreasing", "Same"]

    for which_sort in test_sorts:
        for which_fill in test_fills:
            for which_size in test_sizes:

                test_array = Sorting_array(which_size)

                # Create the array with the specified size.
                # do_test = Sorting_array(which_size)

                if which_fill == "Random":
                    test_array.fill()

                elif which_fill == "Increasing":
                    test_array.increase_fill()

                elif which_fill == "Decreasing":
                    test_array.decrease_fill()
                    
                elif which_fill == "Same":
                    test_array.same_fill()

                test_array.set_before_sum()

                if which_sort == "Insertion Sort":
                    test_array.insertion_sort()

                elif which_sort == "Shell Sort":
                    test_array.shell_sort()

                elif which_sort == "Heap Sort":
                    test_array.heap_sort()

                elif which_sort == "Quick Sort":
                    test_array.quicksort()

                test_array.set_after_sum()

                # Report this results.
                # Each report should be a single line that reports the sort used,
                # the fill order, the size and the check result.
                # The output should well formatted and easily understandable.

                print('{:20s} {:15s} {:7d} {:>15s}'.format(which_sort, which_fill, which_size, test_array.check_message()))

def main():
    """ Call all the different sorts. """

    do_complete_test()

main()