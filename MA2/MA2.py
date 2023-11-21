"""
Solutions to module 2 - A calculator
Student: 
Mail:
Reviewed by:
Reviewed date:
"""

"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""

import math
from tokenize import TokenError
from MA2tokenizer import TokenizeWrapper


class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)


class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self, arg)


def statement(wtok, variables):
    """ See syntax chart for statement"""
    result = assignment(wtok, variables)
    # Check for EOL
    print(wtok.get_current())
    if not wtok.is_newline():
        raise SyntaxError("Expected end of line, but found additional tokens")
    return result


def assignment(wtok, variables):
    """ See syntax chart for assignment"""
    result = expression(wtok, variables)
    while wtok.get_current() == '=':
        wtok.next()
        if wtok.is_name():
            variables[wtok.get_current()] = result
            wtok.next()
        else:
            raise SyntaxError("Expected variable after '='")

    return result


def expression(wtok, variables):
    """ See syntax chart for expression"""
    result = term(wtok, variables)
    while wtok.get_current() in ['+', '-']:
        operator = wtok.get_current()
        wtok.next()
        if operator == '+':
            result = result + term(wtok, variables)
        else:
            result = result - term(wtok, variables)
    return result


def term(wtok, variables):
    """ See syntax chart for term"""
    result = factor(wtok, variables)

    while wtok.get_current() in ['*', '/']:
        operator = wtok.get_current()
        wtok.next()
        if operator == '*':
            result = result * factor(wtok, variables)
        else:
            try:
                result = result / factor(wtok, variables)
            except ZeroDivisionError:
                raise EvaluationError("Divide by Zero error")
    return result


def arglist(wtok, variables):
    if wtok.get_current() == '(':
        result = []
        wtok.next()  # Consume the opening parenthesis '('
        while wtok.get_current() is not None and wtok.get_current() != ')':
            result.append(assignment(wtok, variables))
            # Check for and consume ',' separator
            if wtok.get_current() == ',':
                wtok.next()
            else:
                break  # Exit the loop if ',' is not found
        if wtok.get_current() == ')':
            wtok.next()  # Consume the closing parenthesis ')'
            return result
        else:
            raise SyntaxError("Expected ')' in the argument list")
    else:
        raise SyntaxError("Expected '(' in argument list")


def mean(arr):
    return sum(arr) / len(arr)


def fib(n):
    if n < 0:
        raise EvaluationError("Insert positive values")
    memory = {0: 0, 1: 1}

    def fib_mem(n):
        if n not in memory:
            memory[n] = fib_mem(n - 1) + fib_mem(n - 2)
        return memory[n]

    return fib_mem(n)


def log(n):
    if n <= 0:
        raise EvaluationError("log function only accepts positive values")
    return math.log(n)


def fac(n):
    if not n.is_integer():
        raise EvaluationError("insert whole number")
    return math.factorial(n)



def factor(wtok, variables):
    """ See syntax chart for factor"""
    FUNCTIONS_1 = {
        "sin": math.sin,
        "cos": math.cos,
        "exp": math.exp,
        "log": log,
        "fac": fac,
        "fib": fib,
    }
    FUNCTIONS_N = {
        "min": min,
        "max": max,
        "sum": sum,
        "mean": mean,
    }
    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'")
        else:
            wtok.next()

    elif wtok.get_current() in FUNCTIONS_1:
        function = FUNCTIONS_1[wtok.get_current()]
        wtok.next()
        if wtok.get_current() == '(':
            wtok.next()
            result = assignment(wtok, variables)
            if wtok.get_current() != ')':
                raise SyntaxError("Expected ')' in the function")
            else:
                result = function(result)
                wtok.next()
        else:
            raise SyntaxError("Expected '(' in the function")

    elif wtok.get_current() in FUNCTIONS_N:
        function = FUNCTIONS_N[wtok.get_current()]
        wtok.next()
        result = arglist(wtok, variables)
        result = function(result)

    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()

    elif wtok.is_name():
        try:
            result = variables[wtok.get_current()]
        except KeyError:
            raise EvaluationError(f"No saved variable {wtok.get_current()}")
        wtok.next()
    elif wtok.get_current() == "-":
        wtok.next()
        result = -factor(wtok, variables)
    else:
        raise SyntaxError(
            "Expected number or '('")
    return result


def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file
    """

    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
    # Note: The unit test file initiate variables in this way. If your implementation 
    # requires another initiation you have to update the test file accordingly.
    init_file = 'MA2init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('init  :', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0] == '#':
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'quit':
            print('Bye')
            exit()
        # 7: command vars shows all stored variables with values
        if wtok.get_current() == 'vars':
            print(variables)
        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print('Result:', result)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(
                    f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')

            except EvaluationError as ee:
                print("*** Evaluation error: ", ee)


if __name__ == "__main__":
    main()
