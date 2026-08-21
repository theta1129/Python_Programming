# 변수
a = 2
b = 3
print(a, b)

# a = 2, b = 3
# a = (2, b) = 3
# 이렇게 됨 -> 안됨!

# 하는 법
a = 2; b = 3 # 권장 X
a, b = 2, 3 # 자동으로 언패킹해서 넣어 줌
[a, b] = 3, 5 # 이건 왜 되지..?
print(a, b)

# 값 swap
temp = a
a = b
b = temp
print(a, b)

a, b = b, a
print(a, b)

# 변수명 규칙 (C와 동일)
# 알파벳, 숫자, 특수문자(_)만 가능
# 숫자로 시작 불가
# 예악어 금지
# 대소문자 구분

# name! = "뽀로로" # X
# 2name = "크롱" # X
_age = 23 # O
# class = "클래스" # X
이름 = "오승후" # 잘 됨 but 권장 X
print(이름)


student_name = "크롱" # snake_case
studentName = "크롱" # camelCase

MAX_SCORE = 100 # 상수는 대문자로 약속
