class matrix:
    def __init__(self, rowM1, columnM1, rowM2, columnM2):
        self.rowM1 = rowM1
        self.columnM1 = columnM1
        self.rowM2 = rowM2
        self.columnM2 = columnM2

    def normalMatrix(self):
        # Matrix A
        self.A = []
        print("Enter elements of Matrix A:")
        for i in range(self.rowM1):
            rowMatrix = []
            for j in range(self.columnM1):
                rowMatrix.append(int(input()))
            self.A.append(rowMatrix)

        # Matrix B
        self.B = []
        print("Enter elements of Matrix B:")
        for i in range(self.rowM2):
            rowMatrix = []
            for j in range(self.columnM2):
                rowMatrix.append(int(input()))
            self.B.append(rowMatrix)


class Add(matrix):
    def addition(self):
        if (self.rowM1, self.columnM1) == (self.rowM2, self.columnM2):
            c = []
            for i in range(self.rowM1):
                elAdd = []
                for j in range(self.columnM1):
                    elAdd.append(self.A[i][j] + self.B[i][j])
                c.append(elAdd)
            return c
        else:
            print("Order of matrices are not same.")


# Usage
addition = Add(2, 2, 2, 2)
addition.normalMatrix()
result = addition.addition()

print("Result:")
for row in result:
    print(row)