# долго сражалась, методом проб и ошибок победила :)
class Matrix:
    def __init__(self, list):
        self.matrix = list

    def __str__(self):
        return str('\n'.join('\t'.join(str(i) for i in a) for a in self.matrix))

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for a in range(len(self.matrix[i])):
                self.matrix[i][a] += other.matrix[i][a]
        return str('\n'.join('\t'.join(str(i) for i in a) for a in self.matrix))

my_matrix = Matrix([[5, 7, 8], [9, 0, 3], [8, 9, 6]])
my_matrix2 = Matrix([[3, 6, 9], [5, 4, 0], [5, 5, 5]])
print(my_matrix)
print(my_matrix2)
print(my_matrix + my_matrix2)