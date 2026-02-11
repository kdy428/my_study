in_stack = {'(' : 0 , '*' : 2, '/' : 2, '+' : 1, '-' : 1}
in_txt = {'(' : 3 , '*' : 2, '/' : 2, '+' : 1, '-' : 1}

for tc in range(10):
    #길이 n짜리 txt
    n = int(input())
    txt = input()
    txt_back = ''

    stack = []

    for x in txt:
        if x not in '(*/+-)':
            txt_back += x
        elif x == ')':
            while stack[-1] != '(':
                txt_back += stack.pop()
            stack.pop() #여는 괄호 삭제
        else:
            if len(stack) == 0 or in_stack[stack[-1]] < in_txt[x]:
                stack.append(x)
            elif in_stack[stack[-1]] >= in_txt[x]:
                while len(stack) != 0 and in_stack[stack[-1]] >= in_txt[x]:
                    txt_back += stack.pop()
                stack.append(x)
    
    while stack:
        txt_back += stack.pop()
    
    # print(txt_back, stack) 후위 계산식, stack = []

    for x in txt_back:
        if x not in '(*/+-)':
            stack.append(int(x))
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            if x == '+':
                stack.append(op2+op1)
            elif x == '-':
                stack.append(op1-op2)
            elif x == '/':
                stack.append(op1/op2)
            elif x == '*':
                stack.append(op1*op2)
    
    print(f'#{tc+1} {stack[0]}')


