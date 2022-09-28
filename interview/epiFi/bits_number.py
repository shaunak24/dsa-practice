class Solution:
    # Find pairs where set_bits(a) + set_bits(b) = k
    def bitsNum(self, nums, k):

        def countSetBits(n):
            return bin(n).count('1')

        bits_map = {}  # key - no. of set bits, value - [index of no.]
        count = 0
        for i in range(len(nums)):
            set_bits = countSetBits(nums[i])
            if set_bits not in bits_map.keys():
                bits_map[set_bits] = []
            if (k - set_bits) in bits_map.keys():
                count += len(bits_map[k - set_bits])
            bits_map[set_bits].append(i)
        print(bits_map)
        return count


s = Solution()
print(s.bitsNum([2, 5, 3, 4], 3))