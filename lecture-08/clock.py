leds = [False] * 10

def populate(leds):

    hours, minutes = 0, 0

    for h in range(0, 4):
        if leds[h]:
            hours += (2**h)

    for m in range(4, 10):
        if leds[m]:
            minutes += (2**(m-4))

    return hours, minutes

def clock(n, leds,  index):

    if(len(leds) == index):
        if(n == 0):
            hours, minutes = (populate(leds))
            if((hours < 12) and (minutes < 60)):
                print(hours, minutes)
        return

    if n > 0:
        leds[index] = True
        clock(n-1, leds, index+1)
        leds[index] = False

    clock(n, leds, index+1)



clock(2, leds, 0)

