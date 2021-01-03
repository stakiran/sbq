# encoding: utf-8

import datetime
import json
import os
import re
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

def count_first_space_or_tab(s):
    count = 0
    for c in s:
        if c == '\t':
            count += 1
            continue
        if c == ' ':
            count += 1
            continue
        break
    return count

def ________Argument________():
    pass

def arguments_pagename(parser):
    parser.add_argument('--substr', default=None, type=str)
    parser.add_argument('--method', default=None, type=str)

def arguments_root(parser):
    parser.add_argument('-i', '--input', default=None, required=True,
        help='An input .json filename.')

def parse_arguments():
    import argparse

    parser_root = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    subparsers = parser_root.add_subparsers()

    parser_pagename = subparsers.add_parser('name')

    arguments_root(parser_root)
    arguments_pagename(parser_pagename)

    args = parser_root.parse_args()
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
    def pages(self):
        return self._obj['pages']

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

class Page:
    def __init__(self, page_obj):
        self._obj = page_obj
        self._lines_cache = []

    @property
    def title(self):
        return self._obj['title']

    @property
    def id(self):
        return self._obj['id']

    @property
    def created_by_unixtime(self):
        return self._obj['created']

    @property
    def updated_by_unixtime(self):
        return self._obj['updated']

    @property
    def created_by_datetime(self):
        unixtime = self.created_by_unixtime
        return create_datetime_from_unixtime(unixtime)

    @property
    def updated_by_datetime(self):
        unixtime = self.updated_by_unixtime
        return create_datetime_from_unixtime(unixtime)

    @property
    def _lines(self):
        return self._obj['lines']

    @property
    def lines(self):
        ''' 以下を実施
        - 行頭インデントを space に揃える'''
        if len(self._lines_cache) != 0:
            return self._lines_cache

        newlines = []
        for line in self._obj['lines']:
            # 上手い正規表現思いつかなかった...
            # r'^[\t ]+' を「マッチした文字数個の ' '」にreplaceしたいんだが...
            count = count_first_space_or_tab(line)
            newline = '{}{}'.format(
                ' '*count,
                line[count:]
            )
            newlines.append(newline)
        self._lines_cache = newlines
        return newlines

    @property
    def rawstring(self):
        lines = self.lines
        return '\n'.join(lines)


    def __str__(self):
        lines = self.lines
        lineHeads = '\n'.join(lines[:3])
        line_number = len(lines)
        return '''{title}
created at: {created}
updated at: {updated}
---
{lineHeads}...

total {lineNumber} lines. '''.format(
            title=self.title,
            created=self.created_by_datetime,
            updated=self.updated_by_datetime,
            lineHeads=lineHeads,
            lineNumber=line_number,
        )

def ________Main________():
    pass

if __name__ == '__main__':
    args = parse_arguments()

    print('=== args ===')
    print(args)
    print('')

    filename = args.input
    s = file2str(filename)
    obj = str2obj(s)

    proj = Project(obj)
    print('=== Project ===')
    print(proj)
    print('')

    pages = proj.pages
    page = Page(pages[0])
    print('=== page[0] ===')
    print(page)
    print('')

    print(page.rawstring)
