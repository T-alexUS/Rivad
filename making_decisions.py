# #Задание 1
# def task1():
#     number = int(input('Введите целое число\n'));
#     if number % 2 == 0:
#         print('Вы ввели четное число');
#     else:
#         print("Вы ввели нечетное число");
    
# task1();

# #Задание 2
# def task2():
#     letter = input('Введите любую букву латинского алфавита\n');
#     if letter == 'a' or 'e' 'i' or 'o' or 'u':
#         print('Вы ввели гласную букву');
#     else:
#         print('Вы ввели согласную букву');

# task2();

# def task3():
#     number_of_ribbers = int(input('Введите количество ребер фигуры от 3 до 10\n'));
#     if number_of_ribbers == 3:
#         print('Треугольник');
#     elif number_of_ribbers == 4:
#         print('Четырехугольник');
#     elif number_of_ribbers == 5:
#         print('Пятиугольник');
#     elif number_of_ribbers == 6:
#         print('Шестиугольник');
#     elif number_of_ribbers == 7:
#         print('Семиугольник');
#     elif number_of_ribbers == 8:
#         print('Восьмиугольник');
#     elif number_of_ribbers == 9:
#         print('Девятиугольник');
#     elif number_of_ribbers == 10:
#         print('Десятиугольник');
#     else:
#         print("Вы ввели неверное количество сторон. Читайте лучше");

# task3();

# def task4():
#     month = input('Введите название месяца\n')
#     if month == "январь" or month == "Январь":
#         print('В указанном месяце 31 день');
#     elif month == "февраль" or month == 'Февраль':
#         print('В указанном месяце 28 или 29 дней');
#     elif month == 'март' or month == 'Март':
#         print('В указанном месяце 31 день');
#     elif month == 'апрель' or month == 'Апрель':
#         print('В указанном месяце 30 дней');
#     elif month == 'май' or month == 'Май':
#         print('В указанном месяце 31 день');
#     elif month == 'июнь' or month == 'Июнь':
#         print('В указанном месяце 30 дней');
#     elif month == 'июль' or month == 'Июль':
#         print('В указанном месяце 31 день');
#     elif month == 'август' or month == 'Август':
#         print('В указанном месяце 31 день');
#     elif month == 'сентябрь' or month == 'Сентябрь':
#         print('В указанном месяце 30 дней');
#     elif month == 'октябрь' or month == 'Октябрь':
#         print('В указанном месяце 31 день');
#     elif month == 'ноябрь' or month == 'Ноябрь':
#         print('В указанном месяце 30 дней');
#     elif month == 'декабрь' or month == 'Декабрь':
#         print('В указанном месяце 31 день');
#     else:
#         print('Повторите ввод');

# task4();

# #Задание 5
# def task5():
#     a = float(input('Введите длину 1-ой стороны треугольника\n'));
#     b = float(input('Введите длину 2-ой стороны треугольника\n'));
#     c = float(input('Введите длину 3-ей стороны треугольника\n'));
#     if a == b and a == c and c == b:
#         print('Треугольник равносторонний');
#     elif a == b or a == c or b == c:
#         print('Треугольник равнобедренный');
#     else:
#         print('Треугольник разносторонний');

# task5();

#Задание 8
def task8():
    month = input('Введите месяц года\n');
    day = input('Введите день вышеуказанного месяца\n');
    if ((month == 'март' and day >= 20) or month == 'апрель' or month == 'май' or (month == 'июнь' and day <= 20)):
        print('Данный день входит в весенний сезон');
    elif ((month == 'июнь' and day >= 21) or month == 'июль' or month == 'август' or (month == 'сентябрь' and day <= 21)):
        print('Данный день входит в летний сезон')
    elif ((month == 'сентябрь' and day >= 22) or month == 'октябрь' or month == 'ноябрь' or (month == 'декабрь' and day <= 20)):
        print('Данный день входит в осенний сезон')
    elif ((month == 'декабрь' and day >= 21) or month == 'январь' or month == 'февраль' or (month == 'март' and day <= 19)):
        print('Данный день входит в зимний сезон')

task8();


