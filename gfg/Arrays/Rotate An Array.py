# https://www.pepcoding.com/resources/online-java-foundation/function-and-arrays/rotate_an_array/topic



# Deciding K Value: If the value of K is positive, K=K%N where N is the length of the input array.
#  If the value of K is negative, K=K%N + N.
# Revering Parts of Array: After we have calculated the value of K, reverse the first part of the array i.e.
#  from 0 to N-K-1 and the second part from N-K to N-1 separately.
# Reverse the entire Array: Now, reverse the entire array i.e. from 0 to N-1. The array will be rotated according 
# to the value of K.


def rotate(L,d,n):
    k=L.index(d)
    new_lis=[]
    new_lis=L[k+1:]+L[0:k+1]
    return new_lis
   
d = 2
n = 7
print(rotate([1,2,3,4,5,6,7],d,n))

def rotateArr(A,D,N):
    #Your code here
    def reverse(A , l  , r):
        while l < r:
            temp = A[l]
            A[l]= A[r]
            A[r] = temp
            l+=1
            r-=1
        return A
        
    D = D%N
    if D < 0:
        D +=N
    
    reverse(A , 0 , D-1)  # from 0 to D
    reverse(A , D , N-1)  # from D till end
    reverse(A , 0 , N-1)  # whole array

    
    return A
        