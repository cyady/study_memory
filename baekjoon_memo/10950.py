C=int(input())
for i in range(C):
    A, B = map(int, input().split())
    if (A is not None) or (B is None):
        print(A+B)
