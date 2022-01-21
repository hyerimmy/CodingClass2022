n = int(input()) # n 입력 받음
for i in range (1,n+1): # 1~n에 대하여 반복
  if (n%i == 0): # 만약 나누어 떨어진다면 (=약수라면)
    print(i, end=' ') # 출력
