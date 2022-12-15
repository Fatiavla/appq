numbers = [5, 2, 7]
numbers.append(100) #Добавляет значение
print('Добавление 1 значения в список - append ')
print(numbers)
numbers.insert(1, False) #Добавляет значение по индексу
print('Добавление значения по индексу в список - numbers.insert ')
print(numbers)
numbers.extend([5, 6, 8]) # Добавляет несколько символов в писок
b = [2, 3, 4]
numbers.extend(b)
print('Добавляение несколько символов в список - numbers.extend')
print(numbers)
numbers.sort() #Сортировка списка
print('Сортировка списка - numbers.ort ')
print(numbers)
numbers.reverse() # Переворот списка
print('Переворот списка - numbers.reverse')
print(numbers)
numbers.pop() # пустая - удаляет послений элемент
print('Удаляет последний элемент списка или по индексу () - numbers.pop')
print(numbers)
numbers.remove(100)
print('Удаляет назначенный элемент из списка - numbers.remove')
print(numbers)
# numbers.clear()
print('Полностью очистить список - numbers.clear (Закоментировал)')
# print(numbers, ' <--')
print('Посчитать кол-во элементов в списке - numbers.count()')
print(numbers.count(5))
print('Показывает длину всего списка - len(numbers)')
print(len(numbers))
