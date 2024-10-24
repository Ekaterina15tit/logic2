slovo = (input('Слово:'))
a = slovo.count('a') 
e = slovo.count('e')
i = slovo.count('i')
o = slovo.count('o')
u = slovo.count('u')
y = slovo.count ('y')
if a == 0:
    print ("False")
elif e == 0:
    print ("False")
elif i == 0:
    print ("False")
elif o == 0:
    print ('False')
elif u == 0:
    print ('False')
elif y == 0:
    print ('False')
else: 
    print ('Все гласные на месте )')
print (f'Кол-во гласных в слове: {a+e+i+o+u+y}')
print (f'Кол-во согласных в слове: {len(slovo)-(a+e+i+o+u+y)}')
