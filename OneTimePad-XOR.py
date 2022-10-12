# One Time Pad - XOR - Yassine SABIR

"""For more informations see https://en.wikipedia.org/wiki/One-time_pad """

def int2bin(n):
    if n==0:
        return "0"
    else:
        return int2bin(n//2)+str(n%2)


def bin2int(ch):
    if ch=="":
        return 0
    else:
        return int(ch[-1])+2*bin2int(ch[:-1])


def bin2bin8bits(ch):
    if len(ch)<8:
        return "0"*(8-len(ch))+ch
    else:
        return ch[-8:]


def string2bin(string):
    if string=="":
        return ""
    else:
        return bin2bin8bits(int2bin(ord(string[0])))+string2bin(string[1:])


def bin2string(binstring):
    n=len(binstring)
    string=""
    for i in range(0,n,8):
        string+=chr(bin2int(binstring[i:i+8]))
    return string


def XOR(a,b):
    if a not in ["0","1"] or b not in ["0","1"]:
        print("ERROR")
        return
    else:
        if a=="1" and b=="1":
            return "0"
        elif a=="0" and b=="0":
            return "0"
        else:
            return "1"


def Onetimepad(string,key):
    for i in key:
        if i not in ["0","1"]:
            print("ERROR")
            return

    binstring=string2bin(string)
    n,m=len(binstring),len(key)
    newbinstring=""
    for i in range(0,n,m):
        for j in range(m):
            newbinstring += XOR(key[j],binstring[j+i])
    return bin2string(newbinstring)

