#level 1

'''x = float(input("Введите сумму вклада:\n"))
p = float(input("Введите процент:\n"))
y = int(input("Ожидаемая прибыль:\n"))
x1 = int(x)
num = 0
l = []

for i in range(x1, y+1):
	if x <= y:
		x += round(x*(p/100))                 Я пытался сделать так чтоб каждый год процент 
		num += 1                             считался не от х, а от результата в 12 строчке,
		if num not in l:                     но у меня ничего не получилось, поэтому 
			l.append(num)                    калькулятор вклада такой примитивный.

print("Через "+str(l[-1])+" лет сумма вклада будет не менее "+str(y))'''


#level 2

'''n = int(input("Введите число повторений:\n"))
x = 1
while x <= n:
	print("for - частный случай цикла while")
	x += 1'''


#level 3

'''num = input("Введите целое число:\n")
dell = list(map(int, num))
x = 0
for i in dell:
	x += i 
print(x)'''