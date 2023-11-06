# Given an array of citations (each citation is a non-negative integer) of a researcher,
# write a function to compute the researcher's h-index.

# According to the definition of h-index on Wikipedia: 
# "A scientist has index h if h of his/her N papers have at least h citations each,
#  and the other N − h papers
#  have no more than h citations each."

# Input: citations = [3,0,6,1,5]
# Output: 3 
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
#              received 3, 0, 6, 1, 5 citations respectively. 
#              Since the researcher has 3 papers with at least 3 citations each and the remaining 
#              two with no more than 3 citations each, her h-index is 3.


# Most important of all: The definition.

# "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

# So the observation is: If I sort the citations, then the idx-element in the sorted array means there are at least N-idx papers have citations count more than or equal to citations[idx]

# For example,

#            idx:  0 1 2 3 4
#          N-idx:  5 4 3 2 1
# citations[idx]:  0 1 3 5 6

#     For idx == 0, it means there are at least 5 papers have citations count more than or equal to 0
#     For idx == 3, it means there are at least 2 papers have citations count more than or equal to 5
#     For idx == 4, it means there are at least 1 papers have citations count more than or equal to 6

# But how do we connect it to the definition, which said that it want h papers with at least h citations?
# The answer is that we can further modify the observation to

# there are at least N-idx papers have citations count more than or equal to min(N-idx, citations[idx])

# Why? I actually notice this transformation when I failed with the case [100], which follow by what I observed could be:

#     For idx == 0, it means there are at least 1 papers have citations count more than or equal to 100

# It's right, but from the definition, h papers with at least h citations, h could not be 100, instead, it should be 1!!

# And the answer would be the largest value for min(N-idx, citations[idx]) in each idx!
# So, that's pretty much how I think of this problem, hope it helps you!

# Sample Python Code:

# def hIndex(citations):
#     citations.sort()
#     comparePairs = zip([len(citations)-i for i in range(len(citations))], citations)
#     # [(5, 0), (4, 1), (3, 3), (2, 5), (1, 6)]
#     return max([min(p) for p in comparePairs]) if citations else 0

# or

# def hIndex(self, citations):
#     citations.sort()
#     maxh, lc = 0, len(citations)
#     for i, n in enumerate(citations):
#         maxh = max(min(lc-i, n), maxh)
#     return maxh

# Solution 1 with std::sort
# Time complexity: Linear O(n log n), sorting cost + one pass through citations array
# Space complexity: Constant O(1)

# class Solution {
# public:
#     int hIndex(vector<int>& citations) {
#         std::sort(citations.begin(), citations.end());
#         int n = citations.size();

#         for (int i = 0; i < citations.size(); ++i) {
#             if (citations[i] >= n - i) {
#                 return n - i;
#             }
#         }

#         return 0;
#     }
# };

# Solution 2 without std::sort
# Time complexity: Linear O(n), one pass through paper count array
# Space complexity: Linear O(n), space allocated to paper count array

# class Solution {
# public:
#     int hIndex(vector<int>& citations) {
#         int n = citations.size();
#         vector<int> papers(n + 1);

#         // count papers
#         for (const auto x : citations) {
#             // any citation larger than n can be replaced by n
#             // and the h-index will not change after the replacement
#             papers[std::min(n, x)]++;
#         }

#         int count = papers[n];
#         while (count < n) {
#             // incrementing count while decrementing n
#             count += papers[--n];
#         }
        
#         return n;
#     }
# };


class Solution:
    def hIndex(self, cit):
        cit.sort()
        n=len(cit)
        for i in range(n):
            if cit[i]>=n-i:
                return n-i
        return 0


# class Solution:
#     def hIndex(self, citations: List[int]) -> int:
#         n = len(citations)
#         buckets = [0 for i in range(n + 1)]
#         for i in citations:
#             if(i > n):
#                 buckets[n] += 1
#             else:
#                 buckets[i] += 1
        
#         runPaperCount = 0
        
#         for i in range(n, 0, -1):
#             runPaperCount += buckets[i]
#             if i <= runPaperCount:
#                 return i
        
#         return 0

# def hIndex(citations){
#     {
# if(citations == null || citations.length == 0){
#             return 0;
#         }
#         int max = 0;
#         for(int i = 0; i < citations.length; ++i){
#             max = Math.max(citations[i], max);
#         }
#         int[] citationsNums = new int[max+1];
#         for(int i = 0; i < citations.length; ++i){
#             citationsNums[citations[i]] += 1;
#         }
#         int total = 0;
#         for(int i = citationsNums.length-1; i >= 0; --i){
#             total += citationsNums[i];
#             if(total >= i){
#                 return i;
#             }
#         }
#         return 0;
        
#     }
# }
# int hIndex(vector<int>& citations) {
#         if(citations.size() == 0)
#             return 0;
#         int max = INT_MIN;
#         for(int num: citations)
#             if(num > max)
#                 max = num;
#         vector<int> arr(max+1, 0);
#         for(int num: citations)
#             arr[num]++;
#         vector<int> suffixSum(max+1, 0);
#         suffixSum[arr.size()-1] = arr[arr.size()-1];
#         for(int i = arr.size()-2;i>=0;i--)
#             suffixSum[i] = suffixSum[i+1] + arr[i];
#         int hIndex = 0;
#         for(int i=0;i<suffixSum.size(); i++)
#             if(suffixSum[i] >= i)
#                 hIndex = i;
#         return hIndex;
        
#     }


#For sorted array---


# class Solution:
#     def hIndex(self, A):
#         L     = len(A)
#         valid = lambda i: A[i]>=(L-i)
#         i,j   = 0, L-1 
#         best  = L
#         #
#         while i<=j:
#             mid = (i+j)//2
#             if valid(mid):
#                 best = mid # After a match, " (j = mid - 1) < mid ", so the latest match is always the minimum
#                 j = mid - 1 # try even lower
#             else:
#                 i = mid + 1 # index must be higher
#         return L-best

# class Solution {
# 	public int hIndex(int[] c) {
# 		int i=c.length-1,k=1;
# 		if(i==0)     return 0;
# 		while(i>=0 && c[i--]>=k) { k++;}
# 		return k-1;
# 	}
# }
# This approach is to find the first element such that the value of that element is greater than or equal 
# to the amount of elements remaining.
#  The ans is return the length of array after that point. If no such element exisits return 0.

# class Solution {
#     public int hIndex(int[] citations) {
#         int n = citations.length;
#         int low = 0, high = n;
#         while(low<high){
#             int mid = low + ((high-low)>>1);
#             if(n-mid <= citations[mid])
#                 high = mid;
#             else
#                 low = mid+1;
#         }
#         return n-high;
#     }
# }

# class Solution:
#       def hIndex(self, cit):
#             n=len(cit)
#             l=0
#             h=n
#             while l<h:
#                 m=(l+h)//2
#                 print('M',m)
#                 print('n-m',n-m,cit[m])
#                 if n-m <= cit[m]: // base condition as with unsorted one 
#                     h=m
#                     print('H',h)
#                 else:
#                     l=m+1
#                     print('L',l)
#             return n-h
s=Solution()
print(s.hIndex([3,0,6,1,5]))
print(s.hIndex([3,0,1,6,5]))

# print(hIndex([3,0,6,1,5]))
# print(hIndex([3,0,1,6,5]))