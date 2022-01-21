a,b,c = map(int,input().split()) # a, b, c 입력 받음
print((a+b)%c)
print((a%c+b%c)%c)
print((a*b)%c)
print((a%c*b%c)%c)