#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())
    binary_number = "{0:b}".format(n)
    consecutive_one = 1
    counter = 1
    for i in range(len(binary_number)-1) :
        if binary_number[i] == '1' and binary_number[i+1] == '1':
            counter = counter + 1
            if counter > consecutive_one:
                consecutive_one = counter
        else :
            counter = 1
    print(consecutive_one)