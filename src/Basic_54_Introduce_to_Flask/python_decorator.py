def divide(n1, n2):
    return n1 / n2


"""
Function are first class Object
The ability to pass the function around as an object
"""


def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)


def outer_function():
    print("I am outer")

    def nested_function():
        print("I am inner")

    nested_function()


def outer_function1():
    def nested_function():
        print("inside")

    return nested_function()


# inner_function = outer_function1()
# inner_function()
#################################### Another test #########################################

import time


def decorator_func(function):
    def wrapper_func():
        time.sleep(2)
        function()

    return wrapper_func()


@decorator_func
def hello_func():
    print("hello")


hello_func
