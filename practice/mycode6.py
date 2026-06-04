# 딕셔너리 만들기
person = {
    "name": "tyang",
    "age": 37,
    "job": "AI 개발자"
}

# 값 꺼내기
print(person["name"])
print(person["job"])

# 값 추가/수정
person["city"] = "서울"
person["age"] = 31
person["sex"] = "male"

# 전체 출력
for key, value in person.items():
    print(key, ":", value)