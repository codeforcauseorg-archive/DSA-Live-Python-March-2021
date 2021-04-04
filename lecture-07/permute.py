def permute(unproc, proc=""):
    if unproc == "":
        print(proc)
        return

    for index in range(len(unproc)):
        ch = unproc[index]
        remaining = unproc[:index] + unproc[index + 1:]
        permute(remaining, proc + ch)

permute("abc")