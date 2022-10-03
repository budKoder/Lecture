import sys
# sys.stdin = open("input.txt", "r")
'''
Anagram(아나그램)
'''
a = input()
b = input()
check_a, check_b = dict(), dict()
for x in a:
    if x in check_a:
        check_a[x] += 1
    else:
        check_a[x] = 1
for y in b:
    if y in check_b:
        check_b[y] += 1
    else:
        check_b[y] = 1
if check_a == check_b:
    print("YES")
else:
    print("NO")

'''
solution
'''
# dict.get(key, default_value) : dict에 key값이 있으면 해당 value를 반환, 없으면 default_value를 반환
a = input()
b = input()
str1 = dict()
str2 = dict()
for x in a:
    str1[x] = str1.get(x,0) + 1
for x in b:
    str2[x] = str2.get(x,0) + 1
for i in str1.keys():
    if i in str2.keys():
        if str1[i] != str2[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")

'''
solution2(딕셔너리 해쉬)
'''
a = input()
b = input()
sH = dict()
for x in a:
    sH[x] = sH.get(x, 0) + 1
for x in b:
    sH[x] = sH.get(x, 0) - 1
for x in a:
    if sH.get(x) != 0:
        print("NO")
        break
else:
    print("YES")

'''
solution3(리스트 해쉬)
'''
a = input()
b = input()
# 알파벳 대문자 + 소문자 총 52개 초기화
str1 = [0] * 52
str2 = [0] * 52
# ascii : 대문자 65~90 / 소문자 97~122
# list : 0~25 대문자 / 26~51 소문자
for x in a:
    if x.isupper():
        str1[ord(x)-65] += 1
    else:
        str1[ord(x)-71] += 1
for x in b:
    if x.isupper():
        str2[ord(x)-65] += 1
    else:
        str2[ord(x)-71] += 1
for i in range(52):
    if str1[i] != str2[i]:
        print("NO")
        break
else:
    print("YES")
