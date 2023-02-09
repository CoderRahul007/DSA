# https://www.youtube.com/watch?v=0do2734xhnU

# Another Efficient Approach :  By finding next smaller element and previous smaller element for every element in O(n) time complexity and O(n) auxiliary space .

# Step 1 : First we will take two arrays left_smaller[] and right_smaller[] and initialize it with -1 and n respectively.

# Step 2 : For every element we will store the index of previous smaller and next smaller element in left_smaller[] and right_smaller[] arrays respectively.

#                 (It will take O(n) time).

# Step 3 : Now for every element we will calculate area by taking this ith element as the smallest in the range left_smaller[i] and right_smaller[i] and multiplying it with the difference of left_smaller[i] and right_smaller[i].

# Step 4 : We can find the maximum of all the area calculated in step 3 to get the desired maximum area.



def getMaxArea(arr):

  s = [-1]
  n = len(arr)
  area = 0
  i = 0
  left_smaller = [-1]*n
  right_smaller = [n]*n
  
  while i < n:
      while s and (s[-1] != -1) and (arr[s[-1]] > arr[i]):
          right_smaller[s[-1]] = i
          s.pop()
      if((i > 0) and (arr[i] == arr[i-1])):
          left_smaller[i] = left_smaller[i-1]
      else:
          left_smaller[i] = s[-1]
      s.append(i)
      i += 1

  for j in range(0, n):
      area = max(area, arr[j]*(right_smaller[j]-left_smaller[j]-1))
  return area
 
hist = [6, 2, 5, 4, 5, 1, 6]
print("maxArea = ", getMaxArea(hist))