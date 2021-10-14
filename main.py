# 1

# while True:
#
#     x = int(input("Введите число от 1 до 9: "))
#     if x == 13:
#         break
#     elif 0 < x < 4:
#         s = str(input("Введите какую-нибудь строку: "))
#         n = int(input("Введите число повторов строки: "))
#         for i in range(n):
#             print(s)
#
#     elif 3 < x < 7:
#         m = float(input("Введите степень, в которую возведется введенное число: "))
#         print(pow(x, m))
#
#     elif 6 < x < 10:
#         for i in range(10):
#             x += 1
#             print(x, " ")
#
#     else:
#         print("Ошибка ввода")
#
#     print("Для выхода нажмите 13")
#
# print("Программа завершена")

# 2

while True:

    print("Общество в начале XXI века")
    x = (input("Введите Ваш возраст: "))
    if x.lower() == "q":
        break
    x = int(x)
    if -1 < x < 8:
        print("Вам в детский сад")

    elif 7 < x < 19:
        print("Вам в школу")

    elif 18 < x < 26:
        print("Вам в профессиональное учебное заведение")

    elif 25 < x < 61:
        print("Вам на работу")

    elif 60 < x < 121:
        print("Вам предоставляется выбор")

    else:
        for i in range(5):
            print("Ошибка! Это программа для людей")

    print("Для выхода нажмите q\n")

print("Программа завершена")
