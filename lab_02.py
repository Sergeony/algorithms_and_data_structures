""" Lab_2
    1) Individual task: N=20
        20. Для заданих x та n визначити значення функції:
            P(x) = x + x^3 / 3! + x^5 / 5! + ... + x^(2n+1) / (2n+1)!

    2) Time results:
        - Iterative: P(10, 10) ~= 10.014 * 10^(-6) s; P(80, 80) ~= 319.958 * 10^(-6) s;
        - Recursive: P(10, 10) ~= 07.153 * 10^(-6) s; P(80, 80) ~= 328.064 * 10^(-6) s;

    3) Conclusion:
        The first one takes more time on the small values, but the second one on the big.
        But the difference isn't very big.
        So, both of these algorithms take approximately the same time.
 """
from math import factorial
from time import time


def main():
    """ The main logic of the program.
    """
    x = int(input("Enter x: "))
    n = int(input("Enter n: "))

    print('Iterative result: ', iterative_p(x, n), end='; ')
    print('time: ', round(get_runtime(iterative_p, x, n), 3))

    print('Recursive result: ', recursive_p(x, n), end='; ')
    print('time: ', round(get_runtime(recursive_p, x, n), 3))


def iterative_p(x: int, n: int) -> float:
    """ Iterative algorithm to find p(x) with n numbers.
    """
    result: float = 0

    i = 1
    while i <= 2 * n + 1:
        result += (x ** i) / factorial(i)
        i += 2

    return result


def recursive_p(x: int, n: int) -> float:
    """ Recursive algorithm to find p(x) with n numbers.
    """
    if n == 0:
        return x

    return (x ** (2*n + 1)) / factorial(2*n+1) + recursive_p(x, n - 1)


def get_runtime(func, *args) -> float:
    """ Calculate runtime in microseconds for a some function.
    """
    start = time()
    func(*args)
    return (time() - start) * 1_000_000


if __name__ == "__main__":
    main()
