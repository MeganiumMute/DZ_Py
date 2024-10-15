items = {
 'milk15':{'name': 'молоко 1.5%', 'count': 34, 'price': 89.9},
 'cheese':{'name': 'сыр молочный 1 кг.', 'count': 12, 'price': 990.9},
 'sausage':{'name': 'колбаса 1 кг.', 'count': 122, 'price': 1990.9}
}
schet_1=0
result={}
keys_1lv=items.keys()
for it in keys_1lv:
    keys_2lv=items[it].keys()
    break

for i in keys_2lv:
    schet_1+=1
    if schet_1==2:
        for y in keys_1lv:
            if items[y][i]>20:
                result[y]=False
            else:
                result[y]=True