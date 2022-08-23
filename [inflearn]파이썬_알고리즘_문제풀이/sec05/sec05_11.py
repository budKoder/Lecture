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
