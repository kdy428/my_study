T = int(input())
for tc in range(T):
    a, b, c = map(int, input().split())

    if b<2 or c<3:
        print(f'#{tc+1} -1')
        continue
    
    # a,b를 먹어서 c의 순서를 만들자
    def f(a, b, c, count):
        if a<b and b<c:
            print(f'#{tc+1} {count}')
            return
        # b를 c보다 작게 먼저 만들기
        elif b>=c:
            tmp = b-c+1
            f(a, b-tmp, c, count+tmp)
        # a를 b보다 작게 만들기
        elif a>=b:
            tmp = a-b+1
            f(a-tmp, b, c, count+tmp)
            
    f(a,b,c,0)