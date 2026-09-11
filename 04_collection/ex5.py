# 딕셔너리 기초

# ===========================================================
#  딕셔너리 (dict): 키와 값 쌍으로 저장하는 변경 가능한 자료형
#  딕셔너리의 특징
#  1. ( mutable, 변경 가능 )
#  2. ( iterable, 반복 가능 )
#  3. ( sequence X, 인덱싱 슬라이싱 불가 )
#  4. ( 키는 중복 불가, 값은 중복 가능 )
# ===========================================================

# 딕셔너리 생성
a = {}
b = dict()
print(type(a), type(b)) # <class 'dict'>

d = {"id" : "1418",
     "name" : "Seunghu Oh",
     "age" : 17}

print(d)

# 키로 값 가져오기
print(d["name"])
#print(d["phone"]) # 키값이 없으면 KeyError

# 에러가 안나게 하려면?
if "phone" in d:
    print(d["phone"])

print(d.get("phone")) # Key가 있으면 Value, 없으면 Default(None) 리턴
print(d.get("phone", "no phone")) # Default 파라미터 변경 가능


# ===========================================================
# 1. 딕셔너리는 mutable하다. (변경 가능)
# ===========================================================

print(d["age"])
d["age"] += 1 # 값 변경
print(d["age"])

d["phone"] = "123-4567" # 값 추가
print(d)

del d["phone"]
print(d)

print(d.pop("age")) # Key를 지우고 그 Value를 반환

# print(d.pop("age")) # 없는 Key가 들어오면 KeyError
# del d["age"] # 없는 Key가 들어오면 KeyError

# ===========================================================
# 2. 딕셔너리는 iterable하다. (반복 가능)
# ===========================================================

# 딕셔너리 순회
for data in d:
    print(data) # Key만 나옴
    print(d[data]) # Value

for idx, key in enumerate(d):
    print(idx, key) # idx는 d의 인덱스가 아니라 그냥 순서; d는 Sequence X

for value in d.values():
    print(value) # Value

for key, value in d.items():
    print(key, value) # Key, Value 둘 다 나옴

# d.keys(), d.values(), d.items()는 view 객체; 바꿔도 바로 적용됨!
a = d.values()
d["name"] = "Will"
print(a) # 바로 적용!

# 컨텍스트 안쪽에서 변경되면 RuntimeError:
# for key, value in d.items():
#     d["Hi I'm Runtime Error"] = 1
for key, value in d.items():
    key = "Hi I don't change" # 바뀌지 않음
    value += "1" # 바뀌지 않음
print(d)

# ===========================================================
# 3. 딕셔너리는 sequence 객체가 아니다. (인덱싱, 슬라이싱 불가)
# ===========================================================




# ===========================================================
# 4. 딕셔너리는 키는 중복 불가, 값은 중복 가능하다.
# ===========================================================

d = {"kor": 90, "mat": 85, "eng": 80}



# 키로 가능한 것 : immutable 타입 (숫자형, 불리언, 문자열, 튜플) -> hashable type
# 키로 안되는 것 : mutable 타입 (리스트, 딕셔너리, 집합) -> unhashable type
# 키는 해시 가능(hashable) + 프로그램 실행 동안 hash값이 변하지 않아야 함



# 딕셔너리가 저장되는 방식
# 1. 딕셔너리 데이터를 저장하기 위한 해시 테이블을 생성함
# 2. hash(key) 함수를 통해 hash값을 얻음
# 3. hash값을 테이블 크기로 압축하여 버킷 인덱스를 계산하고 해시 테이블에 저장함
# 4. key값으로 조회할 때에도 hash(key)로 hash값을 얻어낸 후(동일 hash값) 해당 인덱스로 가서 조회함

# 만약 key에 mutable 타입을 허용했다면?
# 1. hash(key) 함수로 hash값을 얻어 해시 테이블에 저장함
# 2. key 내용이 변경됨
# 3. 다시 hash(바뀐key)를 하면 새로운 hash값이 나옴
# 4. 새 hash값을 이용하여 버킷 인덱스를 계산하고 해시테이블에 조회를 하면 원래 데이터를 찾을 수 없음



# ===========================================================
#  파이썬 내장 함수
# ===========================================================

d = {"kor": 90, "mat": 85, "eng": 80}



# 정렬 기준 설정하기
# lambda: 이름 없는(익명) 한 줄짜리 함수를 만듦
# lambda 매개변수1, 매개변수2, ... : 표현식



# 딕셔너리 합치기
d2 = {"sci": 95, "prog": 100}


# 딕셔너리 반복하기


# 멤버십 연산자