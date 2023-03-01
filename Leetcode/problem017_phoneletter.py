def palindromeSS(s):
    def getSS(s,l):
        L = len(s)
        lst = []
        for i in range(L-l+1):
            lst.append( s[i:l+i] )          
        return lst

    L = len(s)
    if L%2 == 0:
        L = L//2
    else:
        L = L//2 + 1
    while L>0:
        print(L)
        for ss in getSS(s,L):
            stest = ss + "".join(reversed(ss))
            print(ss,"  ",stest)
            if stest in s:
                return stest
    
        for ss in getSS(s,L):
            stest = ss[:-1] + ss[-1] + "".join(reversed(ss[:-1]))
            print(ss,"  ",stest)
            if stest in s:
                return stest
        
        L = L-1
    return ""

print(palindromeSS("babbabac"))


