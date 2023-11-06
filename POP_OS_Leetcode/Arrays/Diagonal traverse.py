
# For every cell in the 2-D list, if there is an element after nums[row][col], add (row, col+1) to queue.
# Cells along the first column is special, so before checking 1 we have to check if there is a row below the current cell,
#  ex. nums[row+1], and add (row+1, col) to queue and there are "row" number of rows to check. Then we check 1. like any other cell.
# Please upvote if it makes sense.

# class Solution {
#     public int[] findDiagonalOrder(List<List<Integer>> nums) {
#         int count = 0;
#         for (List<Integer> l : nums) count += l.size();
#         int[] res = new int[count];
#         Queue<int[]> q = new LinkedList();
#         q.add(new int[]{0,0});
#         int row = 0, rows = nums.size(), index = 0;
#         while (q.isEmpty() == false) {
#             int[] cur = q.poll();
#             res[index++] = nums.get(cur[0]).get(cur[1]);
#             if (row + 1 < rows && cur[1] == 0) {
#                 q.add(new int[]{++row, 0});
#             }
#             if (cur[1] + 1 < nums.get(cur[0]).size()) {
#                 q.add(new int[]{cur[0], cur[1]+1});
#             }
#         }
#         return res;
#     }
# }
#---------------------------------------
#index sum based
import collections
# def diagonal(nums):
#     d = collections.defaultdict(list)
#     for r, row in enumerate(nums):
#         for c, val in enumerate(row):
#             d[r+c].append(val)
#     print(d)
#     res = []
#     for lst in d.values():
#         res.extend(lst[::-1])
#     return res

class Solution:
    def diagonal(self, nums):
        res = [] 
        queue = [[0,0]]
        while queue:
            i = queue[0][0]
            j = queue[0][1]
            print('i->',i,'j->',j)
            print('nums i j',nums[i][j])
            res.append(nums[i][j])
            print(res)
            queue.pop(0)
            print('Q',queue)
            if i < len(nums)-1 and j == 0 and len(nums[i+1]) > j:
                queue.append([i+1,j])
                print('1st',queue)
            if j + 1 < len(nums[i]):
                queue.append([i, j+1])
                print('2nd',queue)
        return res
nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
nums1 = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
nums2 = [[1,2,3,4,5,6]]
s=Solution()
# print(diagonal(nums))
# print('-------------------------------')
# print(diagonal(nums1))
# print('-------------------------------')
# print(diagonal(nums2))
print(s.diagonal(nums))
print('-------------------------------')
print(s.diagonal(nums1))
print('-------------------------------')
print(s.diagonal(nums2))