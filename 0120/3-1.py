n = int(input()) # n 입력 받음
if (n<2): # 0과 1
  print("소수가 아니다")
else: # 2이상의 수인 경우
  for i in range(2,n):
    if (n%i==0): # 1과 자기자신 외에 약수가 존재하면
      print("소수가 아니다") # 소수가 아니다
      quit() # 강제종료
print("소수이다")
  