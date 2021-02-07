from typing import List
import functools

def cmp(a, b):
    if str(a) + str(b) < str(b) + str(a):
        return -1  # 负值为小于
    elif str(a) + str(b) > str(b) + str(a):
        return 1
    return 0

class Solution:
    def minNumber(self, nums: List[int]) -> str:
        nums = sorted(nums, key=functools.cmp_to_key(cmp))
        return ''.join(map(str, nums))

'''
提示:

0 < nums.length <= 100
说明:

输出结果可能非常大，所以你需要返回一个字符串而不是整数
拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0

'''