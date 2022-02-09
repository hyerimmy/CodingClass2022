answer = 80

user = int(input("1~100 사이 숫자를 입력하세요 >> "))
if user == answer:
  print("정답입니다!!")
elif user > answer:
  print("입력값이 정답보다 큽니다")
elif user < answer:
  print("입력값이 정답보다 작습니다")