def bubble_sort(lst):
    """
    This function is sorting list with integers using bubblesort algoritm
    :param lst: list with integers to sort
    :return:
    """
    ln = len(lst)  # length of list
    while ln > 0:  # while length of list is more then null algoritm will sort the list
        for i in range(len(lst)-1):  # for iterator is getting each number from list in range length of list -1
            if lst[i] > lst[i+1]:  # comparing each number with the next one in list
                lst[i], lst[i+1] = lst[i+1], lst[i]  # priority of list getting change heregit
        ln = ln - 1  # length of list -1 to close the loop
    return lst  # return sorted list


print(bubble_sort([1, 0, 9, 5, 3, 8, 4, 6, 2]))
