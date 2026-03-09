def find_friend(lst_num, now, goal, cnt):
    cnt += 1
    for i in range(len(lst_num)):
        if lst_num[i][0] == now:
            lst_num[i][1] == goal

            data = lst_num[i][1]
            return cnt
    return find_friend(lst_num, data, goal, cnt)

# n명, m개의 친구 관계
n, m = map(int, input().split())
lst = []
for _ in range(m):
    a, b = map(int, input().split())
    lst.extend([(a, b), (b, a)])

lst.sort()

min_v = 0
for friend_v in range(1, n+1):
    val = 0
    cnt = 0
    for friend_g in range(friend_v+1, n+1):
        #val은 v에서 g를 찾기위한 재귀함수가 돌아간 횟수
        val += find_friend(lst, friend_v, friend_g, cnt)

    if min_v > val:
        min_v = val

    print(min_v)
    # for i in range(len(lst)): #lst[i][0] or lst[i][1]




