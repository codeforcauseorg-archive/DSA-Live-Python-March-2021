def maze(cx, cy, tx, ty):

    if(cx > tx or cy > ty):
        return 0

    if (cx == tx and cy == ty):
        return 1

    return maze(cx+1, cy, tx, ty) + maze(cx, cy+1, tx, ty)

def maze(cx, cy, tx, ty, path=""):

    if(cx > tx or cy > ty):
        return

    if (cx == tx and cy == ty):
        print(path)
        return

    maze(cx+1, cy, tx, ty, path+"V")
    maze(cx, cy+1, tx, ty, path+"H")


maze(0, 0, 2, 2)


