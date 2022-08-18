import sys
# sys.stdin = open("input.txt","r")
'''
사과나무
'''
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
st, ed = 0, n
mid = n//2
cnt = sum(arr[mid])
for i in range(mid):
    st += 1
    ed -= 1
    cnt += sum(arr[mid-(i+1)][st:ed])
    cnt += sum(arr[mid+(i+1)][st:ed])
print(cnt)
