# encoding: utf-8

import datetime
import json
import os
import sys

MYFULLPATH = os.path.abspath(sys.argv[0])
MYDIR = os.path.dirname(MYFULLPATH)

def ________Util________():
    pass

def file2str(filepath):
    ret = ''
    with open(filepath, encoding='utf8', mode='r') as f:
        ret = f.read()
    return ret

def str2obj(s):
    return json.loads(s)

def create_datetime_from_unixtime(number):
    return datetime.datetime.fromtimestamp(number)

def ________Argument________():
    pass

def parse_arguments():
    import argparse

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument('-i', '--input', default=None, required=True,
        help='An input .json filename.')

    args = parser.parse_args()
    return args

def ________Wrapper________():
    pass


class Project:
    def __init__(self, obj):
        self._obj = obj

    @property
    def name(self):
        return self._obj['name']

    @property
    def display_name(self):
        return self._obj['displayName']

    @property
    def exported_by_unixtime(self):
        return self._obj['exported']

    @property
    def exported_by_datetime(self):
        unixtime = self.exported_by_unixtime
        return create_datetime_from_unixtime(unixtime)

    def __str__(self):
        return '''/{name} {displayName}
exported at {exported}'''.format(
            name=self.name,
            displayName=self.display_name,
            exported=self.exported_by_datetime,
        )

def ________Main________():
    pass

if __name__ == '__main__':
    args = parse_arguments()

    filename = args.input
    s = file2str(filename)
    obj = str2obj(s)

    proj = Project(obj)
    print(proj)
