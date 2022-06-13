""" Lab_9
    1) Individual task: N = 20 % 17 = 3.

    2) Results:
        - bm search: O(N / Σ)
        - direct search: O(N * M)
        where N - a string length,
              M - a search string length,
              Σ - count of unique chars in search a string.

        Direct search:  20; time:  5.484; compares:  96
        BM search:  20; time:  6.437; compares:  6.0
        ------------------------------
        Direct search:  121; time:  32.425; compares:  2178
        BM search:  121; time:  8.583; compares:  22.0
        ------------------------------
        Direct search:  840; time:  217.199; compares:  13776
        BM search:  840; time:  66.996; compares:  98.4
        ------------------------------
        Direct search:  Not found; time:  1308.68; compares:  10000
        BM search:  Not found; time:  5030.87; compares:  5000.0
        ------------------------------

    3) Conclusion:
        As we can see, BM algorithm is much faster, but it's useful for big data,
        and it's worse than first one when there are no matches in the text.
"""
from time import time


def main():

    # Example 1: length ~ 20
    search_string = 'data'
    text = 'dump date dare rate data'

    print('Direct search: ', direct_search(search_string, text), end='; ')
    print('time: ', get_runtime(direct_search, search_string, text), end='; ')
    print('compares: ', len(search_string) * len(text))

    print('BM search: ', bm_search(search_string, text), end='; ')
    print('time: ', get_runtime(bm_search, search_string, text), end='; ')
    print('compares: ', len(text) / len(create_image(search_string)))

    print('-' * 30)

    # Example 2: length ~ 200
    search_string = 'information'
    text = 'informatioN' * 11 + search_string + 'information' * 6

    print('Direct search: ', direct_search(search_string, text), end='; ')
    print('time: ', get_runtime(direct_search, search_string, text), end='; ')
    print('compares: ', len(search_string) * len(text))

    print('BM search: ', bm_search(search_string, text), end='; ')
    print('time: ', get_runtime(bm_search, search_string, text), end='; ')
    print('compares: ', len(text) / len(create_image(search_string)))

    print('-' * 30)

    # Example 3: length ~ 1000
    search_string = 'capitalization'
    text = 'capitalizatiOn' * 60 + search_string + 'capitalizatio' * 10

    print('Direct search: ', direct_search(search_string, text), end='; ')
    print('time: ', get_runtime(direct_search, search_string, text), end='; ')
    print('compares: ', len(search_string) * len(text))

    print('BM search: ', bm_search(search_string, text), end='; ')
    print('time: ', get_runtime(bm_search, search_string, text), end='; ')
    print('compares: ', len(text) / len(create_image(search_string)))

    print('-' * 30)

    # Example 4: length ~ 10000 with 'Not found' result
    search_string = 'a'
    text = 'b' * 10_000

    print('Direct search: ', direct_search(search_string, text), end='; ')
    print('time: ', get_runtime(direct_search, search_string, text), end='; ')
    print('compares: ', len(search_string) * len(text))

    print('BM search: ', bm_search(search_string, text), end='; ')
    print('time: ', get_runtime(bm_search, search_string, text), end='; ')
    print('compares: ', len(text) / len(create_image(search_string)))

    print('-' * 30)


def direct_search(substring: str, string: str) -> [int, str]:
    """ A simple algorithm for finding a substring in a string.
    Return 'Not found' if there are no matches.
    """
    substr_length = len(substring)
    str_length = len(string)

    if substr_length > str_length:
        return 'Not found'

    i = 0
    while i < str_length:

        k = i
        j = 0
        while j < substr_length:
            if string[k] != substring[j]:
                break
            if j == substr_length - 1:
                return k - substr_length + 1

            j += 1
            k += 1

        i += 1

    return 'Not found'


def bm_search(substring: str, string: str) -> [int, str]:
    """ An algorithm for finding the first occurrence of a substring in a string.
    Return 'Not found' if there are no matches.
    """
    substr_length = len(substring)
    str_length = len(string)

    if substr_length > str_length:
        return 'Not found'

    img = create_image(substring)

    i = substr_length - 1
    while i < str_length:

        k = 0
        for j in range(substr_length-1, -1, -1):
            if string[i-k] != substring[j]:
                if j == substr_length - 1:
                    offset = img[string[i]] if string[i] in img else img['*']
                else:
                    offset = img[substring[j]]

                i += offset
                break

            k += 1

        if k == substr_length:
            return i - k + 1

    return 'Not found'


def create_image(substring: str):
    """ A table that assigns each char to its offset in the search string.
    It ignores occurrences more than 1.
    And create * char with substring length value.
    """
    length = len(substring)
    image = {}

    for i in range(length - 2, - 1, -1):
        if substring[i] not in image:
            image[substring[i]] = length - i - 1

    if substring[length - 1] not in image:
        image[substring[length - 1]] = length

    image['*'] = length

    return image


def get_runtime(func, *args) -> float:
    """ Calculate runtime in microseconds for a some function.
    """
    start = time()
    func(*args)
    return round((time() - start) * 1_000_000, 3)


if __name__ == "__main__":
    main()
