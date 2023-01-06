import sys
sys.stdin = open("input.txt", "r")
'''
네트워크 선 자르기(Top-Down)
'''
# def DFS(x):
#     if x == 1:
#         return 1
#     elif x == 2:
#         return 2
#     else:
#         return DFS(x-1) + DFS(x-2)
#
#
# n = int(input())
# print(DFS(n))
'''
solution
'''
def DFS(len):
    if dy[len] > 0:
        return dy[len]
    if len == 1 or len == 2:
        return len
    else:
        dy[len] = DFS(len-1) + DFS(len-2)
        return dy[len]


if __name__ == "__main__":
    n = int(input())
    dy = [0] * (n+1)
    print(DFS(n))
