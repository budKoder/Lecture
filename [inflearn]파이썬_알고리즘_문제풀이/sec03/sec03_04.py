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
