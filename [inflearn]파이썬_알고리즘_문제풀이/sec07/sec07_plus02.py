# 퀵정렬 - 전위순회
def Qsort(lt, rt):
    if lt < rt:
        pos = lt
        pivot = arr[rt]
        for i in range(lt, rt):
            if arr[i] <= pivot:
                arr[i], arr[pos] = arr[pos], arr[i]
                pos += 1
        arr[pos], arr[rt] = arr[rt], arr[pos]
        Qsort(lt, pos-1)
        Qsort(pos+1, rt)


if __name__ == "__main__":
    arr = [45, 21, 23, 36, 15, 67, 11, 60, 20, 33]
    print("before sort : ", end='')
    print(arr)
    Qsort(0, 9)
    print("after sort : ", end='')
    print(arr)
