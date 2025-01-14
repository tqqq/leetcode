# coding=utf-8

import os
import shutil


def mkdir_if_not_exist(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)


def create_proj():
    for i in range(3):
        dir_name_1 = f"{i*1000}_{i*1000+1000}"
        mkdir_if_not_exist(dir_name_1)
        for j in range(10):
            dir_name_2 = os.path.join(dir_name_1, f"{j*100+i*1000}_{100+j*100+i*1000}")
            mkdir_if_not_exist(dir_name_2)
            for k in range(10):
                dir_name_3 = os.path.join(dir_name_2, f"{k*10+j*100+i*1000}_{10+k*10+j*100+i*1000}")
                mkdir_if_not_exist(dir_name_3)


def create_file(index: int):
    i = index - (index%1000)
    j = index - (index%100)
    k = index - (index%10)
    dir_path = os.path.join(f"{i}_{i+1000}", f"{j}_{j+100}", f"{k}_{k+10}")
    file_path = os.path.join(dir_path, f"{index}.py")
    shutil.copy("template.py", file_path)


def create_files(start, end):
    for i in start, end:
        create_file(i)


def main():
    # create_proj()
    for index in [1, 9, 13, 14, 20]:
        create_file(index)

    return


if __name__ == "__main__":
    main()




