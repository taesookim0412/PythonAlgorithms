#3/10
#The solution works except the accepted solution
#uses nodes due to .... string interpolation delay?

def receivedText(s):
    idx = 0
    curr = 0
    newStr = []
    toggled = True
    while idx < len(s):
        a = s[idx]
        if a == '<':
            curr = 0
            idx+=1
            continue
        elif a == '>':
            curr = len(newStr)
            idx += 1
            continue
        elif a=='*':
            if curr > 0:
                del newStr[curr-1]
                curr -=1
            idx+=1
            continue
        elif a=='#':
            toggled = not toggled
            idx+=1
            continue
        elif str(0)<=a<=str(9):
            if toggled:
                newStr.insert(curr, a)
                curr+=1
            idx+=1
            continue
        else:
            newStr.insert(curr, a)
            curr += 1
            idx += 1
            continue
    return ''.join(newStr)


#LLHO
print(receivedText("HE*<LL>O"))
#LL0
print(receivedText("HE**<LL>O"))
print(receivedText(""))


#002HLL
print(receivedText("HE*>LL<002#824#2**2"))
print(receivedText(chr(30)))