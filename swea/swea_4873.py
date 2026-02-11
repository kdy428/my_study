t = int(input())
for tc in range(t):
    txt = input()

    stack = [0] * 1001
    top = -1
    for x in txt:
        if stack[top] == x:
            top -= 1
        else:
            top += 1
            stack[top] = x
    
    print(f'#{tc+1} {top+1}')