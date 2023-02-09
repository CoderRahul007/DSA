from os import *
from sys import *
from collections import *
from math import *

def areAnagram(str1, str2):
    # Write your code here.
    arr = [0]*256
    for i in str1:
        ch = ord(i)
        arr[ch] +=1
    for i in str2:
        ch = ord(i)
        arr[ch] -=1
    for i in arr:
        if i != 0:
            return 0
    return 1