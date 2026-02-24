import sys
input = sys.stdin.readline

def f(s):
    global cnt_0, cnt_1

    if s == 0:
        cnt_0 += 1
        return 0
    elif s == 1:
        cnt_1 += 1
        return 1
    else:
        return f(s-1) + f(s-2)

t = int(input())
for _ in range(t):
    n = int(input())
    cnt_0, cnt_1 = 0, 0
    f(n)
    print(cnt_0, cnt_1)