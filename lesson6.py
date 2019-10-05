#Посчитать количество 9 в списке.
#L=[1,2,3,4,5,6,7,8,9,10]
#i=0
#while i < 9:
#i += 1
#	print(i)

l=[9,2,9,5,6,9,8,9,10]
i = 0
while i < len(l)-1:
	i += 1
	if l[i] == 9:
		print(l[i])
#Вывести количество четный и нечетных елементов в рандомной
#последовательности.
import random
l = []
for i in range(6):
	l.append(random.randint(1, 100))
print(l)
count_even = 0
cout_odd = 0
for elem in l :
	if elem%2 == 0:
		count_even += 1
	else:	
		cout_odd += 1
print(count_even)
print(cout_odd)	

#Пользователь должен ввести последовательность чисел через
 #пробел.Для каждого числа выведите слово YES
  #(в отдельной строке), если это число ранее встречалось
  # в последовательности или NO, если не встречалось.
a = int(input("Введите последовательность чисел"))
l = [1,2,1,1,3]
s = set()
for elem in l :
	if elem in l:
		print(yes)
	else:
		print(no)
		s.add(elem)	



	