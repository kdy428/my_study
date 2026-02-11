# 아래 함수를 수정하시오.
def intersection_sets(set_1, set_2):
    set_3 = set_1 & set_2
    if len(set_3) == 0:
        return '공통 요소가 없습니다.'
    else :
        return (len(set_3), set_3)


result = intersection_sets({1, 2, 3}, {3, 4, 5})
print(result)  # (1, {3})

result = intersection_sets({1, 2}, {3, 4})
print(result)  # (0, set())
# 출력: 공통 요소가 없습니다
