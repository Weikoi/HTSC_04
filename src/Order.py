from Beverage import *


class Order(object):
    def __init__(self):
        self.order_list = []

    def __repr__(self):
        return self.order_list

    def add_order(self, beverage):
        self.order_list.append(beverage)

    def calculate(self):
        sum_price = 0
        for beverage in self.order_list:
            sum_price += beverage.get_price()
        return sum_price
