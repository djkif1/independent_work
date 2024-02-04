goods = input("Введіть 5 необхідних товарів через пробіл: ").split(" ") # запитуємо список товарів і розділяємо
                                                                        # методом split() і записує в список
print("Список ваших товарів")

while goods:  #  віводимо нумерований список
    for index, element in enumerate(goods, start=1): # присвоюємо номер кожному елементу
        print(f"{index}. {element.title()}")

    del_goods = int(input("Введіть номер купленого товару (або 0 для виходу): ")) - 1

    if 0 <= del_goods < len(goods): # перевірка списка, якщо порожній то виходимо з 
        del goods[del_goods]
        print("\nСписок ваших товарів")
    elif del_goods == -1:
        break
    else:
        print("Некоректний номер. Спробуйте ще раз.")

print("Ви вийшли з програми або ваш список товарів порожній.")





#   banan chery lemon apple melon




















