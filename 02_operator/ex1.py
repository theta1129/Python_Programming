# 연산자

# 산술 연산자
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) # 나머지
print(a // b) # 몫
print(a ** b) # 거듭제곱

# 복합 대입 연산자
a += 4
print(a)
a -= 4
print(a)
a *= 4
print(a)
a /= 4
print(a)
a //= 4
print(a)
a %= 4
print(a)
a **= 4
print(a)

# 증감 연산자
# a++ # 안 됨!
a += 1 # 이거 써야 함!

# 비교 연산자
print(3 == 3.0) # True
print(3 != 4) # True
print("apple" < "apble") # False
print(1 < 2 < 3) # 1 < 2 and 2 < 3 --> True
print(1 < 3 < 2) # 1 < 3 and 3 < 2 --> False

# 논리 연산자
a = True
b = False

print(a and b)
print(a or b)
print(not a)

# Short-circuit 테스트
a = 10
b = 0

# print(a / b) # ZeroDivisionError

if a > 0 or a / b:
    print("yes yes yes")
else:
    print("no no no no no")