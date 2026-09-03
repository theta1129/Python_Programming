# for문

# for (int i = 0; i < 10; i++)

for i in 'iterable 객체':
    print(i,end='')
print()


for i in range(5): # start = 0, stop, step = 1
    print(i, end=' ') # 0 1 2 3 4
print()

a = range(5) # range는 iterable 크래스!
print(a.start, a.stop, a.step) # 0 5 1

# 1부터 5까지
for i in range(1, 6):
    print(i, end=' ')
print()

# 0부터 10까지 중에 짝수 출력
for i in range(0, 11, 2):
    print(i, end=' ')
print()

# 5 4 3 2 1 출력
for i in range(5, 0, -1):
    print(i, end=' ')
print()

# 1부터 10까지의 합

# 1. for문
tot = 0
for i in range(1, 11):
    tot += i
print(tot)

# 2. sum
print(sum(range(1, 11)))

# sum을 변수로 써버리면 함수로써는 못 씀! --> 예약어는 못 쓰고, sum같은 '함수'는 안 쓰는게 좋음

s = "hi12!@한글大韓民國😂"

for c in s:
    print(c, end=" ") # Python은 Unicode 기반이기 때문에 출력 정상적으로 가능!
print()

print(len(s)) # 길이도 잘 나옴; 바이트 수 달라도 1로 잡힘!


# 구구단 출력
# 2 * 1 = 2    2 * 2 = 4  ..  2 * 9 = 18
# ..
# 9 * 1 = 9    9 * 2 = 18  ..  9 * 9 = 81

for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j:<2d}", end='   ')
    print()