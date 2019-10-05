#Сгенерировать случайное число с помощью randint и
# вывести его на экран
import random
random.randint(3,6)
print(random.randint(3,6))
#Дан список чисел [1,2,3,4,5,6]. Перемешать список с
# помощью функции random.shuffle и вывести 
#случайное число с помощью random.choice
import random
list=([1,2,3,4,5,6])
random.shuffle([1,2,3,4,5,6])
print(list)
print(random.choice([1,2,3,4,5,6]))
#Сгенерировать случайное число с плавающей точкой 
#с помощью random.random() и вывести его на
# экран
import random
random.random()
print(random.random())