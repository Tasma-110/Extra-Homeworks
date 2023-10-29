import math

a = int(input())
b = int(input())
c = int(input())

D = b*b - 4*a*c
if D<0:
    print(0)
if D>0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(x1, " ", x2)
if D==0:
    print(-b/(2*a))

