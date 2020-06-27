#AR was ~17%?
#15.56/40
#The actual solution uses about 100 lines of union
#and spf
#25th percentile
#https://www.hackerrank.com/taesookim0412


def getMinConnectionChange(connection):
    ct = 0
    for i, a in enumerate(connection):
        if a== i+1:
            ct+=1
    if ct > 1: return ct-1
    else: return ct