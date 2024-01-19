# Не пишітиь назви змінних укроїньською мовою

# змінна = 10 #BAD PRACTICE
# print(змінна)

# Правильний варіант
# variable = 25
# print(variable)
# print(type(variable))

var_1 = 42
var_2 = 5
var_3 = 5  # ctrl+d копіює стрічку на нижній рядок

# print(var_1 + var_2)# без збереження в змінну
#
# result = var_2 -var_1 #збереження результату в змінну (більш вірний варіант)
# print(result)

# залишок від ділення %
# result = var_1 % var_2 # 2
# print(result)
#
# # скільки разів ми змогли поділити націло //
# result = var_1 // var_2 # 8
# print(result)


# todo питання які питають на співбесіді : які типи данних є в python?  (Числові: int, float, complex)
#  (строчні: str) (Структуровані: tuple, dict, list, set) (NoneType: None)
#  Байтові і Спеціальні


#STR


# sample_text = "Привіт мене звуть Олександр"
# print(sample_text)
# print(type(sample_text))


# semple_text = "999"
# semple_text_1 ="1"
# print(type(semple_text))
# print(semple_text_1 + semple_text) # конкатенація

age = input("Скільки вам років?")# Запитуеє в користувача (відкриває поле для вводу)
print(age)
print(type(age))# повертае str тип данних

