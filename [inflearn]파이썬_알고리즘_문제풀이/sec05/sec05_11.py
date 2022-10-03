import sys
import heapq
# sys.stdin = open("input.txt","r")
'''
최대힙
'''
heap = []
while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0:
        print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-n,n))

'''
solution
'''
import heapq as hq
# heapq는 기본적으로 최소힙으로 작동
# 부호를 반대로 바꿔서 넣으면 최대힙 구현 가능
a = []
while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0:
        print(-hq.heappop(a))
    else:
        hq.heappush(a, -n)
