import os
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

while True:
    question = input("질문을 입력하세요: ")
    if question == "끝":
        print("대화를 종료합니다.")
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question
    )
    print(response.text)
    print("---")