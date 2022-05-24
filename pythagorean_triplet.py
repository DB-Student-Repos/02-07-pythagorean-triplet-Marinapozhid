from math import sqrt
def triplets_with_sum(number):
    triplets = [
        (a, b, sqrt(a**2 + b**2)) for a in range(1, number // 3) for b in range((a + 1), number)
        ]
    triplets = list(filter(lambda triple: triple[2].is_integer(), triplets))

    return list(filter(lambda triple: sum(triple) == number, triplets))


