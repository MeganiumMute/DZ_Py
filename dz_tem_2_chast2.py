# boys=['Peter','Alex','john','Arthur','Richard',]
# girls=['Kate','Liza','Kira','Emma','Trisha']
boys=(input('Введиет всех парней через ",":').split(', '))
girls=(input('Введиет всех парней через ",":').split(', '))
print(girls)
print(boys)
boys.sort()
girls.sort()
schet=0
if len(boys)==len(girls):
    print('Пары:\n')
    for item_boys in boys:
        while True:
            print(item_boys+':'+girls[schet])
            schet+=1
            break
else:
    print('Внимание, кто-то может остаться без пары.')