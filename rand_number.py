#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random


def do_rand():
    min_number = 0
    max_number = 0
    keep_count = 0
    number_count = 0

    while True:
        try:
            min_number = int(input("输入最小值："))
        except Exception as e:
            print("输入错误，请重新输入最小值")
            continue
        break

    while True:
        try:
            max_number = int(input("输入最大值："))
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

    rst_list = []
    for j in range(number_count):
        temp = random.uniform(min_number, max_number)
        rst_list.append(format(round(temp, keep_count), "." + str(keep_count) + "f"))

    return rst_list


if __name__ == "__main__":
    while True:
        rst = do_rand()
        rst_len = len(rst)
        for i in range(rst_len):
            for j in range(rst_len - i - 1):
                if float(rst[j]) > float(rst[j+1]):
                    rst[j], rst[j+1] = rst[j+1], rst[j]

        for i in rst:
            print(i)
