# date
import datetime
from dish import Dish
from price import Price
from sale import Sale

class Restaraunt():
    def __init__(self):
        dishes = []
        prices = []
        sales = []
        work_date = datetime.date.today()

    def add_price(self, price):
        if(price.dateStart < self.work_date):
            print("Incorrect date. Can't add prices for closed period.")
            return 0
        self.price_for_dish_on_day(price.dish, price.dateStart).dateEnd = price.DateStart - datetime.timedelta.days(1)
        self.prices.append(price)

    def add_dish(self, dish):
        if self.get_dish_by_name(dish.name).name == "":
            self.dishes.append(dish)
        else: 
            print("Dish with such name already exists.")

    def get_dish_by_name(self, search_name):
        for dish in self.dishes:
            if dish.name == search_name :
                return dish
        return Dish("")

    def dish_date_sales(self, dish, date):
        sales_for_dish = []
        for sale in self.sales:
            if sale.dish.name == dish.name and sale.date == date:
                sales_for_dish.append(sale)
        return sales_for_dish

    def date_sales(self, date):
        sales_on_date = []
        for sale in self.sales:
            if sale.date == date:
                sales_on_date.append(sale)
        return sales_on_date

    def price_for_dish_on_day(self, dish, day_of_sale):
        for price in self.prices:
            if price.dish.name == dish.name and day_of_sale <= price.dateEnd and day_of_sale >= price.dateStart:
                return price
    
    def price_for_dish(self, dish):
        return self.price_for_dish_on_day(dish, self.work_date)

    def prices_for_dish(self, dish):
        for price in self.prices:
            if price.dish.name == dish.name:
                return price

    def date_prices(self, date):
        prices_on_date = []
        for price in self.prices:
            if price.dateStart < date and price.dateEnd > date:
                prices_on_date.append(price)
        return prices_on_date

    def calculate(self, day_of_calc):
        money = 0
        # will calculate for each dish separately
        for dish in self.dishes:
            for sale in self.dish_sales(dish, day_of_calc):
                money += sale.amount * price_for_dish_on_day(dish, sale.date)
        return money
    
    def calculate_period(self, dateStart, dateEnd):
        money = 0
        date_ind = dateStart
        while(date_ind < dateEnd):
            money += self.calculate(date_ind)
            date_ind += datetime.timedelta.days(1)
        return money

    def nextDay(self):
        self.work_date += datetime.timedelta.days(1)