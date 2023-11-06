def nthroot(num,n):
    l=1
    h=num
    if num<=0:
        return 0
    if 0<num<1:
        l=num
        h=1
    eps=0.00000000001
    guess=l+(h-l)/2
    while abs(guess**n-num )>=eps:
        if guess**n >num:
            h=guess
        else:
            l=guess
        guess=l+(h-l)/2
    return guess
print(nthroot(8,2))
