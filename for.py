for i in range(1, 6, 2): #1 <- начальное, 6 <- до знач, 2 <- шаг знач
    print(i)

count = 0
world = 'Hello world!'
for t in world:
    if t == 'l':
        count+= 1
print('Count:', count)


for e in range(1, 11):
    if e == 5:
        break


    if e % 2==0:
        continue # пропускает итерацию, и продолжает цикл 

    print(e)

found = None #в переменную ничего не устанавливаем
for t in 'hello':
    if t == 'l':
        found = True
        break
else:
    found = False
print(found)