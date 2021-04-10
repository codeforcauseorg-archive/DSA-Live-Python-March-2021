hours = [False] * 4
minutes = [False] * 6

def clock(n, hours, minutes, h, m, posh, posm):

    if(posm > 5 or posh > 3):
        return

    if(n == 0):
        if(h < 12 and m < 60):
            print(str(h) + ":" +str(m))
        return

    for pos in range(posh, len(hours)):
        if not hours[pos]:
            hours[pos] = True
            clock(n-1, hours, minutes, h + (2**pos), m, pos+1, posm)
            hours[pos] = False

    for pos in range(posm, len(minutes)):
        if not minutes[pos]:
            minutes[pos] = True
            clock(n-1, hours, minutes, h, m + (2**pos), posh, pos+1)
            minutes[pos] = False


clock(2, hours, minutes, 0, 0, 0, 0)

