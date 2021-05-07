class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        if n < 2:
            return False
        pre_comp = {}
        total = 0
        for i in range(n):
            key_i = '%s-1' % i
            pre_comp[key_i] = nums[i]
            total += nums[i]
        if total % k == 0:
            return True
        for w in range(2, n+1):
            total_aux = total
            for i in range(n-w+1):
                key_i = '%s-%s' % (i, w)
                if key_i not in pre_comp:
                    key_sub = '%s-%s' % (i + 1, w - 1)
                    pre_comp[key_i] = nums[i] + pre_comp[key_sub]
                sum_list = pre_comp[key_i]
                if sum_list % k == 0:
                    return True
                pre_comp[key_i] = sum_list
                key_rest = '%s-%s' % (i + w, n - w - i)
                if n - w - i > 1:
                    if key_rest not in pre_comp:
                        pre_comp[key_rest] = total_aux - pre_comp[key_i]
                    sum_list_2 = pre_comp[key_rest]
                    if sum_list_2 % k == 0:
                        return True
                total_aux -= nums[i]
        return False
