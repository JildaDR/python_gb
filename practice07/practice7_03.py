class Cell:

    def __init__(self, amount):
        self.amount = amount

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, a):
        if not int(a):
            raise Exception("enter number")
        elif not (a > 0):
            raise Exception("enter number > 0")
        else:
            self.__amount = a

    def make_order(self, value):
        row = ''
        for i in range(int(self.__amount / value)):
            row += f'{"*" * value}\\n'
        row += f'{"*" * (self.__amount % value)}'
        return row


    def __add__(self, other):
        return self.__amount + other.__amount

    def __sub__(self, other):
        if self.__amount > other.__amount:
            return self.__amount - other.__amount
        else:
            return ('Недопустимо вычитать из меньшего')

    def __mul__(self, other):
        return self.__amount * other.__amount

    def __truediv__(self, other):
        return int(self.__amount / other.__amount)

    def __str__(self):
        return f'{self.__amount}'


cell = Cell(10)
cell2 = Cell(30)
cell3 = Cell(40)
cell4 = Cell(5)
cell5 = Cell(2)
print(cell.make_order(10))
print(cell2.make_order(3))
print(cell3.make_order(9))
print(cell4.make_order(3))
print(cell5.make_order(3))
print(cell5 + cell2)
print(cell - cell2)
print(cell3 - cell2)
print(cell * cell2)
print(cell4 / cell5)
