# 문자열(str)
# "", '

a = "python" # ''도 되긴 하는데 "" 권장!
print(a, type(a)) # <class 'str'>

print("I'll be back") # 문자열에 ' 있을 땐 무조건 "" 써야 함!
print('I\'ll be back') # \ 써도 됨!
print('I"ll be back') # 문자열에 " 있을 땐 무조건 '' 써야 함!

# 여러 줄 문자열
a = """
Life is short
You need python
""" # 이거 주석 아님!!

print(a)

# docstring
def func():
    """
    func() 함수에 대한 설명 작성
    """
    pass

print(func.__doc__) # 첫 줄에 문자열 설명 쓰면 나옴!

# 문자열 연결
print("Hello" + "Python")

# 문자열 반복
print("Hello" * 10)

# 문자열 연산 시 주의사항
# print("Hello" + 3)

print("10" + "2")
print(int("10") + int("2"))
# print(sum(map(int, ["10", "2"]))) # 이것도 되네 ㄷㄷ
# print(map(int, ["10", "2"])[0]) # 이건 안되네.. 'map' object is not subscriptable

# 문자열 포맷팅 (f-string)
name = "뽀로로"
age = 23

print(f"이름: {name}, 나이: {age}")
print(f"내년 나이: {age + 1}살")
print(f"{name.upper()}") # 대문자로 쓰기; 한글은 안 됨; 근데 아스키코드 더하는거 아님? 왜 한글은 그대로 나오지?
print(f"중괄호 두 개 쓰고 싶으면 두 개 쓰면 됨 ㄱ- {{}}")


pi = 3.14
print(f"{pi:.1f}") # 반올림해서 나옴; 파이썬은 5사 5입!
print(f"{pi:.0f}") # 반올림해서 나옴; 파이썬은 5사 5입!

num = 123456789
print(f"{num:,}") # 세 자리씩 끊기

print(f"{num:15,d}") # 15칸 오른쪽 정렬, 세 자리씩 끊기
print(f"{num:<15,d}") # 15칸 왼쪽 정렬, 세 자리씩 끊기
print(f"{num:015,d}") # 15칸 오른쪽 정렬, 세 자리씩 끊기, 0채우기
print(f"{num:<015,d}") # 15칸 왼쪽 정렬, 세 자리씩 끊기, 0채우기