# 비트 연산자

a = 5 # 0000 0000 0000 0101
b = 3 # 0000 0000 0000 0011
print(a & b) # 0000 0000 0000 0001 --> 1
print(a | b) # 0000 0000 0000 0111 --> 7
print(a ^ b) # 0000 0000 0000 0110 --> 6
print(a << b) # 0000 0000 0010 1000 --> 40; 5 -> 10 -> 20 -> 40
print(a >> b) # 0000 0000 0000 1010 --> 5
print(~a) # 1111 1111 1111 0101 --> -6

# 멤버십 연산자
print("a" in "apple") # True
print("a" not in "apple") # False

print(3 in [1, 2, 3]) # True

# 삼항 연산자
# int max = a > b ? a : b; --> C version

a = 2
b = 3

print(a if a > b else b) # 3
print("even" if a % 2 == 0 else "odd") # even

score = 85
# 90점 이상이면 "A"
# 80점 이상이면 "B"
# 70점 이상이면 "C"
# 70점 미만이면 "D"
print("A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D")