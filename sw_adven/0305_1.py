### 10진수를 2진수로 변환
def decimal_to_binary(n):
    binary_num = ''
    # 0보다 클 때까지 2로 나누면서, 나머지를 정답에 추가
    while n > 0:
        remain = n % 2
        binary_num = str(remain) + binary_num
        n = n // 2
    
    return binary_num
print(decimal_to_binary(74))

### 10진수를 16진수로 변환
def decimal_to_hexadecimal(n):
    hex_digits = '0123456789ABCDEF'
    hexadecimal_num = ''
    while n > 0:
        remain = n % 16 # 0~15 숫자가 나옴, 0~9 + a~f로 나오게 변환해야함

        hexadecimal_num = hex_digits[remain] + hexadecimal_num
        n //= 16
    
    return hexadecimal_num
print(decimal_to_hexadecimal(255))

### 내장함수 활용 : 2진수변환 bin, 16진수변환 hex
print(bin(74))
print(hex(255))

### 문자열 입력
def func(binary_str):
    # 문자열의 뒤에서부터 탐색하며, 10진수로 변환
    pass
word = input().strip()

for i in range(0, len(word), 7):
    func(word[i:i+7])