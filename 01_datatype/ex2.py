# 파이썬의 자료형
# 1. 기본 자료형: 숫자형(정수형, 실수형), 불리언, 문자열
# 2. 컬렉션 자료형: 리스트, 튜플, 딕셔너리, 집합

# 숫자형 - 정수형 (int)
a = 10
print(a, type(a)) # <class 'int'>

# 2진수, 8진수, 16진수
print(bin(a), oct(a), hex(a))
# 아스키코드, 문자
print(ord("A"), chr(65))

# int 데이터의 표현 범위 : 4300자리 까지!
x = 10 ** 100
print(x)

# int 데이터가 커졌다가 작아지면 메모리 어떻게 됨? -> 

# 오버플로우 안 남
a = 2 ** 31 - 1
print(a)
a = a + 1
print(a)

# 숫자형 - 실수형 (float)
b = 3.14
print(b, type(b)) # <class 'float'>

# float 데이터의 표현 범위
# 부동소수점 방식
# 64비트 = 부호부 1비트 + 지수부 11비트 + 가수부 52비트

import sys
print(sys.float_info.min) # 양수 최솟값
print(sys.float_info.max) # 양수 최댓값

print(-sys.float_info.min) # 음수 최댓값
print(-sys.float_info.max) # 음수 최솟값

a = 1.7e308
b = 1.8e308
print(a, b) # b는 범위를 벗어나서 inf 뜸!

# 실수의 오차
print(0.1 + 0.2 == 0.3) # False
print(f"{0.1:.20f}")
print(f"{0.2:.20f}")
print(f"{0.3:.20f}")

print(0.1 == 0.1+0.1e-308) # 이건 왜 됨?

# 형변환
print(float(10))
print(int(3.14))
print(int("100"))
print(float("3.14"))