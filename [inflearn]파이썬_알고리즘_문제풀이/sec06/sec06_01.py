import sys
sys.stdin = open("input.txt", "r")
'''
재귀함수를 이용한 이진수 출력
'''
def DFS(x):
    if x == 0:
        return
    else:
        DFS(x//2)
        print(x%2, end='')


# solution
def solution(x):
    if x == 0:
        return
    else:
        solution(x//2)
        print(x%2, end='')


if __name__ == "__main__":
    n = int(input())
    DFS(n)
    print()
    solution(n)
