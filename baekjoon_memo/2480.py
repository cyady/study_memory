diceA, diceB, diceC = map(int, input().split())
count = 0
reward =0
same_eye=0
# print(diceA, diceB, diceC)

if diceA == diceB and diceB!=diceC:
    count=1
    same_eye=diceA
elif diceA == diceC and diceB!=diceA:
    count=1
    same_eye=diceA
elif diceB==diceC and diceB!=diceA:
    count=1
    same_eye=diceB
elif (diceA==diceB) and (diceA==diceC):
    count=2
    same_eye=diceC

# print(count)

if count==0:
    reward=max(diceA, diceB, diceC)*100
elif count==1:
    reward=1000+same_eye*100
elif count==2:
    reward=10000+same_eye*1000

print(reward)