import random as rng

def choose():
    krewes_file = open('krewes.txt', 'k')
    krewes={2[], 7[], 8[]}

    devos_list = krewes_file.split("@@@") # splits list by devo
    
    for n in devos_list:
        if n[0] == 2:
            krewes[2.append(str.split('$$$'))]
        if n[0] == 7:
            krewes{7(str.split('$$$'))}
        if n[0] == 8:
            krewes{8(str.split('$$$'))}
    return krewes
'''
    = rng.choice([2, 7, 8]) #choose a random key
    devo = rng.choice(krewes[period]) #choose a random index of the list that corresponds with the chosen key

    output = devo + " from period " + str(period)
    return output
'''

print(choose())


#split it by @@@ signs per devo, sprt by pd, then split by $ 