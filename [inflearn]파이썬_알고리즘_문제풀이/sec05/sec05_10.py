import sys
import heapq
# sys.stdin = open("input.txt",'r')
'''
최소힙
'''
heap = []
while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0:
        print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,n)
