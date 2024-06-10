def all_strong_spell_sequences(n: int) -> list[str]:

    spells: list[str] = []

    def is_valid(curr: list[str]) -> bool:
        for k in range(len(curr)//2 + 1):
            if curr[-k:] == curr[-k*2:-k]:
                return False
        return True

    def backtrack(curr: list[str]) -> None:
        if len(curr) == n:
            spells.append(''.join(curr))
            return
        
        for c in 'fil':
            if is_valid(curr + [c]):
                backtrack(curr + [c])
    backtrack([])
    return spells