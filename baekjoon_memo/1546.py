N=int(input())
score=list(map(int, input().split()))
score = list(score[0:N])

fix = []
for i in range(len(score)):
    fix.append(score[i]/max(score)*100)

fix = sum(fix)/len(fix)
print(fix)