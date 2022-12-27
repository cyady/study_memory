A=int(input())

string=""
space=""

for i in range(1,A+1):
    for j in range(0,i):
        string+="*"
        # print(string)
    for j in range(i,A):
        space+=" "
    space=space+string
    print(space)
    string=""
    space=""