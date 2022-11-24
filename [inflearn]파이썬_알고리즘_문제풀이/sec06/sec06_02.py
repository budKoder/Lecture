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


if __name__ == "__main__":
    n = int(input())
    print("전위순회 출력 : ", end='')
    preOrder(1)
    print("\n중위순회 출력 : ", end='')
    inOrder(1)
    print("\n후위순회 출력 : ", end='')
    postOrder(1)
