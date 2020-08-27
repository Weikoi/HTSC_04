class Beverage(object):

    def __init__(self, spec):
        self.spec = spec

    def get_prop(self, prop_name):
        return self.spec[prop_name]

    def get_all_props(self):
        return self.spec.items()


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
        if base_type == "latte":
            return 10
        elif base_type == "mocha":
            return 11
        elif base_type == "flat_white":
            return 12
