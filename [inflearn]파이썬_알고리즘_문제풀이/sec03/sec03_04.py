import sys
# sys.stdin = open('input.txt',"r")
'''
두 리스트 합치기
'''
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
print(*sorted(a+b))

'''
solution
'''
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

p1 = p2 = 0
c = []
while p1 < len(a) and p2 < len(b):
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1
if p1 < n:
    c = c + a[p1:]
else:
    c = c + b[p2:]
for x in c:
    print(x, end=' ')
