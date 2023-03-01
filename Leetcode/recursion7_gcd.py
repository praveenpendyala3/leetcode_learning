


def gcd(a,b):
    if a==0:
        return b
    elif b==0:
        return a
    elif a==b:
        return a

    if a>b:
        return gcd(b,a%b)
    if b>a:
        return gcd(a,b%a)

print(gcd(12,1))

