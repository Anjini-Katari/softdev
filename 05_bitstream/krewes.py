def choose():
    period = rng.choice([2, 7, 8]) #choose a random key
    devo = rng.choice(krewes[period]) #choose a random index of the list that corresponds with the chosen key

    output = devo + " from period " + str(period)
    return output

print(choose())