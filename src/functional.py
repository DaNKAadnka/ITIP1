def formation(str1: str, str2: str) -> str:
    return str1.format(str2)

def gcd (a, b) :
    if (b == 0) :
        return a
    else :
        return gcd(b, a % b)

def BIG_CHENGES_OF_EVER(n):
    return n