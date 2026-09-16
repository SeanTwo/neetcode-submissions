class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_str = str(bin(n))[2:]
        count = 0
        for char in bin_str:
            if char == '1':
                count += 1
        return count