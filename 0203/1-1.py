# 함수 호출을 이용한 재귀적 방법

def fibo1(n):
  if n<2:
    return n
  else:
    return fibo1(n-1) + fibo1(n-2)

n = int(input())
print(fibo1(n))