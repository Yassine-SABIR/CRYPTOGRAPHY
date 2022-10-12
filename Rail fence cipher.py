

# Rail fense cipher Yassine SABIR

"""for more informations see https://en.wikipedia.org/wiki/Rail_fence_cipher """

def RailFenceEnc(plain,Rails):#plain is String & Rails is integer

    ROWS = [[] for i in range(Rails)]

    PLIST = list(plain)

    enc = ""

    while PLIST != []:

        for i in range(Rails):

            if PLIST != []:
                ROWS[i]+= [PLIST[0]]
                PLIST = PLIST[1:]

            else:
                break

        for i in range(Rails-2,0,-1):

            if PLIST != []:
                ROWS[i] += [PLIST[0]]
                PLIST = PLIST[1:]

            else:
                break

    for A in ROWS:
        for l in A:
            enc += l

    return enc
