import sys
# sys.stdin = open("input.txt","r")
'''
씨름 선수(그리디)
'''
n = int(input())
people = []
for _ in range(n):
    h,w = map(int, input().split())
    people.append([h,w])
people.sort(key=lambda x:x[0], reverse=True)

cnt = 0
for i in range(1,len(people)):
    weight = people[i][1]
    for j in range(i):
        if weight <= people[j][1]:
            cnt += 1
            break
print(len(people)-cnt)
