# 불리언(bool)

a = True
print(a, type(a)) # <class 'bool'>

print(2 < 3) # True
print(2 > 3) # False
print(2 == 3) # False
print(2 != 3) # True

print("apple" > "banana") # 사전순 -> False
print("apple" > "apble") # 사전순 -> True

# bool()
print(bool(3)) # True
print(bool(0)) # False
print(bool("hello")) # True
print(bool("")) # False
print(bool([0])) # True
print(bool([])) # False

# None 자료형
a = None
print(a, type(a)) # <class 'NoneType'>
print(bool(a)) # False

if a is None:
    print("값이 없습니다.")