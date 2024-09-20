

import argparse
import re


argv = ['/home/ln304/PycharmProjects/R7-Act-Tests/bin/data_digger.py', '-p',
        '/home/ln304/Documents/R7-5514/finx_products_pricing_live_time.request', '-o',
        '/home/ln304/Documents/R7-5514/data/st-7', '-e', 'st-7', '-csv']


def print_argv(argv):
    error = filter(lambda x: re.match("^-[0-z].", x), argv)
    # error = filter(lambda x: len(x) == 5, argv)
    print("error: " + str(list(error)))


def validate_argv(argv):
    error = list(filter(lambda x: re.match("^-[0-z].", x), argv))
    if error:
        raise argparse.ArgumentTypeError(f"Wrong given arguments: '{error}'")



validate_argv(argv)

s = ['a', 'aa', 'aaa', 'b', 'bb']

two = filter(lambda x: len(x) == 5, s)
if list(two):
    print(list(two))
else:
    print('no two')

numbers = [70, 60, 80, 90, 50, 82, 90, 91, 84, 82, 94, 99, 78, 65, 61, 45, 89, 87, 49, 76, 81, 94]


def check_score(number):
    if number >= 80:
        return True

    return False


percentage_score = filter(check_score, numbers)

scores = list(percentage_score)
print(scores)
