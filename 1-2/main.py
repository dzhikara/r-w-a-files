def cook_book():  # задача 1
    with open("recipes.txt", encoding="utf-8") as file:
        cook_book = {}
        for line in file.read().split("\n\n"):
            name, _, *args = line.split("\n")
            cook_list = []
            for arg in args:
                ingredient_name, quantity, measure = map(
                    lambda x: int(x) if x.isdigit() else x, arg.split(" | ")
                )
                cook_list.append(
                    {
                        "ingredient_name": ingredient_name,
                        "quantity": quantity,
                        "measure": measure,
                    }
                )
            cook_book[name] = cook_list
    return cook_book


print(cook_book())


def get_shop_list_by_dishes(dishes, person_count):  # задача 2
    shop_list = {}
    cb = cook_book()
    for dish in dishes:
        if dish in cb:
            for ingredient in cb[dish]:
                ingredient_name = ingredient["ingredient_name"]
                quantity = ingredient["quantity"] * person_count
                measure = ingredient["measure"]
                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = {
                        "quantity": quantity,
                        "measure": measure,
                    }
                else:
                    shop_list[ingredient_name]["quantity"] += quantity
    return shop_list


result = get_shop_list_by_dishes(["Запеченный картофель", "Омлет"], 2)
print(result)
