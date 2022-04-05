#Задача 1
def task1():
    print('Alexey');
    print('Адрес не скажу!!!');

task1();

#Задача 2
def task2():
    name = input('Введите ваше имя\n')
    print(f"Желаю здравствовать, {name}.");

task2();

#Задача 3
def task3():
    width = float(input("Какая ширина комнаты\n"));
    length = float(input('Какая длина комнаты\n'));
    area = width * length;
    print(f"Площадь комнаты - {area} м2");

task3()

#Задача 4
def task4():
    width = float(input("Какая ширина участка\n"));
    length = float(input('Какая длина участка\n'));
    area = round(width * length / 43560, 5);
    print(f"Площадь участка в акрах - {area}");

task4();

#Задача 5
def task5():
    lessALitter = float(input("Сколько бутылок объемом 1 литр и меньше\n"));
    moreThanALitter =float(input("Сколько бутылок объемом больше литра\n"));
    sum = float(lessALitter * 0.1 + moreThanALitter * 0.25);
    sum = round(sum, 2);
    print(f"Вы сдали бутылок на сумму {sum} $")

task5();