"""
Task
Read two integers from STDIN and print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
"""
#for this iuse python formating
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print("%d\n%d\n%d"%(a+b,a-b,a*b))