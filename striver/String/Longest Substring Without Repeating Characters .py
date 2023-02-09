def uniqueSubstrings(arr ) :
    # Write your code here.
    mp = defaultdict(lambda : -1) # 256 char
    left = 0
    right = 0
    n = len(arr)
    Len = 0
    while right < n :
        l = arr[left]
        r = arr[right]
        if mp[r] != -1: # if arr[right] is found in mp
            left = max(mp[r] + 1 , left)
        mp[r] = right
        Len = max(Len , right - left +1)
        right += 1
    return Len


''''
    Time Complexity - O(N)
    Space Complexity - O(K)

    where N is the length of the string.
    and K in number of different character in the string 
'''


def uniqueSubstrings(input) :

    n = len(input)
    Set = set()

    ans = 0
    i = 0
    j = 0

    while(i < n and j < n) :
        
        # try to extend the range [i,j]    

        if input[j] not in Set :           
            Set.add(input[j])           
            ans = max(ans, j - i + 1)
            j+=1
        
        else :

            Set.remove(input[i]) # since we are removing from starting as 
            # longest substring cant start from that left which has duplicate in window left to right
            # the new lenght will start from j+1
            # it will remove one by one elements from left

            i+=1

    return ans

input = "pwwkew"
print(uniqueSubstrings(input))

# input[j]  p
# input[i]  p
# In If
# Before
# set()
# After
# {'p'}
# input[j]  w
# input[i]  p
# In If
# Before
# {'p'}
# After
# {'w', 'p'}
# input[j]  w
# input[i]  p
# ________________________________________________
# In else
# Before
# {'w', 'p'}
# After
# {'w'}
# _________________________________________________
# input[j]  w
# input[i]  w
# ________________________________________________
# In else
# Before
# {'w'}
# After
# set()
# _________________________________________________
# input[j]  w
# input[i]  w
# In If
# Before
# set()
# After
# {'w'}
# input[j]  k
# input[i]  w
# In If
# Before
# {'w'}
# After
# {'w', 'k'}
# input[j]  e
# input[i]  w
# In If
# Before
# {'w', 'k'}
# After
# {'w', 'e', 'k'}
# input[j]  w
# input[i]  w
# ________________________________________________
# In else
# Before
# {'w', 'e', 'k'}
# After
# {'e', 'k'}
# _________________________________________________
# input[j]  w
# input[i]  k
# In If
# Before
# {'e', 'k'}
# After
# {'w', 'e', 'k'}
# 3