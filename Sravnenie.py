print (2>1)
print (type(2>1))


print ('string'=="string")

x ="string"
y = "String"
print(x.lower()==y.lower())

print ( 1<2>3)
print ( 1<2<3)
print ( 1 < 2 and 2 > 3)
print ( 1 > 2 or 2 < 3)

is_admin = True 
file_exist = True

should_open_file= is_admin and file_exist
print(should_open_file)

is_admin = False
if not is_admin:
    print('not admin')

if is_admin == False:
    print('not an admin')