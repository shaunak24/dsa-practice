class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n_set = set()
        for n in nums:
            if n != 0 and n not in n_set:
                n_set.add(n)
        return(len(n_set))
