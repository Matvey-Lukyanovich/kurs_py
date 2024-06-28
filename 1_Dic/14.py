import random
list1 = []
for i in range(10):
    list1.append(random.randint(-10,10))

print(list1)
print("Min")
print(min(list1))
print("Max")
print(max(list1))

a = int(input('a: '))
b = int(input('b: '))
for i in list1:
    if i in range(a,b+1):
        list1.remove(i)
print(list1)