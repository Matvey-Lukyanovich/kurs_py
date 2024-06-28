import random
list1 = []
for i in range(10):
    list1.append(random.randint(-10,10))
print(list1)
sum1=0

for i in list1:
    if i>=0:
        sum1+=i
print(sum1)
print()
print("#2")
mas = list1
print(sum(mas)/len(mas))
for i in mas:
    if i< (sum(mas)/len(mas)):
        print(i)
