print("Стороны:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует")
else:
    print("Треугольник не существует")


n = int(input("n = "))

k = n
if n > 0 :
    k = n % 10

if k == 1 :
    print('мне ', n,' год')
elif k in range(2,5) :
    print('мне ', n, ' года')
elif k==0 or k in range(5,10):
    print('мне ', n, ' лет')