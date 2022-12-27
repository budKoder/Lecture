import sys
# sys.stdin = open("input.txt", "r")
'''
양팔저울
'''
# def DFS(x, L, left, right):
#     if left == right:
#         ch[x] = 0
#     if L == k:
#         return
#     else:
#         DFS(x, L+1, left + a[L], right)
#         DFS(x, L+1, left, right + a[L])
#         DFS(x, L+1, left, right)
#
#
# if __name__ == "__main__":
#     k = int(input())
#     a = list(map(int, input().split()))
#     ch = [1] * (sum(a) + 1)
#     ch[0] = 0
#     for i in range(1, sum(a)+1):
#         DFS(i, 0, i, 0)
#     print(sum(ch))
def DFS(L, sum):
    if L == n:
        if 0 < sum <= s:    # 음수는 대칭값으로 나타나므로, 양수인 값만 추가
            res.add(sum)
    else:
        DFS(L+1, sum+G[L])  # 현재 추를 왼쪽에
        DFS(L+1, sum-G[L])  # 현재 추를 오른쪽에
        DFS(L+1, sum)       # 현재 추를 사용하지 않음


if __name__ == "__main__":
    n = int(input())
    G = list(map(int, input().split()))
    s = sum(G)
    res = set()
    DFS(0, 0)
    print(s - len(res))
