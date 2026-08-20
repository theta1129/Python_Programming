# 입출력

a = input()
print(a) # 자동 줄바꿈 되어 있음
print(type(a)) # <class 'str'>; 입력은 기본적으로 문자열임!
print(a, end='') # 줄바꿈 안하기
print(a, type(a)) # , 쓰면 여러 개 쓸 수 있음 (사이에 공백)
print(a, type(a), sep=",") # 구분자 바꿀 수 있음

a = int(a) # 형변환
print(a, type(a))

a = int(input()) # 입력 받고 바로 형변환
print(a, type(a)) # 파이썬은 정수형 int 하나임

b = float(input()) # 파이썬은 실수형 float 하나임
print(b, type(b))

# 정수 두 개 입력

# 100
# 200
a, b = int(input()), int(input()) # 1
print(a, b)
a = int(input()) # 2
b = int(input()) # 2
print(a, b)

# 100 200
a = input().split()
print(a, type(a)) # ['100', '200'] <class 'list'>

# map
# map(함수, List 객체)
a = map(int, input().split())
print(a, type(a)) # <map object at ..> <class 'list'>; map()은 맵 클래스 생성자임!

a, b, c = map(int, input().split()) # 언패킹해서 데이터 넣어줌
print(a, b, c)

# 리스트 변환
a = list(map(int, input().split))
print(a, type(a)) # <class 'list'>

