import sys

A=int(sys.stdin.readline())
for i in range(0,A):
    a, b= map(int, sys.stdin.readline().split())
    string="Case #"+str(i+1)+": "+str(a)+" + "+str(b)+" = "+str(a+b)
    print(string)