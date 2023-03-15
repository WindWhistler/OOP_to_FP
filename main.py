from restaraunt import Restaraunt
from price import Price
from sale import Sale
import datetime

restaraunt = Restaraunt()

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
            for price in restaraunt.date_prices(restaraunt.work_date):
                print(price)
        case 2:
            for dish in restaraunt.dishes:
                print(dish)
        case 3:
            print("Введите название блюда.")
            for price in restaraunt.prices_for_dish(restaraunt.get_dish_by_name(input())):
                print(price)
        case 4:
            print("Введите название нового блюда.")
            restaraunt.add_dish(input())
        case 5:
            print("Сперва выберите блюдо.")
            dish = restaraunt.get_dish_by_name(input())
            if dish.name != "":
                print("Введите начало периода действия цены (не раньше текущего рабочего дня) в формате ггггммдд")
                date = datetime.datetime.strptime(input(), "%Y%m%d")
                print("Введите цену (целое число)")
                restaraunt.add_price(Price(date, dish, int(input())))
        case 6:
            print("Введите название блюда.")
            dish = restaraunt.get_dish_by_name(input())
            print("Введите количество проданных блюд")
            restaraunt.sales.append(Sale(restaraunt.work_date, dish, int(input())))
        case 7:
            print(restaraunt.calculate(restaraunt.work_date))
        case 8:
            print("Введите начало периода в формате ггггммдд")
            startDate = datetime.datetime.strptime(input(), "%Y%m%d")
            print("Введите конец периода в формате ггггммдд")
            endDate = datetime.datetime.strptime(input(), "%Y%m%d")
            print(restaraunt.calculate_period(startDate, endDate))
        case 9:
            print("Сперва выберите блюдо.")
            dish = restaraunt.get_dish_by_name(input())
            if dish.name != "":
                print("Введите начало периода действия цены в формате ггггммдд")
                startDate = datetime.datetime.strptime(input(), "%Y%m%d")
                print("Введите конец периода действия цены в формате ггггммдд")
                endDate = datetime.datetime.strptime(input(), "%Y%m%d")
                print("Введите цену (целое число)")
                restaraunt.add_price_to_past(Price(startDate, endDate, dish, int(input())))