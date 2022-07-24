# 📌Q4. 강의에서 미국과 유럽의 엘리베이터 층수를 변환하는 프로그램이 나왔습니다.
#       그와 비슷하게 우리는 한국 나이를 미국 나이로 변환하는 프로그램을 코딩 해봅시다.
# hint: 미국 나이는 생일이 지났는지 안지났는지가 중요하죠!
# birth = int(input("생일이 지났습니까? 맞으면 0 아니면 -1 : "))

from tokenize import String


age = int(input("한국 나이가 몇살입니까? : "))
birth = int(input("생일이 지났습니까? 맞으면 0 아니면 -1 : "))
age = age - 1 + birth
print(f"당신의 미국나이는 {age}살 입니다.")
