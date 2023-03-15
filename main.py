import restaraunt as rt
from price import Price
from sale import Sale
import datetime

restaraunt = rt.Restaraunt()

command = -1
while command != 0:
    print(
        "0 - Выход из программы." +
        "1 - Вывести меню с ценами" +
        "2 - Вывести список всех блюд" + 
        "3 - Вывести историю цен по блюду" + 
        "4 - Добавить блюдо" +
        "5 - Поставить новую цену на блюдо" +
        "6 - Продать блюдо" + 
        "7 - Вывести сегодняшнюю выручку" +
        "8 - Вывести выручку за период" +
        "9 - Изменить цену на предыдущем периоде"
    )
    command = int(input())
    match command:
        case 1:
            for price in rt.date_prices(restaraunt.prices, restaraunt.work_date):
                print(price)
        case 2:
            for dish in restaraunt.dishes:
                print(dish)
        case 3:
            print("Введите название блюда.")
            for price in rt.prices_for_dish(restaraunt.prices, restaraunt.get_dish_by_name(input())):
                print(price)
        case 4:
            print("Введите название нового блюда.")
            restaraunt.dishes = rt.add_dish(restaraunt.dishes, input())
        case 5:
            print("Сперва выберите блюдо.")
            dish = rt.get_dish_by_name(restaraunt.dishes, input())
            if dish.name != "":
                print("Введите начало периода действия цены (не раньше текущего рабочего дня) в формате ггггммдд")
                date = datetime.datetime.strptime(input(), "%Y%m%d")
                print("Введите цену (целое число)")
                restaraunt.prices = rt.add_price(restaraunt.prices, Price(date, dish, int(input())))
        case 6:
            print("Введите название блюда.")
            dish = rt.get_dish_by_name(restaraunt.dishes, input())
            print("Введите количество проданных блюд")
            restaraunt.sales.append(Sale(restaraunt.work_date, dish, int(input())))
        case 7:
            print(rt.calculate(restaraunt.dishes, restaraunt.sales, restaraunt.prices, restaraunt.work_date))
        case 8:
            print("Введите начало периода в формате ггггммдд")
            startDate = datetime.datetime.strptime(input(), "%Y%m%d")
            print("Введите конец периода в формате ггггммдд")
            endDate = datetime.datetime.strptime(input(), "%Y%m%d")
            print(rt.calculate_period(restaraunt.dishes, restaraunt.sales, restaraunt.prices, startDate, endDate))
        case 9:
            print("Сперва выберите блюдо.")
            dish = rt.get_dish_by_name(restaraunt.dishes, input())
            if dish.name != "":
                print("Введите начало периода действия цены в формате ггггммдд")
                startDate = datetime.datetime.strptime(input(), "%Y%m%d")
                print("Введите конец периода действия цены в формате ггггммдд")
                endDate = datetime.datetime.strptime(input(), "%Y%m%d")
                print("Введите цену (целое число)")
                restaraunt.prices = rt.add_price_to_past(restaraunt.prices, Price(startDate, endDate, dish, int(input())))