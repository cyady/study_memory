a,b,c=map(int, input().split())
#첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.
d= (a+b)%c
print(d)
d=((a%c)+(b%c))%c
print(d)
d=(a*b)%c
print(d)
d=((a%c) * (b%c))%c
print(d)

