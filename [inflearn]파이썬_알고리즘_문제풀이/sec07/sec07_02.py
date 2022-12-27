import sys
sys.stdin = open("input.txt", "r")
'''
휴가
'''
# def DFS(st, ed, p):
#     global mx
#     for nst, ned, np in schedule:
#         if nst >= ed and ned <= n+1:
#             DFS(nst, ned, p+np)
#     else:
#         if p > mx:
#             mx = p
#
#
# if __name__ == "__main__":
#     n = int(input())
#     a = [list(map(int, input().split())) for _ in range(n)]
#     schedule = []
#     for i in range(len(a)):
#         schedule.append([i+1, i+1+a[i][0], a[i][1]])
#     mx = 0
#     DFS(0, 0, 0)
#     print(mx)
def DFS(L, sum):    # L : 날짜
    global res
    if L == n+1:
        if sum > res:
            res = sum
    else:
        # 상담진행
        if L+T[L] <= n+1:
            DFS(L+T[L], sum+P[L])
        # 상담진행 x
        DFS(L+1, sum)

if __name__ == "__main__":
    n = int(input())
    T = list()  # 걸리는 시간
    P = list()  # 얻을 수 있는 비용
    for i in range(n):
        a, b = map(int, input().split())
        T.append(a)
        P.append(b)
    res = -2147000000
    T.insert(0, 0)  # 인덱스 번호를 날짜로 사용하기 위해 0번째 인덱스에 dummy 삽입
    P.insert(0, 0)
    DFS(1, 0)
    print(res)