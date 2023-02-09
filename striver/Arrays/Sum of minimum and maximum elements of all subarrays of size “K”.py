'''
    Time Complexity: O(N)
    Space Complexity: O(K),

    Where N is the number of elements in the array, K is the size of the subarray.
'''

def sumOfMaxAndMin(nums, n, k):
    totalSum = 0
    minDQ = []
    maxDQ = []

    for i in range(k):
        curr = nums[i]

        while len(minDQ) > 0 and nums[minDQ[-1]] >= curr:
            minDQ.pop()

        while len(maxDQ) > 0 and nums[maxDQ[-1]] <= curr:
            maxDQ.pop()

        minDQ.append(i)
        maxDQ.append(i)

    totalSum += (nums[minDQ[0]] + nums[maxDQ[0]])

    for i in range(k, n):
        curr = nums[i]

        while len(minDQ) > 0 and minDQ[0] <= i - k:
            minDQ.pop(0)

        while len(maxDQ) > 0 and maxDQ[0] <= i - k:
            maxDQ.pop(0)

        while len(minDQ) > 0 and nums[minDQ[-1]] >= curr:
            minDQ.pop()

        while len(maxDQ) > 0 and nums[maxDQ[-1]] <= curr:
            maxDQ.pop()

        minDQ.append(i)
        maxDQ.append(i)

        totalSum += (nums[minDQ[0]] + nums[maxDQ[0]])

    return totalSum