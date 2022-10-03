import sys
# sys.stdin = open("input.txt","r")
'''
후위표기식 만들기
'''
token = list(input().strip())
prior = {"*":3, "/":3, "+":2, "-":2, "(":1}
result = []
st = []
for x in token:
    if x.isdigit():
        result.append(x)
    elif x == '(':
        st.append(x)
    elif x == ')':
        while st[-1] != '(':
            result.append(st.pop())
        st.pop()
    else:
        while st and prior[x] <= prior[st[-1]]:
            result.append(st.pop())
        st.append(x)
while st:
    result.append(st.pop())
print(''.join(result))

'''
solution
'''
a = input()
stack = []
res = ''
for x in a:
    # x가 10진수 숫자이면 True
    if x.isdecimal():
        res += x
    else:
        if x == "(":
            stack.append(x)
        elif x == "*" or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(x)
        elif x == "+" or x == "-":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.append(x)
        elif x == ")":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.pop()
while stack:
    res += stack.pop()
print(res)
