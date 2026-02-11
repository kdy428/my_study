for tc in range(10):
    n = int(input())
    fx = input()
    susik = ''

    stack = [0] * n
    top = -1
    icp = {'*':2, '+':1}
    isp = {'*':2, '+':1}
    
    for x in fx:
        if x not in '+*':   # 숫자라면 susik에 추가
            susik += x
        else:   # 연산자라면
            if top==-1 or isp[stack[top]] < icp[x]: # 토큰의 우선순위가 더 높으면
                top += 1    # push
                stack[top] = x
            elif isp[stack[top]] >= icp[x]:
                while top > -1 and isp[stack[top]] >= icp[x]:
                    susik += stack[top]
                    top -= 1
                top += 1  # push
                stack[top] = x
                
    #남은 stack의 연산자 susik에 추가
    while top > -1:
        susik += stack[top]
        top -= 1
    #후위 표기식으로 변환까지 완료
    
    top = -1
    for x in susik:
        if x not in '+*': # 숫자라면
            top += 1            # push(x)
            stack[top] = int(x)
        else: #연산자
            op2 = stack[top]  # pop()
            top -= 1
            op1 = stack[top]  # pop()
            top -= 1
            if x=='+':  # op1 + op2
                top += 1                # push()
                stack[top] = op1 + op2
            else:
                top += 1
                stack[top] = op1 * op2

    print(f'#{tc+1} {stack[0]}')