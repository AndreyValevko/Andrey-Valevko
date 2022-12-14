# Mikhail Amshei
# Date: 02/02/2022
# Description: Homework 1
# Grodno IT Academy Python 3.9


#Напишите программу, ĸоторая считает общую цену.
#Вводится m рублей и n ĸопееĸ цена, а таĸже ĸоличество s товара.
#Посчитайте общую цену в рублях и ĸопейĸах за l товаров.
#Уточнение:
#Используйте функцию return чтобы ответ был в рублях и копейках.
#Ответ должен быть в формате: "Общая цена составляет M рублей и N копеек за L товаров"
def common_price(m, n, s, l):
    # Пишем наше решение здесь. В случае не верных данных возвращаем False
    m = float(input())
    n = float(input())
    s = float(input())
    l = float(input())
    if not type(m) == type(1):
        return False
    price = m * 100 + n
    price_per_unit = price // s
    final_price = price_per_unit * l
    m = final_price // 100
    n = final_price % 100
    return "Общая цена составляет " + str(m) + " рублей и " + str(n) + " копеек за " + str(l) + " товаров"

# Даны: три стороны треугольника.
# Требуется: проверить, действительно ли это стороны треугольника.
# Если стороны определяют треугольник, найти его площадь с точностью до четырёх десятичных.
# Пример: если строны треугольника равны 2, 2, 2 то мы должны вернуть 1.7321
# Если нет, вывести False.
# Бонус бал если с правильным возвратом мы ещё получим обьяснение в консоль почему это не треугольник.
def triangle(a, b, c):
    # Пишем наше решение
    a = float(input())
    b = float(input())
    c = float(input())
    if a + b > c and a + c > b and b + c > a:
        print('это треугольник')
    return False
