def toggle(puzzle: list[list[bool]], i: int, j: int) -> None:
    rows, cols = len(puzzle), len(puzzle[0])
    positions = [(i, j), (i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    for r, c in positions:
        if 0 <= r < rows and 0 <= c < cols:
            puzzle[r][c] = not puzzle[r][c]

def is_solved(puzzle: list[list[bool]]) -> bool:
    return all(all(not cell for cell in row) for row in puzzle)

def solve_lights_out(puzzle: list[list[bool]]) -> list[tuple[int, int]] | None:
    rows, cols = len(puzzle), len(puzzle[0])
    moves: list[tuple[int, int]] = []

    def backtrack(r: int, c: int) -> bool:
        if r == rows:
            return is_solved(puzzle)
        if c == cols:
            return backtrack(r + 1, 0)
        if backtrack(r, c + 1):
            return True
        
        toggle(puzzle, r, c)
        moves.append((r, c))
        if backtrack(r, c + 1):
            return True

        toggle(puzzle, r, c)
        moves.pop()
        return False

    if backtrack(0, 0):
        for r, c in reversed(moves):
            toggle(puzzle, r, c)
        return moves
    return None