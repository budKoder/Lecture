import sys
# sys.stdin = open("input.txt","r")
'''
점수계산
'''
n = int(input())
arr = list(map(int, input().split()))
score = 0
cur = 1
for x in arr:
    if x == 1:
        score += cur
        cur += 1
    else:
        cur = 1
print(score)

'''
solution
'''
n = int(input())
a = list(map(int, input().split()))
sum = 0
cnt = 0
for x in a:
    if x == 1:
        cnt += 1
        sum += cnt
    else:
        sum = 0
print(sum)
