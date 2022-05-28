from sudokuproject import Sudoku
from sudokuproject import solve

def main():
  starter = "000260701680070090190004500820100040004602900050003028009300074040050036703018000"
  start = [int(x) for x in starter]
  boarder = Sudoku(start)
  answer = solve(boarder)
  answer

if __name__ == '__main__':
  main()