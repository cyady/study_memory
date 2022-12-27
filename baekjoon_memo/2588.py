a=input()
a=int(a)
b=input()
b=int(b)
b_list=list(map(int, str(b)))

sol1 = a*int(b_list[2])
sol2 = a*int(b_list[1])
sol3 = a*int(b_list[0])
ans = a*b

print(sol1)
print(sol2)
print(sol3)
print(ans)