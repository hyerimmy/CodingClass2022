# 반복문을 이용한 반복적 방법

def fibo2(n):
  f = [0,1]
  for i in range(2,n+1):
    f.append(f[i-1]+f[i-2])
  return f[n]

n = int(input())
print(fibo2(n))