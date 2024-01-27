# age = 18
# # else if ,elif
# if age <= 50:
#     print("!!!")


# int_num =100
# if int_num > 10:
#     print(">10")
# elif int_num > 100:
#     print(">100")

# todo Розбір на просту структуру

# print(True or True)#True
# print(True or False)#True
# print(False or False)#False
# print(True and False)#False
# print(False and False)#False
# print(True and 1)# 1
# print(True and bool(1))


# todo round() - Округляє

# print(0.0001 + 0.0002)# глюк pythonA
# print((1+2)/10000)# перший варіант рішення
# #import decimal - імпорт нового типу данних який працює без помилок
# a = 0.0001+0.0002
# print(a)
# a=round(a,5)
# print(a)

# todo in str

# str_a = "knkl Klkj nnjfhgfhgf"
# print("jfh" in str_a)  # True #перевірка чи входе текст в стрічку, чутливий до регістру

# todo: f string

# name = "Ivan"
# age = 32
# print(f"Hi {name}, you are {age} old")###

# todo:len() повертає кількість елементів
# print(len("any text"))# 8 elements


# todo: strip(), lstrip(), rstrip()

# str= "+++asd+++asd+++"

# print(str.strip("+"))# = asd+++asd видаляє з 2х сторін
# print(str.rstrip("+"))# = +++asd+++asd видаляє зправа
# print(str.lstrip("+"))# = asd+++asd+++ видаляє зліва

# todo: .count(), .isdigit(), .find(), .isalpha()

# str_1 = "+++asd+++asd+++"
# print(str_1.count("+")) # показує скілки обраних елементів в змінній/об'єкті

# str_1= "999"
# str_2= "str"
# print(str_1.isdigit()) # використовуеться тільки з стр, перевіряє щоб строка була тільки з цифр
# print(str_2.isalpha()) # використовуеться тільки з стр, перевіряє щоб строка була тільки з літер
# print(str.find())


# num_1 = "999"
# int_2 = "str"
# print(num_1.isdigit())
# print(int_2.isdigit())
#
# var_1= input()
# var_2= input()
#
# if var_1.isdigit() and var_2.isdigit():
#     print((int(var_1)+int(var_2))*3)
# else:
#     print("Мипрацюємо тільки з цілими числами")

# todo: Зрізи в str

# string_a= "123456789012345678901"
# var= 10
# print(string_a[0])# звертаємось до першого елементу
# print(string_a[3])# звертаємось до четвертого елементу
# print(string_a[0:8])# виводимо з 1го по 7й елемент, останній елемент не показує
# print(string_a[2:var])# виводимо з 2го по вказаний в змінній
# print(string_a[:8])# виводимо з 1го по вказаний
# print(string_a[3:])# виводимо з вказаного по останній
# print()
# print(string_a[-1:])# виводимо останній елемент
# print(string_a[-5:-3])# виводимо з -5го по -3й елементи
# print(string_a[::2])# 3й параметр вказує на крок виводу - тут буде показувати кожен 2й символ
# print(string_a[len(string_a)//2+1:])# вираховуемо середину , додаємо +1 символ і виводимо

# todo: приоритети операцій
# print(1 + 2 * 3)
# print((1 + 2) * 3)
# () - Дужки
# ** - Піднесення до степеня
# +x, -x, ~x - Унарні плюс, мінус і бітове заперечення
# *, /, //, %
# *, /, //, % - Множення, ділення, цілочисельне ділення, остача від ділення
# +, - - Додавання та віднімання
# <<, >> - Бітові зсуви
# & - Бітове І (AND)
# ^ - Бітове виключне АБО (XOR)
# | - Бітове АБО (OR)
# ==, !=, >, >=, <, <=, is, is not, in, not in - Порівняння, перевірка ідентичності, перевірка належності
# not - Логічне НЕ (NOT)
# and - Логічне І (AND)
# or - Логічне АБО (OR)


# todo: list





# .split("/")
