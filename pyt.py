# a = int(input('Write msg'))
# list = [1, 3, 4, 5, 6, 7, 8]
# list.reverse()
# print (list)

# list2 = [1, 4, 5, 6, 7, 7, 4, 3]
# list_new = list2[:: -1]
# print(list2)
# print(list_new)

# lisst = [1, 329, 34, 55, 26, 17, 8, 2, 5]
# new_try = list(sorted(lisst))
# print(lisst)
# print(new_try)

# list = [1, 3, 4, 5, 6, 7, 8]
# print(list[:-1])

data = input()
s = data.split(',') or data.split()
# if s == False:
#     print('Entre number with Space') 
# else:
#     A = [int(x) for x in s]
# list(map(int, A))
# A.reverse()
# print(type(A))

A = list(map(int, s))
print(A)