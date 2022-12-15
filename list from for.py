# nums = [5, 2, 7,'50', False]

# for el in nums:
#     el*=2
#     print(el)


n = int(input('Enter length: ')) #просим пользователя ввести длину списка
user_list = [] # это то, куда будем поещать список

i = 0
while i < n: #Через цикл заполняем список
    string = 'Enter element #' + str(i + 1) + ": " # ввод списка
    user_list.append(input(string))
    i+=1

print(user_list)