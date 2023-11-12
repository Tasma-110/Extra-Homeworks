def calc():
    while True:
        print("Available options: ")
        print("1. a + b ")
        print("2. a - b ")
        print("3. a * b ")
        print("4. a / b ")
        print("5. a % b ")
        print("6. Exit ")
        print("Enter option: ")

        user_input = input()

        if user_input.isdigit():
            user_number = int(user_input)

            if user_number == 6:
                print("Выход из программы.")
                break

            if user_number in [1, 2, 3, 4, 5]:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))

                if user_number == 1:
                    print(f"{num1} + {num2} = {num1 + num2}")
                elif user_number == 2:
                    print(f"{num1} - {num2} = {num1 - num2}")
                elif user_number == 3:
                    print(f"{num1} * {num2} = {num1 * num2}")
                elif user_number == 4:
                    if num2 != 0:
                        print(f"{num1} / {num2} = {num1 / num2}")
                    else:
                        print("Ошибка: деление на ноль.")
                elif user_number == 5:
                    if num2 != 0:
                        print(f"{num1} % {num2} = {num1 % num2}")
                    else:
                        print("Ошибка: деление на ноль.")
            else:
                print("Ошибка: неверный ввод. Введите число от 1 до 6.")
        else:
            print("Ошибка: вы ввели строку. Для продолжения введите число.")


if __name__ == "__main__":
    calc()
