# #Задача 1
# def task1():
#     print('Alexey');
#     print('Адрес не скажу!!!');

# task1();

# #Задача 2
# def task2():
#     name = input('Введите ваше имя\n')
#     print(f"Желаю здравствовать, {name}.");

# task2();

# #Задача 3
# def task3():
#     width = float(input("Какая ширина комнаты\n"));
#     length = float(input('Какая длина комнаты\n'));
#     area = width * length;
#     print(f"Площадь комнаты - {area} м2");

# task3()

# #Задача 4
# def task4():
#     width = float(input("Какая ширина участка\n"));
#     length = float(input('Какая длина участка\n'));
#     area = round(width * length / 43560, 5);
#     print(f"Площадь участка в акрах - {area}");

# task4();

# #Задача 5
# def task5():
#     lessALitter = float(input("Сколько бутылок объемом 1 литр и меньше\n"));
#     moreThanALitter =float(input("Сколько бутылок объемом больше литра\n"));
#     sum = float(lessALitter * 0.1 + moreThanALitter * 0.25);
#     sum = round(sum, 2);
#     print(f"Вы сдали бутылок на сумму {sum} $")

# task5();

# #Задание 6
# def task6():
#     sum = float(input('Введите сумму вашего заказа\n'));
#     tips = float(sum * 0.18);
#     tips = round(tips,2)
#     tax = float(sum * 0.2);
#     tax = round(tax,2);
#     finalSum = sum + tax + tips;
#     finalSum = round(finalSum, 2)
#     print(f"Сумма налога составила {tax}");
#     print(f"Сумма чаевых составила {tips}")
#     print(f"Итоговая сумма - {finalSum}");

# task6();

# #Задание 7
# def task7():
#     number = float(input('Введите положительное натуральное число\n'));
#     sum = number * (number + 1) / 2;
#     print(f"Сумма первых n положительных чисел равна {sum}");

# task7();

# #Задание 8
# def task8():
#     bezdNumber = int(input(f"Сколько безедлушек вы приобрели\n"));
#     suvNumber = int(input(f"Сколкь сувениров вы приобрели\n"));
#     sum = suvNumber * 75 + bezdNumber * 112;
#     print(f"Общий вес покупки составил {sum} грамм");

# task8();

# #Задание 9
# def task9():
#     startingSum = float(input("Введите первоначальную сумму вклада\n"));
#     finalSum1 = startingSum * (1.04 ** 1);
#     finalSum1 = round(finalSum1, 2)
#     finalSum2 = startingSum * (1.04 ** 2);
#     finalSum2 = round(finalSum2, 2)
#     finalSum3 = startingSum * (1.04 ** 3);
#     finalSum3 = round(finalSum3, 2)
#     print(f"Сумма вклада на конец 1-го года - {finalSum1}");
#     print(f"Сумма вклада на конец 2-го года - {finalSum2}");
#     print(f"Сумма вклада на конец 3-го года - {finalSum3}");

# task9();

# #Задание 10
# import math;
# def task10():
#     a = float(input("Введите число а\n"));
#     b = float(input("Введите число b\n"));
#     print(f"сумма a и b: {a + b}")
#     print(f"разница между a и b: {a - b}")
#     print(f"произведение a и b: {a * b}")
#     print(f"частное от деления a на b: {a / b}")
#     print(f"остаток от деления a на b: {a % b}")
#     print(f"десятичный логарифм числа a: {math.log10(a)}")
#     print(f"результат возведения числа a в степень b: {a ** b}");

# task10();