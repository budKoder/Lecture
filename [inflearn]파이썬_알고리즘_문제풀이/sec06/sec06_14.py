import sys
sys.stdin = open("input.txt", "r")
'''
인접행렬(가중치 방향그래프)
'''
if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(m)]
    arr = [[0 for i in range(n)] for j in range(n)]
    for st, ed, val in a:
        arr[st-1][ed-1] = val
    for x in arr:
        print(' '.join(list(map(str, x))))
