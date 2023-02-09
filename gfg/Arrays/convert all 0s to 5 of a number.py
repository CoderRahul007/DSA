def convert(n):
    s = 0
    res = 1

    while n > 0:
        rem = n % 10
        rem = 5 if rem == 0 else rem        
        s = s + int(res * rem)
        res = res * 10
        n = n//10
    return s

print(convert(1004))