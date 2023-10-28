print("Добро пожаловать, вы заполняете анкету")

user_first_name = input("Введите ваше имя:")
user_last_name = input("Введите вашу фамилию:")
user_birthdate = input("Ввидте ваш год рождения:")
user_feedback = input("Нравится ли вам наш курс?:")
course_expectations = input("Что вы ожидете в дальнейших занятиях?:")

print("Вы заполнили такие данные:")
print("Вас зовут: ",user_first_name)

user_age = 2023-int(user_birthdate)
if 1<= user_age%10 <=4:
    print("Вам ", user_age," года")
else:
    print("Вам ", user_age," лет")

print("Ваш ответ к первому вопросу : ",user_feedback)
print("Ваш ответ на второй вопрос: ", course_expectations)
