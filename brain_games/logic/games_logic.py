#!/usr/bin/env python3


from random import randint


lower_limit = 1
upper_limit = 100


def create_number():
    """This function creates random number."""
    random_number = randint(lower_limit, upper_limit)
    return random_number
