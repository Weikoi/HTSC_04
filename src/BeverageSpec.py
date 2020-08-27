class BeverageSpec(object):

    def __init__(self, prop_dict):
        self.prop_dict = prop_dict

    def get_prop(self, prop_name):
        return self.prop_dict[prop_name]

    def get_all_props(self):
        return self.prop_dict.items()


class CoffeeSpec(BeverageSpec):
    def __init__(self, prop_dict):
        BeverageSpec.__init__(self, prop_dict)


