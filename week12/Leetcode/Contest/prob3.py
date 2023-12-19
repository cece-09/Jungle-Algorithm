class Solution(object):
    def minIncrementOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 3보다 큰 모든 부분수열이
        # k보다 크거나 같은 수를 포함하게 하는
        # 최소한의 increse 수

        # 가장 큰 수를 올려야함
        # 바이너리??