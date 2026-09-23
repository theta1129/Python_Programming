# 함수 1

# ===========================================================
# 1. 기본 함수
# ===========================================================

# int add(int a, int b)
# {
#     return a + b;
# }


def add(a, b):
    """return the result of operation : a + b""" # --> doc string
    return a + b # __add__()

print(int.__add__(1, 2))
print(str.__add__("hello", " python"))
print(list.__add__([1, 2], [3, 4]))
print(tuple.__add__((1, 2), (3, 4)))

print(add(3, 4))
print(add("hello", " python"))
print(add([1, 2], [3, 4]))
print(add((1, 2), (3, 4)))
print(add.__doc__)

# ===========================================================
# 2. 튜플을 리턴하는 함수
# ===========================================================

def add_sub(a, b):
    return a + b, a - b

print(add_sub(5, 3))
print(*add_sub(5, 3))

x, y = add_sub(5, 3) # 자동 언패킹
print(x, y)


# ===========================================================
# 3. 디폴트 매개변수 (Default Parameter)
# ===========================================================
# 매개변수에 기본값을 지정하면, 호출 시 해당 인자를 생략할 수 있다.
# 디폴트 매개변수는 항상 일반 매개변수 뒤에 위치해야 한다.

# def sub(a = 0, b): # --> 디폴트가 있는 매개변수는 항상 없는 매개변수 뒤에 와야 함!
#     return a - b

def sub(a = 0, b = 0):
    return a - b

print(sub(5, 10))
print(sub(5))
print(sub())


# ===========================================================
# 4. 키워드 인자 (Keyword Argument)
# ===========================================================
# 인자를 순서가 아니라 "매개변수명=값" 형태로 전달할 수 있다.
# 순서를 바꿔서 호출해도 이름만 맞으면 정확히 전달된다.

print(sub(5, 10))
print(sub(b = 10, a = 5))
# print(sub(b = 10, 5)) # --> 키워드 인자는 항상 젤 뒤에 와야 함!
# print(sub(5, a = 6)) # --> 키워드 인자로 앞에 적은 값이 들어오면 안됨!

def introduce(name, hometown, mbti = "INTP"):
    return f"저는 {name}이고, {hometown}에 살고, {mbti}입니다."

print(introduce("Theta", "Greece", "INTP"))
print(introduce(mbti = "INTP", hometown = "Greece", name = "Theta"))
print(introduce(hometown = "Greece", name = "Theta"))

# ===========================================================
# 5. 가변 인자 (Variable-length Argument, *args)
# ===========================================================
# 몇 개의 인자가 들어올지 모를 때 *args를 사용한다. (관례적으로 사용)
# args라는 이름으로 입력값들을 모아 튜플로 만든다.

def add_all(*args):
    print(args)
    return sum(args)

print(add_all(1, 2, 3))
print(add_all(1, 2, 3, 4, 5))

a = [1, 2, 3]
print(add_all(*a))


# ================================================================
# 6. 키워드 가변 인자 (Keyword Variable-length Argument, **kwargs)
# ================================================================
# 이름=값 형태로 몇 개가 들어올지 모를 때 **kwargs를 사용한다.
# kwargs라는 이름으로 입력값들을 모아 딕셔너리로 만든다.

def introduce2(**kwargs):
    print(kwargs)

introduce2(name="크롱", age=4, kind="공룡")

d = {"name": "크롱", "age": 4, "kind": "공룡"}
introduce2(**d)

# ===========================================================
# 7. *args와 **kwargs를 함께 사용하는 예시
# ===========================================================

# 디미가 현재 가진 돈 구하기
# - 지난 달 남은 돈 : 500원
# - 길 가다가 주운 돈 : 100원, 200원 => 가변인자 (튜플)
# - 아빠한테 받은 돈 : 10000원
# - 엄마한테 받은 돈 : 5000원 => 키워드 가변인자 (딕셔너리)

def pocket_money(last_money, *args, **kwargs):
    # print(last_money)
    # print(args)
    # print(kwargs)
    return last_money + sum(args) + sum(kwargs.values())

print(f"{pocket_money(500, 100, 200, dad=10000, mom=5000)}원")
print(f"{pocket_money(500, 100, 200, 300, dad=10000, mom=5000, uncle=100000)}원")