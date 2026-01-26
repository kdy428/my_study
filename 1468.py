# 아래 함수를 수정하시오.
def remove_duplicates(num_list):
    new_lst = []
    for i in num_list:
        if i not in new_lst:
            new_lst.append(i)
            
        # num = num_list.count(i)
        # for j in range(num-1) :
        #     num_list.remove(i)

    return new_lst


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)
