from oj import Person


def count_matching_names(person: Person) -> int:
    count = 0
    
    def counts(p: Person):
        nonlocal count
        first_letter = p.name[0].lower()
        for child in p.children:
            if child.name[0].lower() == first_letter:
                count += 1
            counts(child)
    
    counts(person)
    return count