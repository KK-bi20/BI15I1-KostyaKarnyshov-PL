# Площадь прямоугольного треугольника
a = int(input())
b = int(input())
print ("Площадь: " +str(a * b / 2))

# Сумма трёх чисел
a = int(input())
b = int(input())
c = int(input())
print ("Сумма: "+str(a + b + c))

# Дележ яблок
n = int(input())
k = int(input())
print( k // n)
print(k % n)

# Электронные часы
n = int(input())
hours = n % (60 * 24) // 60
minutes = n % 60
print(hours, minutes)

# Парты
import math

stdNum1 = int(input())
stdNum2 = int(input())
stdNum3 = int(input())
table = math.ceil((stdNum1+stdNum2+stdNum3)/2)
print("Парты: " +str(table))

# Шнуровка
a = int(input())
b = int(input())
L = int(input())
N = int(input())
print(2 * L + (2 * N - 1) * a + 2 * (N - 1) * b)

# Лекция №2
# Задача 1
a = int(input())
b = int(input())

while b >= a:
  print (a)
  a+=1

# Задача 2
a = int(input())
b = int(input())

if b>a:
	while b >= a:
		print (a)
		a+=1
else:
	while a >= b:
		print (a)
		a-=1

# Задача 3
a = int(input())
b = int(input())
if a > b:
  for i in range(b, a+1):
    if(i % 2 != 0):
      print(i)
else:
  print("Ошибка")

# Задача 4
sum = 0
for i in range(10):
    number = int(input())
    sum += number
print(sum)

# Задача 5
n = int(input())
sum = 0
for i in range(n):
    sum += int(input())
print(sum)

# Задача 6
h1 = int(input('Часы1: '))
m1 = int(input('Минуты1: '))
s1 = int(input('Секунды1: '))
h2 = int(input('Часы2: '))
m2 = int(input('Минуты2: '))
s2 = int(input('Секунды2: '))
if h1 < h2:
    print((h2-h1)*3600 + (m2-m1)*60 + (s2-s1))
else:
    print("Ошибка")

# Задача 7
import math

a = int(input())
b = int(input())

print("Гипотенуза = "+str(math.sqrt(a*a + b*b)))

# Задача 8
p = int(input('Процент годовых = '))
x = int(input('Рублей = '))
y = int(input('Копеек = '))
money_before = 100 * x + y
money_after = int(money_before * (100 + p) / 100)
print((money_after // 100), (money_after % 100))

# Задача 9
print(input().count(' ') + 1)

# Задача 10
s = input()
print(s[ (len(s) + 1) // 2: ] + s[ :(len(s) + 1) // 2 ])

# Задача 11
s = input()
first_word = s[:s.find(' ')]
second_word = s[s.find(' ') + 1: ]
print(second_word + ' ' + first_word)

# Задача 13
s = input()
b = s.find('h') 
e = s.rfind('h')  
print(s[:b] + s[e + (e != -1):])

# Задача 14
s = input()
t = ''
for i in range(len(s)):
    if i % 3 != 0:
        t = t + s[i]
print(t)

# Задача 15
A = int(input('Введите A: '))
x = x1 = 1
s = 2
while True:
   b = x
   x = x1
   x1 += b
   s += 1
   if x1 == A:
        print(s)
        break
   elif x1 > A :
        print(-1)
        break