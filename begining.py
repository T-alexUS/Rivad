# Задача 1
def task1():
    print('Alexey');
    print('Адрес не скажу!!!');

task1();

def task2():
    name = input('Введите ваше имя\n')
    print(f"Желаю здравствовать, {name}.");

task2();

def task3():
    width = float(input("Какая ширина комнаты\n"));
    length = float(input('Какая длина комнаты\n'));
    area = width * length;
    print(f"Площадь комнаты - {area} м2");

task3()

def task4():
    width = float(input("Какая ширина участка\n"));
    length = float(input('Какая длина участка\n'));
    area = round(width * length / 43560, 5);
    print(f"Площадь участка в акрах - {area}");

task4();

