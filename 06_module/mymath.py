# 사용자 정의 모듈
print("start:", __name__) # 직접 실행하면 __main__, import 해서 실행되면 mymath
PI = 3.14


def add(a, b):
    return a + b

# if __name__ == "mymath":
#     exit(0)
if __name__ == "__main__":
    print(PI)
    print(add(10, 20))