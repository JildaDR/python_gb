#В задании нужно было @property реализовать, пришлось помучаться, чтоб применить его здесь,
# хотя без него было все намного приятнее. Ниже есть вариант без проперти.
from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, value):
        self.value = value

    @abstractmethod
    def tissue(self):
        pass

    def __add__(self, other):
        return f'Количество ткани на пошив всей одежды: {float(self.tissue) + float(other.tissue)}'

    def __str__(self):
        return str(self.tissue)


class Coat(Clothes):
    def tissue(self):
        self.tissue = "{0:.2f}".format((float(self.value) / 6.5) + 0.5)
        return float(self.tissue)

    @property
    def sum_tissue(self):
        return f'Количество ткани на пошив пальто: {self.tissue()}'


class Suit(Clothes):
    def tissue(self):
        self.tissue = "{0:.2f}".format((float(self.value) * 2) + 0.3)
        return float(self.tissue)

    @property
    def sum_tissue(self):
        return f'Количество ткани на пошив костюма: {self.tissue()}'


my_coat = Coat(42)
print(my_coat.sum_tissue)
my_suit = Suit(1.7)
print(my_suit.sum_tissue)
print(my_suit + my_coat)

#вариант без @property
class Clothes2(ABC):

    def __init__(self, value):
        self.value = value

    @abstractmethod
    def tissue(self):
        pass

    def __add__(self, other):
        return float(self.tissue) + float(other.tissue)

    def __str__(self):
        return str(self.tissue())


class Coat2(Clothes2):
    def tissue(self):
        self.tissue = "{0:.2f}".format((float(self.value) / 6.5) + 0.5)
        return float(self.tissue)


class Suit2(Clothes2):
    def tissue(self):
        self.tissue = "{0:.2f}".format((float(self.value) * 2) + 0.3)
        return float(self.tissue)


my_coat = Coat2(42)
print(my_coat)
my_suit = Suit2(1.7)
print(my_suit)
print(my_suit + my_coat)
