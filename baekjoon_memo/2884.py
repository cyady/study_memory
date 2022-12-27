A, B = map(int, input().split())
time=(A*60+B-45)
if time<0:
    time=24*60+time
A=time//60
B=time%60

print(A, B)