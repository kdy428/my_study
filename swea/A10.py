t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    heights = list(map(int, input().split()))
    max_h = max(heights)

    cnt1, cnt2 = 0, 0
    for h in heights:
        diff = max_h - h
        cnt2 += diff // 2
        cnt1 += diff % 2

    while cnt2 > cnt1 + 1: # 2쪼개기
        cnt2 -= 1
        cnt1 += 2

    if cnt1 == cnt2:
        day = cnt1 * 2
    elif cnt1 > cnt2:
        day = cnt1 * 2 - 1
    else:
        day = cnt2 * 2

    print(f"#{tc} {day}")
