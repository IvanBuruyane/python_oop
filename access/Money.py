class Money:

    @staticmethod
    def __check_money(money: int) -> bool:
        return isinstance(money, int) and money >= 0

    def __init__(self, money: int) -> None:
        if self.__check_money(money):
            self.__money = money

    def get_money(self) -> int:
        return self.__money

    def set_money(self, money: int) -> None:
        if self.__check_money(money):
            self.__money = money

    def add_money(self, mn) -> None:
        self.__money += mn.get_money()

mn_1 = Money(10)
mn_2 = Money(20)
mn_1.set_money(100)
mn_2.add_money(mn_1)
m1 = mn_1.get_money()    # 100
m2 = mn_2.get_money()    # 120

print(m1, m2)


