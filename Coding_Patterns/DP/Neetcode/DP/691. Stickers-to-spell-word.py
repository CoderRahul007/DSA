# We are given n different types of stickers. Each sticker has a lowercase English word on it.

# You would like to spell out the given string target by cutting individual letters from your collection of stickers and rearranging them. You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

# Return the minimum number of stickers that you need to spell out target. If the task is impossible, return -1.

# Note: In all test cases, all words were chosen randomly from the 1000 most common US English words, and target was chosen as a concatenation of two random words.


# Example 1:

# Input: stickers = ["with","example","science"], target = "thehat"
# Output: 3
# Explanation:
# We can use 2 "with" stickers, and 1 "example" sticker.
# After cutting and rearrange the letters of those stickers, we can form the target "thehat".
# Also, this is the minimum number of stickers necessary to form the target string.
# Example 2:

# Input: stickers = ["notice","possible"], target = "basicbasic"
# Output: -1
# Explanation:
# We cannot form the target "basicbasic" from cutting letters from the given stickers.


from collections import Counter


class Solution:
    def minStickers(self, stickers, target):
        dp = [Counter(target)]
        visited = set((frozenset(Counter(target).items()), ))
        stickers = [Counter(sticker) for sticker in stickers]

        print(dp , visited , stickers)

        for result in range(len(target)):
            next_dp = []
            for counter in dp:
                for sticker in stickers:
                    next_counter = counter - sticker
                    print("counter " , counter)
                    print("sticker ", sticker)
                    print("next_counter " , next_counter)
                    if not next_counter:
                        return result + 1
                    visited_check = frozenset(next_counter.items())
                    if visited_check in visited:
                        continue
                    visited.add(visited_check)
                    next_dp.append(next_counter)
            dp = next_dp
        return -1

stickers = ["with","example","science"]
target = "thehat"
obj = Solution()
obj.minStickers(stickers ,target)