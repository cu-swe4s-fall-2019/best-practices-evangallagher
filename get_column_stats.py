import math
import argparse
import sys
import random

# Takes the mean of a given column


def mean(list_col):

    try:
        if list_col == []:
            print('Empty list')
            return None
        else:
            return sum(list_col)/len(list_col)
    except TypeError:
        print('Argument must be an integer')
        raise TypeError
        sys.exit(1)

# takes the standard deviation of a column
def stdev(list_col):

    try:
        if list_col == []:
            print('Empty list')
            return None
        else:
            list_mean = mean(list_col)
            return math.sqrt(sum([(list_mean-x)**2 for x in list_col]) /
                             len(list_col))
    except TypeError:
        print('Argument must be an integer')
        raise TypeError
        sys.exit(1)


# Combines functions, and puts them both out in one window
def main():

    parser = argparse.ArgumentParser(description='calc mean and stdev',
                        prog='get_column_stats')

    parser.add_argument('--file_name', type=str,
                        help='Name of the file', required=True)

    parser.add_argument('--column_number', type=int,
                        help='The column number', required=True)

    args = parser.parse_args()

    file_name = args.file_name
    col_num = args.column_number

    try:
        file = open(file_name, 'r')
    except FileNotFoundError:
        print('Could not find ' + file_name)
        sys.exit(1)
    except PermissionError:
        print('Could not open ' + file_name)
        sys.exit(1)

    pr = []

    for line in file:
        try:
            lin = [x for x in line.split()]
            pr.append(int(lin[col_num]))
        except IndexError:
            print('Column number ' + str(col_num) + ' does not exist')
            sys.exit(1)

    column_mean = mean(pr)
    column_stdev = stdev(pr)

    print(['mean: ' + str(column_mean) + ', stdev: ' + str(column_stdev)])


if __name__ == '__main__':
    main()
