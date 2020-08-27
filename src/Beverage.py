class Beverage(object):

    def __init__(self, spec):
        self.spec = spec


class Coffee(Beverage):
    def __init__(self, coffee_spec):
        Beverage.__init__(self, coffee_spec)

    def get_price(self):
        base_price = self.get_base_price(self.spec["base_type"])
        syrup_num = int(self.spec["original_syrup"]) + int(self.spec["vanilla_syrup"]) + int(self.spec["acorn_syrup"]) + \
                    int(self.spec["caramel_syrup"]) + int(self.spec["raspberry_syrup"]) + int(self.spec["mocha_syrup"])
        sauce_num = int(self.spec["mocha_sauce"]) + int(self.spec["caramel_sauce"])
        return base_price + 3 * int(syrup_num) + 4 * int(sauce_num)

    @staticmethod
    def get_base_price(base_type):
        if base_type == "1":  # latte
            return 10
        elif base_type == "2":  # mocha
            return 11
        elif base_type == "3":  # white
            return 12
