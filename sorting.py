#Sorting

def bubble_sort(lst):
    """Returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap.

        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """
    sorted = False
    i = 0
    while sorted == False and i < len(lst):
        swap_in_this_round = False
        for j in range(len(lst)-1):
            
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swap_in_this_round = True
        sorted = not swap_in_this_round

    return lst



def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list
    containing all integers in the input lists.

    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """

    length = len(list1) + len(list2)

    newly_sorted = []

    while len(newly_sorted) < length:
        if len(list1) < 1:
            newly_sorted.extend(list2)
        elif len(list2) < 1:
            newly_sorted.extend(list1)
        else:
            if list1[0] < list2[0]:
                newly_sorted.append(list1.pop(0))
            else:
                newly_sorted.append(list2.pop(0))

    return newly_sorted


##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.

    Finish the merge sort algorithm by writing another function that takes in a
    single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all
    integers from the input list. In other words, the new function should sort
    a list using merge_lists and recursion.

    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """
    # base case: 
    if len(lst) == 1:
        return lst
    else:
        return merge_lists(merge_sort(lst[:len(lst)/2]), merge_sort(lst[len(lst)/2:]))




#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
