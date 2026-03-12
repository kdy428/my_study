arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = 10

ans = 0
def back(sum_v, cnt):
    global ans
    if cnt == N and sum_v == 10:
        ans += 1
        return
    elif cnt == N and sum_v != 10:
        return
    elif sum_v > 10:
        return
    else:
        back(sum_v + arr[cnt], cnt + 1)
        back(sum_v, cnt + 1)
back(0, 0)
print(ans)