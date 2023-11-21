"""
Solutions to module 1
Student: 
Mail:
Reviewed by:
Reviewed date:
"""

"""
Important notes: 
These examples are intended to practice RECURSIVE thinking. Thus, you may NOT 
use any loops nor built in functions like count, reverse, zip, math.pow etc. 

You may NOT use any global variables.

You can write code in the main function that demonstrates your solutions.
If you have testcode running at the top level (i.e. outside the main function)
you have to remove it before uploading your code into Studium!
Also remove all trace and debugging printouts!

You may not import any packages other than time and math and these may
only be used in the analysis of the fib functionen.

In the oral presentation you must be prepared to explain your code and make minor 
modifications.

We have used type hints in the code below (see 
https://docs.python.org/3/library/typing.html).
Type hints serve as documatation and and doesn't affect the execution at all. 
If your Python doesn't allow type hints you should update to a more modern version!

"""

import time
import math


def power(x, n: int):  # Optional
    """ Computes x**n using multiplications and/or division """
    if n == 0:
        return 1
    return x * power(x, n - 1)


def multiply(m: int, n: int) -> int:  # Compulsory
    """ Computes m*n using additions"""
    if n == 0 or m == 0:
        return 0
    return m + multiply(m, n - 1)


def divide(t: int, n: int) -> int:  # Optional
    """ Computes m*n using subtractions"""
    if t < n:
        return 0
    return 1 + divide(t - n, n)


def harmonic(n: int) -> float:  # Compulsory
    """ Computes and returns the harmonc sum 1 + 1/2 + 1/3 + ... + 1/n"""
    if n == 1:
        return 1
    return (1 / n) + harmonic(n - 1)


def digit_sum(x: int, base=10) -> int:  # Optional
    """ Computes and returns the sum of the decimal (or other base) digits in x"""
    if x <= 0:
        return 0
    return x % base + digit_sum(x // base)


def get_binary(x: int) -> str:  # Compulsory
    """ Returns the binary representation of x """
    if x == 0:
        return "O"
    elif x == 1:
        return "1"
    return get_binary(x // 2) + str(x % 2)


def reverse_string(s: str) -> str:  # Optional
    """ Returns the s reversed """
    if len(s) <= 1:
        return s
    mid = len(s) // 2
    return reverse_string(s[mid:]) + reverse_string(s[:mid])


def largest(a: iter):  # Compulsory
    """ Returns the largest element in a"""
    if len(a) == 1:
        return a[0]
    largest_ = largest(a[1:])
    if a[0] > largest_:
        return a[0]
    return largest_


def count(x, s: list) -> int:  # Compulsory
    """ Counts the number of occurences of x on all levels in s"""
    if not s:
        return 0
    n = 0
    if type(s[0]) == list:
        n += count(x, s[0][:])
    elif s[0] == x:
        n += 1
    n += count(x, s[1:][:])
    return n


def zippa(l1: list, l2: list) -> list:  # Compulsory
    """ Returns a new list from the elements in l1 and l2 like the zip function"""
    if not l1 and not l2:
        return []
    if not l1:
        return l2
    if not l2:
        return l1
    return [l1[0], l2[0]] + zippa(l1[1:], l2[1:])


def bricklek(f: str, t: str, h: str, n: int) -> list:  # Compulsory
    """ Returns a string of instruction ow to move the tiles """
    moves = []

    def hanoi(n, f, t, h):
        if n == 0:
            return
        else:
            hanoi(n - 1, f, h, t)
            moves.append(f"{f}->{t}")
            hanoi(n - 1, h, t, f)

    hanoi(n, f, t, h)
    return moves


def fib(n: int) -> int:  # Compulsory
    """ Returns the n:th Fibonacci number """
    # You should verify that the time for this function grows approximately as
    # Theta(1.618^n) and also estimate how long time the call fib(100) would take.
    # The time estimate for fib(100) should be in reasonable units (most certainly
    # years) and, since it is just an estimate, with no more than two digits precision.
    #
    # Put your code at the end of the main function below!
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def main():
    print('\nCode that demonstates my implementations\n')

    print('\n\nCode for analysing fib\n')

    print('\nBye!')


if __name__ == "__main__":
    main()

####################################################

"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 16: Time for bricklek with 50 bricks:
  
  
  
  
  
  
  Exercise 17: Time for Fibonacci:
  
  
  
  
  
  Exercise 20: Comparison sorting methods:
  
  
  
  
  
  Exercise 21: Comparison Theta(n) and Theta(n log n)
  
  
  
  
  
  
  





"""
