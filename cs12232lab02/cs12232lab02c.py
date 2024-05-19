def final_hill(n: int, s: int, m: int, R: list[int]):
    last_hills: list[int] = [0]
    loc: int = 0
    flags: set[int] = set()
    flags_tracker: list[int] = []
    cards: list[int] = [i for i in range(9)]
    doubled = False
    twice = False

    def flag_tracker(loc: int) -> None:
        flags.add(loc)
        if len(flags) > len(flags_tracker):
            flags_tracker.append(loc)
    
    def last_hill_tracker(loc: int) -> None:
        last_hills.insert(0, loc)
        if len(last_hills) > 3:
            last_hills.pop()

    def throw(doubled: bool) -> None:
        nonlocal loc
        loc = (loc+R[0]) % 12
        last_hill_tracker(loc)
        flag_tracker(loc)

        R.append(abs(R.pop(0)))
        if doubled:
            R[-1] = R[-1] // 2

    def go_to_m(m: int) -> None:
        nonlocal loc
        loc = m
        flag_tracker(loc)
        last_hill_tracker(loc)
        cards.append(cards.pop(0))

    def go_backward() -> None:
        R[0] = -R[0]
        cards.append(cards.pop(0))

    def double_value() -> bool:
        R[0] = R[0] * 2
        cards.append(cards.pop(0))
        return True

    def skip_next_move() -> None:
        R.append(abs(R.pop(0)))
        cards.append(cards.pop(0))

    def skip_next_card() -> None:
        nonlocal cards
        cards.append(cards.pop(0))
        cards.append(cards.pop(0))

    def ret() -> None:
        nonlocal loc
        loc = last_hills[1]
        last_hill_tracker(loc)
        cards.append(cards.pop(0))

    def rettwice() -> None:
        nonlocal loc
        loc = last_hills[2]
        last_hill_tracker(loc)
        cards.append(cards.pop(0))

    def move_latest_flag() -> None:
        nonlocal loc
        flag_tracker(loc)
        loc = flags_tracker[-1]
        last_hill_tracker(loc)
        cards.append(cards.pop(0))
    
    def reverse_deck() -> None:
        nonlocal cards
        print(cards)
        cards.reverse()
    
    for _ in range(n):
        if doubled:
            twice = True
        throw(twice)
        twice = False
        doubled = False
        if loc == s:
            match cards[0]:
                case 0:
                    go_to_m(m)
                    if loc == s:
                        go_backward()
                        cards.append(cards.pop(0))
                case 1:
                    go_backward()
                case 2:
                    doubled = double_value()
                case 3:
                    skip_next_move()
                case 4:
                    skip_next_card()
                case 5:
                    ret()
                    if loc == s:
                        rettwice()
                        cards.append(cards.pop(0))
                case 6:
                    rettwice()
                    if loc == s:
                        move_latest_flag()
                        cards.append(cards.pop(0))
                case 7:
                    move_latest_flag()
                    if loc == s:
                        reverse_deck()
                        cards.append(cards.pop(0))
                case 8:
                    reverse_deck()
                case _:
                    pass
    return loc


#print(final_hill(6, 5, 8, [1, 4, 3]))
#print(final_hill(1000, 5, 8, [1, 4, 3]))
#print(final_hill(1000, 8, 5, [1, 4, 3]))
#print(final_hill(1000, 0, 0, [1, 4, 3]))

print(final_hill(1000, 6, 9, [2, 3, 4, 5, 6, 1, 2]))
#print(final_hill(10000, 6, 9, [6, 5, 4, 5, 6]))

