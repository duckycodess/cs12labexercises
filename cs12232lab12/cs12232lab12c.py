Cell = tuple[int, int]

def tile_with_dominoes(board: list[str]) -> list[tuple[Cell, Cell]]:
    
    visited: set[tuple[int, int]] = set()
    dominoes: list[tuple[Cell, Cell]] = []

    def is_bounded(row: int, col: int) -> bool:
        return 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] != '#'
    
    def backtrack(dominoes: list[tuple[Cell, Cell]], row: int, col: int):
        if row >= len(board)-1 and col >= len(board[0])-1:
            return

        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r,c) in visited or not is_bounded(r,c):
                    continue
                visited.add((r,c))
                if is_bounded(r+1,c) and (r+1,c) not in visited:
                        visited.add((r+1,c))
                        dominoes.append(((r,c),(r+1, c)))
                        backtrack(dominoes, r, c)
                if is_bounded(r,c+1) and (r, c+1) not in visited:
                        visited.add((r,c+1))
                        dominoes.append(((r,c), (r,c+1)))
                        backtrack(dominoes, r, c)

    
    backtrack(dominoes, 0, 0)
    return dominoes