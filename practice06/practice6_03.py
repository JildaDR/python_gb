class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        inc = self.get_total_income()
        return (f' name: {self.name}; surname: {self.surname}; position: {self.position}; total income: {inc}')

    def get_total_income(self):
        my_sum = self._income.get('wage') + self._income.get('bonus')
        return (my_sum)

    def result(self):
        print(self.get_full_name())


manager = Position('John', 'Smith', 'manager', 10000, 500)
ceo = Position('William', 'Walles', 'CEO', 100000, 25000)
cto = Position('Adam', 'Sandler', 'CTO', 90000, 20000)

manager.result()
ceo.result()
cto.result()
