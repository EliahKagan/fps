#!/usr/bin/env python3.10

"""fps: Failed Password Stats"""

from collections import Counter
import fileinput
import re

PATTERN = re.compile(r'Failed password for (?:invalid user )?(\w+)')


def main():
    names = Counter(match.group(1)
                    for match in map(PATTERN.search, fileinput.input())
                    if match)

    for name, count in names.most_common():
        print(f'{count:6}  {name}')


if __name__ == '__main__':
    main()
