# 파일 쓰기
with open("output.txt", "w") as f:
    f.write("Python으로 쓴 파일\n")
    f.write("두 번째 줄\n")
    f.write("세 번째 줄\n")

print("파일 저장 완료!")

# 파일 읽기
with open("output.txt", "r") as f:
    content = f.read()


print("--- 파일 내용 ---")
print(content)