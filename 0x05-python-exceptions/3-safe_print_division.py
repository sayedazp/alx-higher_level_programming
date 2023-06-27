#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        divison = a/b
    except (ValueError, TypeError, ZeroDivisionError):
        divison = None
    finally:
        print("Inside result: {}".format(divison))
    return divison
