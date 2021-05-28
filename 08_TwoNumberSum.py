a = 3
b = 3

A =[]
if a < b:
    A = list(range(a,b+1))
else:
    A = list(range(b,a+1))
answer = sum(A[:len(A)])

if a == b:
    answer = a
print(answer)