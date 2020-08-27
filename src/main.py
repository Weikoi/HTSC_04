from Beverage import *
from Order import *
from BeverageSpec import *


def get_order():
    spec_dict = {}
    print("您选择什么基础咖啡？ 从 1.latte / 2.mocha / 3.flat_white 中选择 (请输入对应序号)")
    spec_dict["base_type"] = input()
    print("您选择什么杯型？ 从 1.M / 2.L / 3.H 中选择  (请输入对应序号)")
    spec_dict["cup"] = input()
    print("您选择什么温度？ 从 1.常温 / 2.冰 / 3.热 中选择 (请输入对应序号)")
    spec_dict["temperature"] = input()
    print("您选择什么奶？ 从 1.全脂 / 2.脱脂 / 3.豆奶 中选择 (请输入对应序号)")
    spec_dict["milk"] = input()
    print("要几份原味糖浆？(请输入份数）")
    spec_dict["original_syrup"] = input()
    print("要几份香草糖浆？(请输入份数）")
    spec_dict["vanilla_syrup"] = input()
    print("要几份榛果糖浆？(请输入份数）")
    spec_dict["acorn_syrup"] = input()
    print("要几份焦糖糖浆？(请输入份数）")
    spec_dict["caramel_syrup"] = input()
    print("要几份覆盆子糖浆？(请输入份数）")
    spec_dict["raspberry_syrup"] = input()
    print("要几份摩卡酱？(请输入份数）")
    spec_dict["mocha_syrup"] = input()
    print("要几份摩卡淋酱？(请输入份数）")
    spec_dict["mocha_sauce"] = input()
    print("要几份焦糖风味酱？(请输入份数）")
    spec_dict["caramel_sauce"] = input()
    return spec_dict


if __name__ == '__main__':
    # coffee_spec_dict1 = {"base_type": "latte",
    #                      "cup": "big",
    #                      "temperature": "hot",
    #                      "milk": "soy_milk",
    #                      "original_syrup": "0",
    #                      "vanilla_syrup": "0",
    #                      "acorn_syrup": "0",
    #                      "caramel_syrup": "0",
    #                      "raspberry_syrup": "2",
    #                      "mocha_syrup": "0",
    #                      "mocha_sauce": "0",
    #                      "caramel_sauce": "0"
    #                      }
    # coffee1 = Coffee(coffee_spec_dict1)
    order = Order()
    print("请问您要购买几杯咖啡？")
    num = int(input())
    for i in range(num):
        print("===========================")
        print("以下是您的第" + str(i + 1) + "杯咖啡")
        order.add_order(Coffee(get_order()))

    print("您的订单总价是：", end="")
    print(order.calculate(), end="")
    print("元")
