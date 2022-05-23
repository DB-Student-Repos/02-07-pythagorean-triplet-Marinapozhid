def triplets_with_sum(number):

    triplets = []
    for a in range(1, number // 3):
        ''' b^2 = c^2 - a^2 and c = number - a - b 
        b^2 = (number - a - b)^2 - a^2
        b^2 = (number - a)^2 - 2(number - a)b + b^2 - a^2
        number^2 - 2number*a + a^2 - 2b*number + 2ab - a^2 = 0
        b(2number - 2a) = number^2 - 2a*number
        
        type(b) == int
        '''
        b = (number ** 2 - 2 * number * a) // (2 * number - 2 * a)
        c = number - a - b
        if a ** 2 + b ** 2 == c ** 2 and c > b and b > a:
                triplets.append([a,b,c])
    return triplets


