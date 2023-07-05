#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random


def do_rand():
    min_number = 0
    max_number = 0
    keep_count = 0
    number_count = 0
    is_sort = ""

    while True:
        try:
            min_number = float(input("输入最小值："))
        except Exception as e:
            print("输入错误，请重新输入最小值")
            continue
        break

    while True:
        try:
            max_number = float(input("输入最大值："))
        except Exception as e:
            print("输入错误，请重新输入最大值")
            continue
        break

    while True:
        try:
            keep_count = int(input("保留几位小数："))
        except Exception as e:
            print("输入错误，请重新输入保留几位小数")
            continue
        break

    while True:
        try:
            number_count = int(input("生成多少个数字："))
        except Exception as e:
            print("输入错误，请重新输入生成多少个数字")
            continue
        break

    while True:
        try:
            is_sort = str(input("是否排序(y/n, 默认n)："))
        except Exception as e:
            print(e)
            print("输入错误，是否排序(y/n, 默认n)")
            continue
        break

    rst_list = []
    for j in range(number_count):
        temp = random.uniform(min_number, max_number)
        rst_list.append(format(round(temp, keep_count), "." + str(keep_count) + "f"))

    if is_sort == "y":
        rst_len = len(rst_list)
        for i in range(rst_len):
            for j in range(rst_len - i - 1):
                if float(rst_list[j]) > float(rst_list[j + 1]):
                    rst_list[j], rst_list[j + 1] = rst_list[j + 1], rst_list[j]

    return rst_list


if __name__ == "__main__":
    while True:
        rst = do_rand()
        for i in rst:
            print(i)
