class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums[:]
        self.array = nums
        

    def reset(self) -> List[int]:
        self.array = self.original[:]
        return self.array
        

    def shuffle(self) -> List[int]:
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array
        

# O(n)
# O(n)