# не понимаю, почему при дебаге этого кода выдает ошибку на методе __str__,
# хотя без дебага работает
# что я не так делаю?
# Если раскомментировать 13-19 и 50 строки кода, вылетает ошибка, которую я не могу
# победить, пожалуйста, напишите, где я пошла по неверному пути?

from abc import ABC, abstractmethod


class Clothes:
    @abstractmethod
    def tissue(self):
        pass

    # @property
    # def sum_tissue(self):
    #     return str(self.value)
    #
    # @sum_tissue.setter
    # def __add__(self, other):
    #     return self.tissue() + other.tissue()


class Coat(Clothes):
    def __init__(self, value):
        self.value = value

    def tissue(self):
        self.tissue = "{0:.2f}".format((float(self.value) / 6.5) + 0.5)
        return float(self.tissue)

    def __str__(self):
        return str(self.tissue())


class Suit(Clothes):
    def __init__(self, value):
        self.value = value

    def tissue(self):
        self.tissue = "{0:.2f}".format((float(self.value) * 2) + 0.3)
        return float(self.tissue)

    def __str__(self):
        return f'{self.tissue()}'


my_coat = Coat(42)
print(my_coat)
my_suit = Suit(1.7)
print(my_suit)
# print(my_coat + my_suit)
