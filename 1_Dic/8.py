s = input('Введите число: ')
mul=1
sum=0

for i in range(len(s)):
    sum += int(s[i])
    mul *= int(s[i])

print("sum:", sum)
print("mul", mul)

start= int(input('Введите min: '))
end = int(input('Введите max: '))
step = int(input('Введите step: '))
for i in range(start, end+1, step):
    print(i)
