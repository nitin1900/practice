#my code but chatgpt gave some code like diagonal logic and map function...
#also had some mistake with and\or validation...

row1,column1=map(int,input("Enter white row,column: ").split(","))
row2,column2=map(int,input("Enter black row,column: ").split(","))
if row1<0 or row2<0:
    raise ValueError("row not positive")
elif column1<0 or column2<0:
    raise ValueError("column not positive")
elif(row1>7 or row2>7):
    raise ValueError("row not on board")
elif(column1>7 or column2>7):
    raise ValueError("column not on board")
elif (row1==row2 and column1==column2):
    raise ValueError("Invalid queen position: both queens in the same square")
else:
    pass

if row1==row2:#row capture
    print("captured")
elif column1==column2:#column capturre
    print("captured")
elif abs(row1-row2)==abs(column1-column2):#diagonal capture
    print("captured")
else:
    print("not caputured")

#solution...

class Result:
    def __init__ (self, ok, msg):
        self.ok = ok; self.msg = msg

class Queen:
    @staticmethod
    def _is_valid (row, col):
        if row > 7: return Result(False, "row not on board")
        if col > 7: return Result(False, "column not on board")
        if row < 0: return Result(False, "row not positive")
        if col < 0: return Result(False, "column not positive")
        return Result(True, "")
    
    def __init__(self, row, column):
        retval = Queen._is_valid(row, column)
        if not retval.ok: raise ValueError(retval.msg)
        self.row = row; self.col = column
    
    def can_attack(self, other):
        if self.col == other.col and self.row == other.row:
            raise ValueError("Invalid queen position: both queens in the same square")
        return self.row == other.row or self.col == other.col or abs(self.row - other.row) == abs(self.col - other.col)