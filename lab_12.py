""" Lab_12: Merge & Dividing sort algorithms.

    1) Individual task: N=20
        20. Write 3 sort algs:
            *quick sort
            *heap sort
            *merge sort

    2) Results:

        Quick sort(50),    random:  time:  40.054 ;     comparisons:  168 ;     permutations:  162
        Heap sort(50),     random:  time:  195.98 ;     comparisons:  1450 ;    permutations:  478
        Merge sort(50),    random:  time:  95.844 ;     comparisons:  325 ;     permutations:  286
        Quick sort(1000),  random:  time:  1277.685 ;   comparisons:  4707 ;    permutations:  6168
        Heap sort(1000),   random:  time:  4686.594 ;   comparisons:  50115 ;   permutations:  18044
        Merge sort(1000),  random:  time:  2999.544 ;   comparisons:  10697 ;   permutations:  9976
        Quick sort(5000),  random:  time:  8199.453 ;   comparisons:  28007 ;   permutations:  41054
        Heap sort(5000),   random:  time:  28144.836 ;  comparisons:  308700 ;  permutations:  113478
        Merge sort(5000),  random:  time:  16006.231 ;  comparisons:  65152 ;   permutations:  61808
        Quick sort(10000), random:  time:  17392.397 ;  comparisons:  60286 ;   permutations:  91812
        Heap sort(10000),  random:  time:  58522.94 ;   comparisons:  666135 ;  permutations:  246452
        Merge sort(10000), random:  time:  36708.593 ;  comparisons:  140114 ;  permutations:  133616
        Quick sort(50000), random:  time:  99868.059 ;  comparisons:  361032 ;  permutations:  573334
        Heap sort(50000),  random:  time:  339715.004 ; comparisons:  3907475 ; permutations:  1462988
        Merge sort(50000), random:  time:  195545.197 ; comparisons:  816457 ;  permutations:  784464

        Quick sort(50),    asc:     time:  37.67 ;      comparisons:  93 ;      permutations:  62
        Heap sort(50),     asc:     time:  134.706 ;    comparisons:  1605 ;    permutations:  540
        Merge sort(50),    asc:     time:  82.97 ;      comparisons:  232 ;     permutations:  286
        Quick sort(1000),  asc:     time:  864.267 ;    comparisons:  1533 ;    permutations:  1022
        Heap sort(1000),   asc:     time:  4818.916 ;   comparisons:  53545 ;   permutations:  19416
        Merge sort(1000),  asc:     time:  2515.316 ;   comparisons:  6931 ;    permutations:  9976
        Quick sort(5000),  asc:     time:  4997.015 ;   comparisons:  8856 ;    permutations:  5904
        Heap sort(5000),   asc:     time:  30746.698 ;  comparisons:  329665 ;  permutations:  121864
        Merge sort(5000),  asc:     time:  14969.587 ;  comparisons:  39803 ;   permutations:  61808
        Quick sort(10000), asc:     time:  10619.402 ;  comparisons:  17712 ;   permutations:  11808
        Heap sort(10000),  asc:     time:  66514.73 ;   comparisons:  709785 ;  permutations:  263912
        Merge sort(10000), asc:     time:  32232.046 ;  comparisons:  84607 ;   permutations:  133616
        Quick sort(50000), asc:     time:  65881.729 ;  comparisons:  98301 ;   permutations:  65534
        Heap sort(50000),  asc:     time:  410022.736 ; comparisons:  4116525 ; permutations:  1546608
        Merge sort(50000), asc:     time:  191524.744 ; comparisons:  482511 ;  permutations:  784464

        Quick sort(50),    dsc:     time:  37.193 ;     comparisons:  117 ;     permutations:  110
        Heap sort(50),     dsc:     time:  134.468 ;    comparisons:  1290 ;    permutations:  414
        Merge sort(50),    dsc:     time:  83.447 ;     comparisons:  252 ;     permutations:  286
        Quick sort(1000),  dsc:     time:  929.356 ;    comparisons:  2032 ;    permutations:  2020
        Heap sort(1000),   dsc:     time:  5079.508 ;   comparisons:  46585 ;   permutations:  16632
        Merge sort(1000),  dsc:     time:  2666.95 ;    comparisons:  7043 ;    permutations:  9976
        Quick sort(5000),  dsc:     time:  5359.888 ;   comparisons:  11358 ;   permutations:  10904
        Heap sort(5000),   dsc:     time:  31347.036 ;  comparisons:  292185 ;  permutations:  106872
        Merge sort(5000),  dsc:     time:  15389.204 ;  comparisons:  42003 ;   permutations:  61808
        Quick sort(10000), dsc:     time:  10653.257 ;  comparisons:  22714 ;   permutations:  21808
        Heap sort(10000),  dsc:     time:  71696.281 ;  comparisons:  633485 ;  permutations:  233392
        Merge sort(10000), dsc:     time:  32180.071 ;  comparisons:  89007 ;   permutations:  133616
        Quick sort(50000), dsc:     time:  65792.322 ;  comparisons:  123300 ;  permutations:  115532
        Heap sort(50000),  dsc:     time:  405031.681 ; comparisons:  3744465 ; permutations:  1397784
        Merge sort(50000), dsc:     time:  203814.745 ; comparisons:  501951 ;  permutations:  784464

    3) Conclusions:
        As we can see, Quick sort takes the least time. The second one is Merge sort. And heap sort is
        the slowest.
"""
from random import randrange
from time import time


