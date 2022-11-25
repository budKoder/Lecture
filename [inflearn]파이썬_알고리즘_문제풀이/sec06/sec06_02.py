import sys
sys.stdin = open("input.txt", "r")
'''
이진트리 순회(깊이우선탐색)
'''
def preOrder(x):
    if x > n:
        return
    else:
        print(x, end=' ')
        preOrder(x*2)
        preOrder(x*2+1)


def inOrder(x):
    if x > n:
        return
    else:
        inOrder(x*2)
        print(x, end=' ')
        inOrder(x*2+1)


def postOrder(x):
    if x > n:
        return
    else:
        postOrder(x*2)
        postOrder(x*2+1)
        print(x, end=' ')


# solution
# 부모 : x / 왼쪽자식 : x*2 / 오른쪽자식 : x*2+1
# 전위순회 : root > left > right
# 중위순회 : left > root > right
# 후위순회 : left > right > root
def solution(v):
    if v > 7:
        return
    else:
        # print(v, end=' ')   # 전위순회
        solution(v*2)
        # print(v, end=' ')   # 중위순회
        solution(v*2+1)
        # print(v, end=' ')   # 후위순회


if __name__ == "__main__":
    n = int(input())
    print("전위순회 출력 : ", end='')
    preOrder(1)
    print("\n중위순회 출력 : ", end='')
    inOrder(1)
    print("\n후위순회 출력 : ", end='')
    postOrder(1)
    print()
    solution(1)
