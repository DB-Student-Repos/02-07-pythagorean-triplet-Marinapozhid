import math
def triplets_with_sum(number):

    triplets = []
    for b in range(number):
        for a in range(1, b):
            c = math.sqrt(a ** 2 + b ** 2)
            if a + b + c == number:
                triplets.append([a, b, c])
    return triplets 




