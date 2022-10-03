import sys
# sys.stdin = open("input.txt","r")
'''
후위식 연산
'''
arr = list(input().strip())
st = []
for x in arr:
    if x.isdigit():
        st.append(int(x))
    else:
        n2 = st.pop()
        n1 = st.pop()
        if x == '+':
            st.append(n1+n2)
        elif x == '-':
            st.append(n1-n2)
        elif x == '*':
            st.append(n1*n2)
        elif x == '/':
            st.append(n1/n2)
print(st[0])

'''
solution
'''
a = input()
stack = []
for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else:
        n1 = stack.pop()
        n2 = stack.pop()
        if x == '+':
            stack.append(n2+n1)
        elif x == '-':
            stack.append(n2-n1)
        elif x == '*':
            stack.append(n2*n1)
        elif x == '/':
            stack.append(n2/n1)
print(stack[0])
