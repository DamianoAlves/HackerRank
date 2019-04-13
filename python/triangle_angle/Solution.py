# -*- coding: utf-8 -*-
import math

if __name__ == '__main__':
    ab = int(input())
    bc = int(input())
    ac = math.sqrt(ab ** 2 + bc ** 2)
    mb = ac / 2
    angle = math.acos((bc / 2) / (mb))
    angle = round(math.degrees(angle))
    print(f"{angle}\u00b0")