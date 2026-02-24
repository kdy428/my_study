# 아래 함수를 수정하시오.
def get_keys_from_dict(dictionary):
    result = list(dictionary.keys())
    return result

def get_all_keys_from_dict(dictionary):
    key_data = []
    for key, val in dictionary.items():
        key_data.append(key)
        if isinstance(val, dict):
            key_data.extend(get_all_keys_from_dict(val))
    return key_data

my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)  # ['name', 'age']

my_dict = {'person': {'name': 'Alice', 'age': 25}, 'location': 'NY'}
result = get_all_keys_from_dict(my_dict)
print(result)  # ['person', 'name', 'age', 'location']
