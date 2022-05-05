def triplets_with_sum(number):
    triplets = []
    for a in range(number):
        for c in range(number):
            b = number - a - c
            if a ** 2 + b ** 2 == c ** 2 and a < b < c:
                triplets.append([a, b, c])
    return triplets 




