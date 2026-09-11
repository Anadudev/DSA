from typing import List


def fibonacci(n :int) -> List[int]:
    """
    Generates Fibonacci sequence up until n
    :param n: digit to reach
    :return: a list of Fibonacci
    """
    if n == 0:
        return [0]
    fib = [0, 1]
    for i in range(1, n):
        calc = fib[i-1]+ fib[i]
        if calc <= n:
            fib.append(fib[i-1]+ fib[i])
        else:
            break
    return fib

