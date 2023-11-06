class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1.0
        if n==1:
            return x
        if n<0:
            n=-n
            x=1/x
        res=1.0
        while n!=0:
            if n%2!=0 :
                res*=x # this will be executed when n is 1
                print("Odd",res,n,x)
            x*=x
            print("Last print",x,n)
            n=n>>1 # n=n//2
        return res


#Recursive

# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if n==0:
#             return 1.0
#         if n==1:
#             return x
#         if n<0:
#             return self.myPow(1/x,-n)
#         l=self.myPow(x,n//2)
#         if n%2==0:
#             return l*l
#         else:
#             return l*l*x
s=Solution()
print(s.myPow(3,9))