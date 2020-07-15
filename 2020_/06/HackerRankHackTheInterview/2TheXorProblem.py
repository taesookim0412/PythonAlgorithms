#20/20
#AR: 94.18%
#Medium
#LOL string iteration
def maxXorValue(x,k) -> str:
    num = []
    x = str(x)
    for i in range(len(x)):
        a = x[i]
        if a == '0' and k>0:
            num.append('1')
            k-=1
        else:
            num.append('0')
    return ''.join(num)

#Yeah this wasnt gonna work.
    # for i in range(5):
    #     print(i, x&mask)
    #     if x & mask != 0:
    #         num.append('0')
    #     else:
    #         num.append('1')
    #     mask <<= 1

#01101
print(maxXorValue('10010',5))
#10000
print(maxXorValue('01010',1))
print(maxXorValue('011111110',3))
