import sys
sys.stdin = open("input.txt", "r")
# 재귀함수와 스택
def DFS(x):
    if x > 0:
        DFS(x-1)
        print(x, end=' ')


def DFS1():
    # 1) 지역변수인지 확인
    # 2) 지역변수가 아니라면 전역변수인지 확인
    # 함수는 지역변수가 우선이다.
    cnt = 3
    print(cnt)


def DFS2():
    # global을 사용하면 할당문을 사용하더라도 지역변수를 생성하는 것이 아닌 전역변수를 사용한다.
    global cnt
    # 할당문(=)을 사용할 시 지역변수를 새로 생성
    # 지역변수가 된 cnt 는 assignment 되어 있지 않으므로 global 을 사용하지 않으면 오류
    if cnt == 5:
        cnt = cnt + 1
        print(cnt)


def DFS3():
    global a
    # a[x] = y 할당문은 새로운 리스트를 생성하는 것이 아니라 리스트의 참조값을 변경하는 것
    # 따라서 전역리스트로 인식하고 작동한다.
    a[0] = 7
    print(a)

    # a = [x,y] / a = a + [x] 할당문은 새로운 리스트가 생성되는 것이므로 지역변수가 된다.
    # 따라서 global 을 사용하거나, 지역변수 a를 선언하고 사용해야 한다.
    a = [7, 8]
    a = a + [4]


if __name__ == "__main__":
    n = int(input())
    DFS(n)
    print()

    # 전역변수와 지역변수
    # 전역변수 : main script 선언되면 전역변수
    #           모든 함수에서 접근/변경 가능
    cnt = 5
    DFS1()
    DFS2()
    print(cnt)

    a = [1, 2, 3]
    DFS3()
    print(a)
