# encoding: utf-8

import os
import sys

MYFULLPATH = os.path.abspath(sys.argv[0])
MYDIR = os.path.dirname(MYFULLPATH)

def str2file(filepath, s):
    with open(filepath, encoding='utf8', mode='w') as f:
        f.write(s)

def parse_arguments():
    import argparse

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument('-i', '--input', default=None,
        help='An input .json filename.')

    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_arguments()
