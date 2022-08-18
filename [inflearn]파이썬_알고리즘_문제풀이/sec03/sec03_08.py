import sys
# sys.stdin = open("input.txt","r")
'''
곶감
'''
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# 회전
m = int(input())
for _ in range(m):
    row, direction, distance = map(int, input().split())
    row -= 1
    distance %= n
    if distance > 0:
        new = []
        if direction == 0:
            new = arr[row][distance:]+arr[row][:distance]
        else:
            new = arr[row][-distance:]+arr[row][:-distance]
        arr[row] = new

# 합
mid = n//2
cnt = arr[mid][mid]
st,ed = mid, mid+1
for i in range(mid):
    st -= 1
    ed += 1
    cnt += sum(arr[mid-(i+1)][st:ed])
    cnt += sum(arr[mid+(i+1)][st:ed])
print(cnt)
