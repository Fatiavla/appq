print('My name is {}'.format('Vlad'))

my_name = 'Vlad' 
print('My name is {}'.format(my_name))

print('My name is {} and I`m {}'.format('Vlad', 25))

print('My name is {0} and I`m {1}'.format('Vlad', 25))

print('My name is {1} and I`m {0}'.format('Vlad', 25))

pi = 3.1415
print(pi)
                    #.2 - то что хотим вывести только 2 числа после запятой
                        #f - форматирование числа (Флоатинг)
                    #1 - не хотим дополнять число пробелами
print('Pi equals {pi:1.2f}'.format(pi=pi))
print('Pi equals {pi:5.2f}'.format(pi=pi))

name = "Vlad"
age = 30
print(f"My name is{name} and I`m {age}") #интрополяция строк

print(f"Pi equals {pi:1.2f}")