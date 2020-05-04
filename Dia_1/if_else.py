"""
Task
Given an integer,n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 29, print Weird
"""

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
test = {True: "Not Weird", False: "Weird"}
print(Test[
    n%2==0 and (
    n in range(2,6) or 
    n > 20) ])