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

'''
solution
'''
import heapq as hq
a = []
while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, n)
