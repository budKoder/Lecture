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
