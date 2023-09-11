import json
from decorators import logger


# @logger
def get_shop_by_dishes(dishes, person_count):
    cook_book = {}
    with open('recipes.txt', 'r', encoding='UTF-8') as file_rec:
        for cook in file_rec:
            ingredient_count = int(file_rec.readline())
            cook_list = []
            for i in range(ingredient_count):
                ingredient_name, quantity, measure = file_rec.readline().strip().split(' | ')
                cook_list.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })
            cook_book[cook.strip()] = cook_list
            file_rec.readline()
    res = json.dumps(cook_book, indent=2, ensure_ascii=False)
    shop_list = {}
    for dish in dishes:
        list = cook_book.get(dish)  # список ингридиентов
        for l in list:
            dic = shop_list.get(l['ingredient_name'])
            if dic != None:
                dic['quantity'] = dic['quantity'] + l['quantity'] * person_count
                shop_list[ingredient_name] = dic
            else:
                shop_list[l['ingredient_name']] = {'measure': l['measure'], 'quantity': l['quantity'] * person_count}
    res = json.dumps(shop_list, indent=2, ensure_ascii=False)
    return res
