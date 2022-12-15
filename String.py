print('123adc'.isalnum())
print('123abc!'.isalnum()) # состоит ли строка из букв и цифр

print('123'.isalpha()) # Есть ли буквы в строке
print('abc'.isalpha())

print(' '.isspace()) # есть ли в строке пустой элемент
print(''.isspace())

empty_string = ""
print(empty_string == '')

empty_string = " "
print(empty_string.strip(' ')) #удаляет с конца строки ( в примере удаляем пробел)

if not empty_string:
    print('not empty')
else:
    print('empty')


h = "hello"
print(h.startswith('he')) # проверяет начинает ли строчка с определенной строки
print(h.endswith('lo'))

split = h.split('l') # разделитель списка
print(split)
split = h.split('e') # удаляет указанный символ
print(split)

data = '12;10;8;10'
split_data = data.split(';')
print(split_data)

python = 'Python is fun'
print(python.partition('is ')) # это и сверху все сипаратор
print(python.partition('not '))

python = 'Python is fan, isn`t it'
print(python.partition('is'))


