import sys
# sys.stdin = open("input.txt","r")
'''
창고정리
'''
l = int(input())
boxes = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    mx = max(boxes)
    mi = min(boxes)
    boxes[boxes.index(mx)] -= 1
    boxes[boxes.index(mi)] += 1
print(max(boxes) - min(boxes))
