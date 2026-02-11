t = int(input())
for tc in range(t):
    txt = list(map(str, input().split()))
    
    stack = []
    ans = True

    for x in txt:
        if ans == False:
            break

        if x == '.':
            break

        if x not in '*/+-':
            stack.append(int(x))

        elif len(stack) < 2:
            ans = False

        else:
            op2 = stack.pop()
            op1 = stack.pop()
            if x == '+':
                stack.append(op1+op2)
            elif x == '-':
                stack.append(op1-op2)
            elif x == '*':
                stack.append(op1*op2)
            elif x == '/':
                stack.append(op1//op2)
        
    if ans == False or len(stack) != 1:
        print(f'#{tc+1} error')
    else:
        print(f'#{tc+1} {stack[0]}')