# date
import datetime
from dish import Dish
from price import Price
from sale import Sale

class Restaraunt():
    def __init__(self, new_dishes = [], new_prices = [], new_sales = [], new_work_date = datetime.date.today()):
        self.dishes = new_dishes
        self.prices = new_prices
        self.sales = new_sales
        self.work_date = new_work_date

def add_price(prices, price, work_date):
    new_prices = prices.copy()
    if(price.dateStart < work_date):
        print("Incorrect date. Can't add prices for closed period.")
    else:
        new_prices = cut_last_price_date(new_prices, price.dish, price.dateStart)
        new_prices.append(price.copy())
    return new_prices

def cut_last_price_date(prices, dish, date):
    new_prices = prices.copy()
    for price in prices:
        if price.dish.name == dish.name and day_of_sale <= price.dateEnd and day_of_sale >= price.dateStart:
            price.dateEnd = price.DateStart - datetime.timedelta.days(1)
    return new_prices

def add_price_to_past(prices, new_price):
    new_prices = prices.copy()
    for old_price in new_prices:
        if (old_price.dish == new_price.dish 
            and old_price.dateStart >= new_price.dateStart 
            and old_price.dateEnd <= new_price.dateEnd
            ):
            new_prices.remove(old_price)
        if (old_price.dish == new_price.dish 
            and old_price.dateStart < new_price.dateStart 
            and old_price.dateEnd <= new_price.dateEnd):
            old_price.dateEnd = new_price.dateStart - datetime.timedelta.days(1)
        if (old_price.dish == new_price.dish 
            and old_price.dateStart >= new_price.dateStart 
            and old_price.dateEnd > new_price.dateEnd):
            old_price.dateStart = new_price.dateEnd + datetime.timedelta.days(1)
    new_prices.append(new_price.copy())
    return new_prices


def add_dish(dishes, dish):
    new_dishes = dishes.copy()
    if get_dish_by_name(dishes, dish.name).name == "":
        new_dishes.append(dish.copy())
    else: 
        print("Dish with such name already exists.")
    return new_dishes

def get_dish_by_name(dishes, search_name):
    for dish in dishes:
        if dish.name == search_name :
            return dish.copy()
    return Dish("")

def dish_date_sales(sales, dish, date):
    sales_for_dish = []
    for sale in sales:
        if sale.dish.name == dish.name and sale.date == date:
            sales_for_dish.append(sale)
    return sales_for_dish

def date_sales(sales, date):
    sales_on_date = []
    for sale in sales:
        if sale.date == date:
            sales_on_date.append(sale)
    return sales_on_date

def price_for_dish_on_day(prices, dish, day_of_sale):
    for price in prices:
        if price.dish.name == dish.name and day_of_sale <= price.dateEnd and day_of_sale >= price.dateStart:
            return price.copy()

def prices_for_dish(prices, dish):
    new_prices = []
    for price in prices:
        if price.dish.name == dish.name:
            new_prices.append(price.copy)
    return new_prices

def date_prices(prices, date):
    prices_on_date = []
    for price in prices:
        if price.dateStart < date and price.dateEnd > date:
            prices_on_date.append(price)
    return prices_on_date

def calculate(dishes, sales, prices, day_of_calc):
    money = 0
    # will calculate for each dish separately
    for dish in dishes:
        for sale in dish_date_sales(sales, dish, day_of_calc):
            money += sale.amount * price_for_dish_on_day(prices, dish, sale.date).price
    return money

def calculate_period(dishes, sales, prices, dateStart, dateEnd):
    money = 0
    date_ind = dateStart
    while(date_ind < dateEnd):
        money += calculate(dishes, sales, prices, date_ind)
        date_ind += datetime.timedelta.days(1)
    return money

def nextDay(restaraunt_in):
    return Restaraunt(
        restaraunt_in.dishes,
        restaraunt_in.prices,
        restaraunt_in.sales,
        restaraunt_in.work_date + datetime.timedelta.days(1))