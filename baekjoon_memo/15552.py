import sys

A=int(sys.stdin.readline())
for i in range(0,A):
    a, b=map(int, sys.stdin.readline().split())
    print(a+b)