import random
answer = random.randint(1, 100)

for i in range(0,5):
  user = int(input("1~100 사이 숫자를 입력하세요 >> "))
  if user == answer:
    print("정답입니다!!")
    quit()
  elif user > answer:
    print("입력값이 정답보다 큽니다")
  elif user < answer:
    print("입력값이 정답보다 작습니다")

print("정답을 못 맞혔습니다. 정답은",answer,"입니다!")