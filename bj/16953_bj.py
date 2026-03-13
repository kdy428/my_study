N, M = map(int, input().split())
min_v = 1000000000

def f(num, cnt):
    global min_v
    if cnt > min_v or num > M:
        return
    # print(num, cnt)
    if num == M:
        if min_v > cnt:
            min_v = cnt
        return
    f(num*2, cnt+1)
    f(int(str(num) + '1'), cnt+1)

f(N, 1)
if min_v == 1000000000:
    print(-1)
else:
    print(min_v)
