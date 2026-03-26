class matrix:
  def __init__(self, rows, columns):
    self.rows = rows
    self.columns = columns
    
  def normalMatrix(self):
    nMatrix = []
    for i in range(1, self.rows + 1):
      rowMatrix = []
      for j in range(1, self.columns + 1):
        elRows = rowMatrix.append(int(input()))
      nMatrix.append(rowMatrix)

    print(nMatrix)

  def rowMatrix(self):
    rMatrix = []
    for i in range (1, 2):
      for j in range(1, self.columns + 1):
        elRowMatrix = rMatrix.append(int(input()))
    print(rMatrix)

  def columnMatrix(self):
    colMatrix = []
    for i in range(1, self.rows + 1):
      elcol = []
      for j in range(1, 2):
        elColMatrix = elcol.append(int(input()))
      colMatrix.append(elcol)
    print(colMatrix)

col = matrix(5, 1)
col.columnMatrix()