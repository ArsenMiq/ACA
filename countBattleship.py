def countBattleships(board):
        count = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'X':
                    var = 1
                    if (r > 0 and board[r-1][c] == 'X') or (c > 0 and board[r][c-1] == 'X'):
                        var = 0
                    count += var
        return count


board = [["X",".",".","X"],
        [".",".",".","X"],
        [".",".",".","X"]]

print(countBattleships(board))

board = [["."]]

print(countBattleships(board))
