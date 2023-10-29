a = int(input("Введите номер урока (от 1 до 10): "))

result = a*45 + (a//2)*5 + ((a-1)//2)*15

print(result//60 + 9, result%60)



