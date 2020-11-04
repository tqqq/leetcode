# coding=utf-8
import os
import sys

template = '''# coding=uf-8


class Solution(object):
    pass


def test():
    sol = Solution()


if __name__ == '__main__':
    test()

'''


def generate_py_with_template():
    args = sys.argv
    num = args[1]

    dir_path = os.getcwd()
    file_path = os.path.join(dir_path, f'{num}.py')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(template)


if __name__ == '__main__':
    generate_py_with_template()
