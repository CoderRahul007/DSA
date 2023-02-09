
# meh = maximum ending here
# msf maximum sum found
def contiguous(arr):
    meh = 0
    msf = arr[0]
    for i in arr:
        meh += i # keep adding the elements
        if meh < i:  # if meh is less than element then make element as meh and it will  continue from this meh
            meh = i
        if msf < meh :
            msf = meh
    return msf

def kadane(a):
    Max = a[0]
    temp = Max
    for i in range(1,len(a)):
        temp += a[i]
        if temp < a[i]: # if temp is less than element then make element as temp and it will  continue from this temp
            temp = a[i]
        Max = max(Max,temp)
    return Max

def maxSubArraySum(a,size):
     
    max_so_far = a[0]
    curr_max = a[0]
     
    for i in range(1,size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far,curr_max)
         
    return max_so_far
 
# Driver function to check the above function
a = [-2, -3, 4, -1, -2, 1, 5, -3]
print("Maximum contiguous sum is" , maxSubArraySum(a,len(a)))

arr = [-2 , -3 , 4 , -1 , -2 , 1 , 5 , -3]

print(contiguous(arr))
print(kadane(arr))

# works for both positive and neagtive elements