def main():

    sizes = [50, 1000, 5000, 10000, 50000]
    orders = ['random', 'asc', 'dsc']

    for order in orders:
        for size in sizes:
            # Quick sort:
            array = generate_sequence(size, order)
            comparisons, permutations = quick_sort(array)
            runtime = get_runtime(quick_sort, array)
            print(f'Quick sort({size}), {order}: ', 'time: ', runtime,
                  '; comparisons: ', comparisons,
                  '; permutations: ', permutations)

            # Heap sort:
            array = generate_sequence(size, order)
            comparisons, permutations = pyramidal_sort(array)
            runtime = get_runtime(pyramidal_sort, array)
            print(f'Heap sort({size}), {order}: ', 'time: ', runtime,
                  '; comparisons: ', comparisons,
                  '; permutations: ', permutations)

            # Merge sort:
            array = generate_sequence(size, order)
            comparisons, permutations = merge_sort(array)
            runtime = get_runtime(merge_sort, array)
            print(f'Merge sort({size}), {order}: ', 'time: ', runtime,
                  '; comparisons: ', comparisons,
                  '; permutations: ', permutations)


class Stack:
    """ A simple stack, for quick sort.
    """

    def __init__(self):
        self.array = []

    def push(self, value: any):
        """ Add a node to the top of the stack. """
        self.array.insert(0, value)

    def pop(self) -> any:
        """ Remove a node from the top of the stack. """
        return self.array.pop(0)

    def peek(self) -> any:
        """ Get a node from the top of the stack """
        return self.array[0] if len(self.array) else None


def quick_sort(array: list):
    """ Iterative implementation of Hoar's sort.

    -unsorted_range is a stack with left and right bounds of the list,
    where the list is not yet sorted.
    -Steps of sorting:
        1) appoint center in bounds as pivot, and pointers as left bound and right bound
        2) compare items on the left side with items on the right side, swap them in sort order
        3) push to unsorted_range the greater range, after comparison
        4) decrement current range with changed pointers, after comparison
    """
    comparisons = permutations = 0

    unsorted_range = Stack()
    unsorted_range.push(0)
    unsorted_range.push(len(array) - 1)

    while unsorted_range.peek():
        right, left = unsorted_range.pop(), unsorted_range.pop()

        while left < right:
            # step 1:
            center = (right + left) // 2
            pivot = array[center]
            i = left
            j = right

            # step 2:
            while i <= j:
                while array[i] < pivot:
                    i += 1
                while array[j] > pivot:
                    j -= 1

                if i <= j:
                    array[i], array[j] = array[j], array[i]
                    i += 1
                    j -= 1
                    permutations += 2
                comparisons += 1

            # step 3 and 4:
            if i < center:
                if i < right:
                    unsorted_range.push(i)
                    unsorted_range.push(right)
                comparisons += 1
                right = j
            else:
                if j > left:
                    unsorted_range.push(left)
                    unsorted_range.push(j)
                comparisons += 1
                left = i
            comparisons += 1

    return comparisons, permutations


def pyramidal_sort(array):
    """ Recursive heap sort.
    """
    comparisons = permutations = 0

    size = len(array)

    for i in range(size, -1, -1):
        add_comparisons, add_permutations = update_heap(array, size, i)
        comparisons += add_comparisons
        permutations += add_permutations

    for i in range(size - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        permutations += 2

        add_comparisons, add_permutations = update_heap(array, i, 0)
        comparisons += add_comparisons
        permutations += add_permutations

    return comparisons, permutations


def update_heap(array, size, root):
    """ Put the biggest element as root.
    """
    comparisons = permutations = 0

    pivot = root
    left = (2 * root) + 1
    right = (2 * root) + 2

    if left < size and array[left] > array[pivot]:
        pivot = left

    if right < size and array[right] > array[pivot]:
        pivot = right

    if pivot != root:
        array[root], array[pivot] = array[pivot], array[root]
        add_comparisons, add_permutations = update_heap(array, size, pivot)

        comparisons += add_comparisons
        permutations += add_permutations
        permutations += 2

    comparisons += 5

    return comparisons, permutations


def merge_sort(array):
    """ Recursive merge sort.
    """
    comparisons = permutations = 0

    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        add_comparisons, add_permutations = merge_sort(left)
        comparisons += add_comparisons
        permutations += add_permutations

        add_comparisons, add_permutations = merge_sort(right)
        comparisons += add_comparisons
        permutations += add_permutations

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
                permutations += 1
            else:
                array[k] = right[j]
                j += 1
                permutations += 1
            k += 1
            comparisons += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
            permutations += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
            permutations += 1

    comparisons += 1

    return comparisons, permutations


def generate_sequence(count: int, order: str):
    """ Generate some sequence: random, ascending, descending.
    """
    if order == 'random':
        return [randrange(1, 100) for _ in range(count)]
    elif order == 'asc':
        return [i for i in range(count)]
    else:
        return [i for i in range(count, 0, -1)]


def get_runtime(func, *args) -> float:
    """ Calculate runtime in microseconds for a some function.
    """
    start = time()
    func(*args)
    return round((time() - start) * 1_000_000, 3)


if __name__ == "__main__":
    main()
