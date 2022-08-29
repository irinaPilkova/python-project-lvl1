#!/usr/bin/env python3


import prompt


def welcome_user():
    """This function returns User's name"""
    name = prompt.string('May I have your name?')
    welcome = 'Hello,' + ' ' + name + '!'
    print(welcome)
    return name
