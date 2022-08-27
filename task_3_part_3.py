#level 1

'''def area(a, b, c):
	p = (a + b + c)/2
	s = (p*(p-a)*(p-b)*(p-c))**0.5
	return s

print(area(6, 7, 2))'''



#level 2


'''import re
s = "Было просто пасмурно, дуло с севера А к обеду насчитал сто градаций серого. Так всегда первого ноль девятого То ли весь мир сошёл с ума, то ли я - того... На столе записка от неё смятая Недопитый виски допивают с матами. Посмотрю в окно, допишу главу Первое сентября, дворник жжёт листву. Серым облакам наплевать на нас Если знаешь как жить - живи Ты хотела плыть как все - так плыви!"
l= []

def lnth(s):
	redak = re.sub(r'[^\w\s]','', s.lower())    #код мой, но это:
	for i in redak.split():                     #re.sub(r'[^\w\s]','') - я нашёл на одном сайте
		if len(i) < 5:                          #можете её объяснить?
			l.append(i)                          
	print(l)

lnth(s)'''




#level 3

'''from random import randint
n = int(input("Сколько хотите сложить чисел?\n"))
m = []

def konk(n):
	for i in range(n):
		m.append(randint(1, 10000))
		str(m.sort(reverse = True))
		x = ""
		for i in m:
			x += str(i)
	print(x)

konk(n)'''