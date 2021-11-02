# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import StringClass


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.

    n = 5

    for i in range(1, n + 1):

        # first element is always 1
        C = 1
        for j in range(1, i + 1):
            # first value in a line is always 1
            print(' ', C, end='')

            # using Binomial Coefficient
            C = C * (i - j) // j

        for j in range(0, n - i):
            print('  0', end='')
        print()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
