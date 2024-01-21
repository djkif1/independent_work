# todo конкатенація може буті додавання (стр +стр) і може бути множеня (стр * інт)

# var = "5"
# var_1 =12
# print(int(var)* var_1)# 60
# print(var * var_1) # 555555555555
# print(str(var_1) +var) # 125


# var_a = "new"
# var_b = "student"
# print(var_a, var_b)# new student
# print(var_a+var_b)# newstudent


# first_1 =20
# first_2 = 10
# print(first_1)
# print(first_2)

##todo Синтаксичний цукор
# first_1, first_2 = first_2, first_1
# print(first_1)


# # множинне присвоєння
# a,b,c = 10,12,15
# print(a,b,c)
#
# #степінь
# print(2**3)
#
# #квадратний корінь
# print(25**0.5)

# todo (Built-in) - это функции встроенные в интерпретатор Python
#   и для их использования в программах не надо импортировать модули

# todo Тип данних bool. Пишеться з великої літери True, False будьте уважні
# var = True
# var_1 = False

# print(bool(""))
# print(bool(" "))
# print(bool("0"))
# print(bool(0))

# todo Тип данних "None"

# var = None
# print(type(var), var)
# print(bool(var))

# todo: Математичні порівняння
# ==, != - порівняння по значенню

# var = 3
# var_1 = 5
# var_2 = var
# print(var > var_1) # білше
# print(var < var_1) # менше
# print(var >= var_1) # білше,або дорівнює
# print(var <= var_1) # менше,або дорівнює
# print(var_2 != var) # не дорівнює
# print(var_2 == var) # перевіряє на рівність
# print(var == 3.0)


# todo: is, not - порівняння по id

# var = 3
# print(var is 3) #True
# print(5 is 5.0) #False перевіряє id, а не значення і тип
# print(not True) #False обертає значення навпаки
# print(True is True) #True
# print(not (True is True))# False обертає значення навпаки


# todo: перевірка ID
# в пайчармі і в терміналі можуть бути різні результати

# var =200
# var_1 =199+1
# print(id(var))
# print(id(var_1))
#
# var = 20000
# var_1 = 19999+1
# print(id(var))
# print(id(var_1))


# todo: Конструкція if/else

# var = int(input("Enter number:"))
# var_1 = 5
# if var < var_1:
#     print("var > var_1")
# else:
#     print("var not > var_1")
# print("block passed")

#todo: Вкладений if

# age = int(input("How old are you? :"))
#
# if age < 18:
#     print("Entrance blocked! ")
# else:
#     if age >= 21:
#         print("You can by alcohol. ")
#     else:
#         print("Alcohol is not allowed!\n Eat ice cream!")

#todo: elif

# if age < 18:
#     print("Entrance blocked! ")
# elif age >=21:
#     print("You can by alcohol. ")
# else:
#     print("Alcohol is not allowed!\n Eat ice cream!")# shift+tab здвигає виділене на 1 tab в ліво

#todo: методи str .title() , .upper() , lower()

# name = input("Please, type your password: ")
# if name.title() == "Igor":
#     print("Welcome")
# else:
#     print("sorry, access deny!")
#
# print(name.title())#Admin
# print(name.upper())#ADMIN
# print(name.lower())#admin

#todo: replace("int", "float") підміняє вибраний символ/символи на інші,  в данному випадку "int" на "float"

url = "https://project/prod.com"
print(url)
print(url.replace("prod","qa"))# https://project/qa.com заміна "prod" на "qa"
new_url = url.replace("prod", "automation/kqa") # зберігаємо новий урл в змінну
print(new_url)
url_1 = url.replace("prod","") # вирізаємо не потрідний шматок стрічки/урла чи чогось що не потрібно
print(url_1)










