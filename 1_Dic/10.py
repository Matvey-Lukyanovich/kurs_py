n = int(input('Введите число: '))
mas = [1,2]
for i in range(1,n-1):
   mas.append((mas[i-1]+mas[i]))
print(mas)

sum=1

for i in range(1, n+1):
    sum *= i
print(f"факториал:{n}! равен {sum}")