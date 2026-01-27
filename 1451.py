def ordered_difference_sets(set1, set2):
    set3 = set1 - set2
    set4 = set2 - set1
    if len(set3) > len(set4):
        return (set4, set3)
    else:
        return (set3, set4)

# 예시 실행
result = ordered_difference_sets({1, 2, 3, 4}, {3, 4, 5, 6})
print("결과:", result)  # 출력: ({1, 2}, {5, 6})

result = ordered_difference_sets({1, 2, 3, 4}, {1, 2, 3})
print("결과:", result)  # 출력: (set(), {4})
