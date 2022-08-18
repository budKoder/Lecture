import sys
# sys.stdin = open("input.txt","r")
'''
대표값
'''
n = int(input())
arr = list(map(int, input().split()))
avg = round(sum(arr)/len(arr))
# index, score, diff
current = [-1, -1, avg]
for idx, value in enumerate(arr):
    if abs(value - avg) < current[2]:
        current = [idx+1, value, abs(value - avg)]
    elif abs(value - avg) == current[2]:
        if value > current[1]:
            current = [idx+1, value, abs(value-avg)]
        elif idx < current[0]:
            current = [idx+1, value, abs(value-avg)]
print(avg, current[0])
