t = int(input())
for tc in range(t):
    txt = input()

    top = -1
    stack = [0] * 100

    ans = 1
    for x in txt:
        # 소괄호 검사
        if x == '(':
            top += 1
            stack[top] = x

        elif x == ')':
            if top == -1: 
                ans = 0
                break
            else:
                if stack[top] == '(' :
                    top -= 1
                else:
                    ans = 0
                    break
        
        # 중괄호 검사
        if x == '{':
            top += 1
            stack[top] = x

        elif x == '}':
            if top == -1: 
                ans = 0
                break
            else:
                if stack[top] == '{' :
                    top -= 1
                else:
                    ans = 0
                    break

    if top != -1 :
        ans = 0

    print(f'#{tc+1} {ans}')
