# 리스트 만들기
numbers = [10, 20, 30, 40, 50]

# 꺼내기 (0번부터 시작!)
print(numbers[0]) #10
print(numbers[2]) #30

# 추가
numbers.append(60)
print(numbers)

# 길이
print("개수:", len(numbers))

# 반복
for n in numbers:
    print(n)
    print(n * 2)
    