def all_spell_sequences(n: int) -> list[str]:
    return generateSpells(n)

def generateSpells(n: int) -> list[str]:
        
    stack: list[str] = []
    spell_sequence: list[str] = []

    def backtrack(f: int, i: int, l: int) -> None:
        if f+i+l == n:
            spell_sequence.append(''.join(stack))
            return
        
        if f < n and (not stack or stack[-1] != 'f'):
            stack.append('f')
            backtrack(f+1, i, l)
            stack.pop()

        if i < n and (not stack or stack[-1] != 'i'):
            stack.append('i')
            backtrack(f, i+1, l)
            stack.pop()

        if l < n and (not stack or stack[-1] != 'l'):
            stack.append('l')
            backtrack(f, i, l+1)
            stack.pop()

    backtrack(0, 0, 0)
    return spell_sequence