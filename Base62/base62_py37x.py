#!/usr/bin/env python
# http://www.zhihua-lai.com/
# base62 convert for python 3.7.x

from math import floor
base = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
b = 62;
def toBase10(b62: str) -> int:
    limit = len(b62)
    res = 0
    for i in range(limit):
        res = b * res + base.find(b62[i])
    return res
def toBase62(b10: int) -> str:
    if b <= 0 or b > 62:
        return 0
    r = b10 % b
    res = base[r];
    q = floor(b10 / b)
    while q:
        r = q % b
        q = floor(q / b)
        res = base[int(r)] + res
    return res
