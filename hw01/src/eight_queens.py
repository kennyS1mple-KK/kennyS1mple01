def solve_n_queens(n: int) -> list[list[str]]:
    """
    求解 N 皇后问题，返回所有合法的棋盘布局
    :param n: 棋盘边长（皇后数量）
    :return: 列表，每个元素是一个棋盘布局（字符串列表）
    """
    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    
    def is_valid(row: int, col: int) -> bool:
        # 检查列
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        # 检查左上对角线
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        # 检查右上对角线
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True
    
    def backtrack(row: int):
        if row == n:
            result.append([''.join(r) for r in board])
            return
        for col in range(n):
            if is_valid(row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'
    
    backtrack(0)
    return result

if __name__ == "__main__":
    # 测试 8 皇后
    solutions = solve_n_queens(8)
    print(f"8 皇后问题共有 {len(solutions)} 种解法")
    if solutions:
        for row in solutions[0]:
            print(row)