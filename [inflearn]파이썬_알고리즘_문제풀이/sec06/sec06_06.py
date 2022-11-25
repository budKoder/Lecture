import sys
sys.stdin = open("input.txt", "r")
# 대량 입력을 읽는 속도 향상
# 문자열을 읽을 때 개행문자(\n)도 함께 읽으므로 strip()을 함께 사용해야 한다.
# s = input().strip()
input = sys.stdin.readline

'''
중복순열 구하기
'''
def DFS(x):
    global cnt
    if x >= m:
        for x in res:
            print(x, end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            res[x] = i
            DFS(x+1)


# solution
def solution(L):
    global cnt
    if L == m:
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            res[L] = i
            solution(L+1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    cnt = 0
    res = [0] * m
    DFS(0)
    print(cnt)

    cnt = 0
    solution(0)
    print(cnt)
