def subseq(unproc, proc):

    if(unproc == ""):
        print(proc)
        return

    ch = unproc[0]
    subseq(unproc[1:], proc+ch)
    subseq(unproc[1:], proc)


def subseq(unproc, index=0, proc=""):
    if (len(unproc) == index):
        print(proc)
        return

    ch = unproc[index]
    subseq(unproc, index+1, proc + ch)
    subseq(unproc, index+1, proc)


def subseq(unproc, index=0, proc=[]):
    if (len(unproc) == index):
        print(''.join(proc))
        return

    ch = unproc[index]

    subseq(unproc, index+1, proc)

    proc.append(ch)
    subseq(unproc, index + 1, proc)
    proc.pop()

def subseq(unproc, solutions, index=0, proc=[]):
    if (len(unproc) == index):
        solutions.append(''.join(proc))
        return

    ch = unproc[index]

    subseq(unproc, solutions, index+1, proc)

    proc.append(ch)
    subseq(unproc, solutions, index + 1, proc)
    proc.pop()


solutions=[]
subseq("abc", solutions)
print(solutions)