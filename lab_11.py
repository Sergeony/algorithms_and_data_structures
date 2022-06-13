""" Lab_11: Insertion & Selection sort algorithms.

    1) Individual task: N=20
        20. 2 algorithms:
            - bubble sort by insert
            - binary insert sort

    2) Results:
        Bubble sort(20),    random:  time:  20.742;        comparisons:  190;        permutations:  87
        Insert sort(20),    random:  time:  18.835;        comparisons:  54;         permutations:  19
        Bubble sort(1000),  random:  time:  46890.497;     comparisons:  499500;     permutations:  250096
        Insert sort(1000),  random:  time:  2851.248;      comparisons:  7987;       permutations:  999
        Bubble sort(5000),  random:  time:  1230116.606;   comparisons:  12497500;   permutations:  6142110
        Insert sort(5000),  random:  time:  46984.673;     comparisons:  51822;      permutations:  4999
        Bubble sort(10000), random:  time:  4749756.813;   comparisons:  49995000;   permutations:  24579309
        Insert sort(10000), random:  time:  184764.862;    comparisons:  113631;     permutations:  9999
        Bubble sort(50000), random:  time:  122217409.849; comparisons:  1249975000; permutations:  616414837
        Insert sort(50000), random:  time:  4583020.21;    comparisons:  684481;     permutations:  49999

        Bubble sort(20),    dsc:     time:  21.219;        comparisons:  190;        permutations:  190
        Insert sort(20),    dsc:     time:  17.881;        comparisons:  54;         permutations:  19
        Bubble sort(1000),  dsc:     time:  46185.255;     comparisons:  499500;     permutations:  499500
        Insert sort(1000),  dsc:     time:  2746.344;      comparisons:  7987;       permutations:  999
        Bubble sort(5000),  dsc:     time:  1247315.407;   comparisons:  12497500;   permutations:  12497500
        Insert sort(5000),  dsc:     time:  41018.724;     comparisons:  51822;      permutations:  4999
        Bubble sort(10000), dsc:     time:  4811381.34;    comparisons:  49995000;   permutations:  49995000
        Insert sort(10000), dsc:     time:  159851.074;    comparisons:  113631;     permutations:  9999
        Bubble sort(50000), dsc:     time:  124955071.926; comparisons:  1249975000; permutations:  1249975000
        Insert sort(50000), dsc:     time:  4291554.928;   comparisons:  684481;     permutations:  49999

        Bubble sort(20),    asc:     time:  21.458;        comparisons:  190;        permutations:  0
        Insert sort(20),    asc:     time:  18.12;         comparisons:  54;         permutations:  19
        Bubble sort(1000),  asc:     time:  47332.287;     comparisons:  499500;     permutations:  0
        Insert sort(1000),  asc:     time:  2774.477;      comparisons:  7987;       permutations:  999
        Bubble sort(5000),  asc:     time:  1212968.826;   comparisons:  12497500;   permutations:  0
        Insert sort(5000),  asc:     time:  41565.895;     comparisons:  51822;      permutations:  4999
        Bubble sort(10000), asc:     time:  5163034.201;   comparisons:  49995000;   permutations:  0
        Insert sort(10000), asc:     time:  165247.44;     comparisons:  113631;     permutations:  9999
        Bubble sort(50000), asc:     time:  124346756.22;  comparisons:  1249975000; permutations:  0
        Insert sort(50000), asc:     time:  4214839.935;   comparisons:  684481;     permutations:  49999

    3) Conclusion:
        Insert sort is much faster in all cases. If we have random data, it's worse to use it.
        But as for ascending sequence, insert sort makes permutations(but still is faster).
"""
from random import randrange
from time import time


