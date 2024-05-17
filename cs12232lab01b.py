def who_gets_the_star(m: int, w: int, p: int, s: int) -> str:
    characters = ["MARIO", "WIGI", "PEARL"]

    distance = [abs(m-s), abs(w-s), abs(p-s)]

    if distance.count(min(distance)) >= 2:
        return "NONE"
    else:
        return characters[distance.index(min(distance))]
