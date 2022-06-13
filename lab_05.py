""" Lab_5
    1) Individual task: N=20.
        20. Нульові елементи розташовані на рядках, індекси яких є кратними трьом.

    2) Results:
        If we save 0 elements, we can get it for N * M.
        If we don't save 0 elements, we can get it for N * (M - (M - 1) // 3 - 1),
        where N - rows,
              M - columns,
              // - python syntax for integer division.

    3) Conclusion:
        So, it's useful in this case.
"""
from random import randint


def main():
    """ The main logic of the program.
    """

    # get table size
    rows = int(input("Enter rows count: "))
    cols = int(input("Enter cols count: "))

    # calculate actual column count
    actual_cols = cols - (cols - 1) // 3 - 1

    # create empty table
    table = [[0 for _ in range(actual_cols)] for _ in range(rows)]

    # fill the table with random values
    fill_table(table)

    # print the table
    print_table(table, cols)

    # print line to separate table from the prints below.
    print('-'*20)

    # print several elements
    print(get_element(table, 2, 0))
    print(get_element(table, 1, 1))
    print(get_element(table, 2, 2))
    print(get_element(table, 3, 3))
    print(get_element(table, 4, 4))


def get_element(table: list, row_id: int, col_id: int) -> int:
    """ Get an element with a given indexes.
    """
    if col_id % 3 == 0:
        return 0
    else:
        actual_col_id = col_id - col_id // 3 - 1

        return table[row_id][actual_col_id]


def fill_table(table: list):
    """ Random fill the table.
    """
    for i in range(len(table)):
        for j in range(len(table[0])):
            table[i][j] = randint(1, 9)


def print_table(table: list, cols: int):
    """ Print the table.
    """
    for i in range(len(table)):
        for j in range(cols):
            if j % 3 == 0:
                print(0, ' ', end='')
            else:
                actual_j = j - j // 3 - 1

                print(table[i][actual_j], ' ', end='')

        print()


if __name__ == "__main__":
    main()
