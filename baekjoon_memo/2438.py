A=int(input())

string=""

for i in range(1,A+1):
    for j in range(0,i):
        string+="*"
        # print(string)
    print(string)
    string=""