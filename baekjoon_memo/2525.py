A, B =map(int, input().split())
C=int(input())#needs

time=(A*60+B+C)
if time >= (24*60):
    time = time -(24*60)


A=time//60
B=time%60
print(A, B)