def main():

    # Example 1: length = 20
    array = [randrange(100) for _ in range(20)]

    _, comparisons, permutations = bubble_sort_by_insert(array)
    runtime = get_runtime(bubble_sort_by_insert, array)
    print('Bubble sort(20), random: ', 'time: ', runtime,
                                       '; comparisons: ', comparisons,
                                       '; permutations: ', permutations)
    _, comparisons, permutations = binary_insert_sort(array)
    runtime = get_runtime(binary_insert_sort, array)
    print('Insert sort(20), random: ', 'time: ', runtime,
                                       '; comparisons: ', comparisons,
                                       '; permutations: ', permutations)

    # Example 2: length = 1000
    array = [randrange(100) for _ in range(1000)]

    _, comparisons, permutations = bubble_sort_by_insert(array)
    runtime = get_runtime(bubble_sort_by_insert, array)
    print('Bubble sort(1000), random: ', 'time: ', runtime,
                                         '; comparisons: ', comparisons,
                                         '; permutations: ', permutations)
    _, comparisons, permutations = binary_insert_sort(array)
    runtime = get_runtime(binary_insert_sort, array)
    print('Insert sort(1000), random: ', 'time: ', runtime,
                                         '; comparisons: ', comparisons,
                                         '; permutations: ', permutations)

    # Example 3: length = 5000
    array = [randrange(100) for _ in range(5000)]

    _, comparisons, permutations = bubble_sort_by_insert(array)
    runtime = get_runtime(bubble_sort_by_insert, array)
    print('Bubble sort(5000), random: ', 'time: ', runtime,
                                         '; comparisons: ', comparisons,
                                         '; permutations: ', permutations)
    _, comparisons, permutations = binary_insert_sort(array)
    runtime = get_runtime(binary_insert_sort, array)
    print('Insert sort(5000), random: ', 'time: ', runtime,
                                         '; comparisons: ', comparisons,
                                         '; permutations: ', permutations)

    # Example 4: length = 10_000
    array = [randrange(100) for _ in range(10_000)]

    _, comparisons, permutations = bubble_sort_by_insert(array)
    runtime = get_runtime(bubble_sort_by_insert, array)
    print('Bubble sort(10000), random: ', 'time: ', runtime,
                                           '; comparisons: ', comparisons,
                                           '; permutations: ', permutations)
    _, comparisons, permutations = binary_insert_sort(array)
    runtime = get_runtime(binary_insert_sort, array)
    print('Insert sort(10000), random: ', 'time: ', runtime,
                                           '; comparisons: ', comparisons,
                                           '; permutations: ', permutations)

    # Example 5: length = 50_000
    array = [randrange(100) for _ in range(50_000)]

    _, comparisons, permutations = bubble_sort_by_insert(array)
    runtime = get_runtime(bubble_sort_by_insert, array)
    print('Bubble sort(50000), random: ', 'time: ', runtime,
                                           '; comparisons: ', comparisons,
                                           '; permutations: ', permutations)
    _, comparisons, permutations = binary_insert_sort(array)
    runtime = get_runtime(binary_insert_sort, array)
    print('Insert sort(50000), random: ', 'time: ', runtime,
                                           '; comparisons: ', comparisons,
                                           '; permutations: ', permutations)

    # Examples with ordered arrays:
    sizes = [20, 1000, 5000, 10000, 50000]

    for asc in range(2):
        for size in sizes:
            array = generate_sequence(size, bool(asc))

            _, comparisons, permutations = bubble_sort_by_insert(array)
            runtime = get_runtime(bubble_sort_by_insert, array)
            print(f'Bubble sort({size}), acs/dcs: ', 'time: ', runtime,
                  '; comparisons: ', comparisons,
                  '; permutations: ', permutations)
            _, comparisons, permutations = binary_insert_sort(array)
            runtime = get_runtime(binary_insert_sort, array)
            print(f'Insert sort({size}), acs/dcs: ', 'time: ', runtime,
                  '; comparisons: ', comparisons,
                  '; permutations: ', permutations)


def bubble_sort_by_insert(array: list):
    """ A bubble sort that reduces steps in the nested loop,
    because after each main loop the biggest element pops on the top.
    """
    comparisons = permutations = 0

    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                permutations += 1
            comparisons += 1

    return array, comparisons, permutations


def binary_insert_sort(array: list):
    """ An insertion sort that uses binary search to find place where element should be entered.
    """
    comparisons = permutations = 0

    for i in range(1, len(array)):
        insertion_item = array[i]

        pivot, add_comparisons = binary_search(array[0:i], insertion_item)
        comparisons += add_comparisons

        for j in range(i, pivot, -1):
            array[j] = array[j-1]
            permutations += 1

        array[pivot] = insertion_item
        permutations += 1

    return array, comparisons, permutations


def binary_search(array: list, value: int) -> [int, int]:
    """ The algorithm to find a value index in a list in logN operations.
    """
    comparisons = 0

    left_bound = 0
    right_bound = len(array)

    while left_bound < right_bound:
        center = (left_bound + right_bound) // 2

        if value < array[center]:
            right_bound = center
        elif value >= array[center]:
            left_bound = center + 1
        comparisons += 1

    return right_bound, comparisons


def get_runtime(func, *args) -> float:
    """ Calculate runtime in microseconds for a some function.
    """
    start = time()
    func(*args)
    return round((time() - start) * 1_000_000, 3)


def generate_sequence(count: int, asc: bool):
    """ Generate ascending or descending sequence.
    """
    if asc:
        return [i for i in range(count)]
    else:
        return [i for i in range(count, 0, -1)]


if __name__ == "__main__":
    main()
