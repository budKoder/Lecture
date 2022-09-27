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

'''
solution
'''
n = int(input())
body = []
for i in range(n):
    a,b = map(int, input().split())
    body.append((a,b))
body.sort(reverse=True)
largest = 0
cnt = 0
for x, y in body:
    if y > largest:
        largest = y
        cnt += 1
print(cnt)
