# 반복문 : while문, for문

# while문
# 1 ~ 10까지 반복 출력
i = 0
while i < 10:
    i += 1
    print(i)
    if i == 5:
        break # break문 만나면 else 호출되지 않음!
else:
    print("End") # 조건식이 False가 되어 빠져나오면 실행!

nums = [1, 3, 5, 7, 9]
target = 2
i = 0
# found = False

while i < len(nums):
    if nums[i] == target:
        print("Target Found")
        # found = True
        break
    i += 1
else:
    print("Target Not Found")

# if not found:
#     print("Target Not Found")

# 1 ~ 10까지의 합
# sum = 55
i = 1
tot = 0
while i <= 10:
    tot += i
    i += 1
print(f"sum = {tot}")


i = 0
tot = 0
while i <= 10:
    # if i % 2 == 0:
    #     tot += i
    i += 1
    if i % 2 == 1:
        continue
    tot += i
print(f"sum = {tot}")
