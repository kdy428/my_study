# 아래 함수를 수정하시오.
def reverse_string(str_list):
    str_list = reversed(list(str_list))
    str = ''.join(str_list)
    return str


result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH
