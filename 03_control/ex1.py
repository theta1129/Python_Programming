# 조건문 : if문, match문

age = 17

if age >= 18:
    print("adult")
else:
    print("minor")


score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")


# match
grade = "A"

match grade:
    case "A":
        print("Brilliant") # break가 자동으로 실행
    case "B":
        print("Fine")
    case "C" | "D": # 케이스 추가
        print("Normal")
    case _: # default에 해당
        print("Unknown")