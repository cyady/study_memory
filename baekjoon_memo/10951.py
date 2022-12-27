import sys


while True:
   try:
        A, B = map(int, sys.stdin.readline().split())
        # print(type(A), type(B))
        if 0 < A and B < 10:
            print(A + B)
            sys.stdout.flush()
        else:
            break
   except:
       break


# while True:
#     A, B=input().split()
#     A=int(A)
#     B=int(B)
#     if 0 < A and B < 10:
#         print(A + B)
#     else:
#         break
# #EOF error

