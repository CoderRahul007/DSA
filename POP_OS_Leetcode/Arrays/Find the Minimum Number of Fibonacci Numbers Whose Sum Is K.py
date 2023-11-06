class Solution:
    def findMinFibonacciNumbers(self, k):
        if k<2:
            return k
        def fib(k):
            a,b=(0,1)
            res=[1]
            while True:
                c=a+b
                if c>k:
                    return res
                res.append(c)
                a=b
                b=c
        z=fib(k)
        c=0
        i=len(z)-1
        print(z)
        while(k!=0):
            if z[i]<=k:
                print('Z[i]',z[i])
                print('k',k)
                k-=z[i]
                print('After minus',k)
                c+=1
            i-=1
        return c
s=Solution()
print(s.findMinFibonacciNumbers(19))

                
