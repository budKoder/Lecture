import sys
# sys.stdin = open("input.txt", "r")
"""
최대점수 구하기(DFS)
"""
# def DFS(x, score, tm):
#     global mx
#     if tm > m:
#         return
#     if x == n:
#         if score > mx:
#             mx = score
#     else:
#         DFS(x+1, score+a[x][0], tm+a[x][1])
#         DFS(x+1, score, tm)
#
#
# if __name__ == "__main__":
#     n, m = map(int, input().split())
#     a = [list(map(int, input().split())) for _ in range(n)]
#     mx = 0
#     DFS(0, 0, 0)
#     print(mx)

'''
solution
'''
def DFS(L, sum, time):  # sum : 얻은 점수 / time : 쓴 시간
    global res
    if time > m:
        return
    if L == n:
        if sum > res:
            res = sum
    else:
        DFS(L+1, sum+pv[L], time+pt[L])
        DFS(L+1, sum, time)


if __name__ == "__main__":
    n, m = map(int, input().split())
    pv = list()     # 점수
    pt = list()     # 시간
    for i in range(n):
        a, b = map(int, input().split())
        pv.append(a)
        pt.append(b)
    res = 2147000000
    DFS(0, 0, 0)
    print(res)
