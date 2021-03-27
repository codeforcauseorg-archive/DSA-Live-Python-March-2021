def deci2bin(deci):

    bin = 0
    place = 1

    while deci > 0:
        rem = deci % 2
        bin = place * rem + bin
        deci = deci // 2
        place = place * 10

    return bin


def deci2any(deci, base):
    any = 0
    place = 1

    while deci > 0:
        rem = deci % base
        any = place * rem + any
        deci = deci // base
        place = place * 10

    return any

def bin2deci(bin):

    deci = 0
    place = 1

    while bin > 0:
        rem = bin % 10
        deci = place * rem + deci
        bin = bin // 10
        place = place * 2

    return deci

print(bin2deci(11101))