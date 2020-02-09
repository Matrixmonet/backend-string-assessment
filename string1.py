#!/usr/bin/env python
"""
kenzie assignment: string1
"""
# copyright 2010 google inc.
# licensed under the apache license, version 2.0
# http://www.apache.org/licenses/license-2.0

# google's python class
# http://code.google.com/edu/languages/google-python-class/

# instructions:
# complete each function below by writing the code for it. main() is already
# set up to test all the functions with a few different inputs, printing 'ok' when
# each function returns the correct result.
# the starter code for each function includes a bare 'return' which is just a
# placeholder for your code.

# a. donuts
# given an int count of a number of donuts, return a string
# of the form 'number of donuts: <count>', where <count> is the number
# passed in. however, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# so donuts(5) returns 'number of donuts: 5'
# and donuts(23) returns 'number of donuts: many'


def donuts(count):
    if count >= 10:
        return 'Number of donuts: many'
    else:
        amt = str(count)

    return 'Number of donuts: ' + amt


# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
def both_ends(s):
    if len(s) < 2:
        return ''

    return s[0:2] + s[-2:]


# C. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.
def fix_start(s):
    firstChar = s[0]
    s = s.replace(firstChar, '*')
    s = firstChar + s[1:]

    return s

# D. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.


def mix_up(a, b):
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]

    return new_a + ' ' + new_b


# Provided simple test() function used in main() to print
#  what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {}    expected: {}'.format(
        prefix, repr(got), repr(expected)))


# The main() func calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
    print('donuts')
    # Each line calls donuts, and compares its result to the expected return for that call.
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print('')
    print('both_ends')
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

    print('')
    print('fix_start')
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print('')
    print('mix_up')
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')


# Standard boilerplate (python idiom) to call the main() function.
# This is called an "import guard"
if __name__ == '__main__':
    main()
