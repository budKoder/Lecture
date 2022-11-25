import sys
sys.stdin = open("input.txt", "r")
'''
바둑이 승차(DFS)
'''
def DFS(x, subSum, leftSum):
    global mx
    if subSum > c:
        return
    elif subSum + leftSum < mx:
        return
    elif x >= n:
        if subSum > mx:
            mx = subSum
    else:
        DFS(x+1, subSum + w[x], leftSum - w[x])
        DFS(x+1, subSum, leftSum - w[x])


def solution(L, sum, tsum):
    # tsum : 현재까지 판단을 완료한 sum
    global result

    # 현재까지의 합과 남은 노드들의 최대합이 현재 max값보다 작다면 진행x
    if sum + (total-tsum) < result:
        return
    if sum > c:
        return
    if L == n:
        if sum > result:
            result = sum
    else:
        solution(L+1, sum + a[L], tsum + a[L])
        solution(L+1, sum, tsum + a[L])


if __name__ == "__main__":
    c, n = map(int, input().split())
    # w = list(int(input()) for _ in range(n))
    # mx = 0
    # DFS(0, 0, sum(w))
    # print(mx)

    a = [0] * n
    result = -2147000000
    for i in range(n):
        a[i] = int(input())
    total = sum(a)
    solution(0, 0, 0)
    print(result)
