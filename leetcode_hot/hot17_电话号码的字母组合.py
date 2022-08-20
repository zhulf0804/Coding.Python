class Solution:
    map_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', \
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    
    def core(self, digits):
        if not digits:
            return []
        ans_list = self.core(digits[1:])
        res = []
        for u in Solution.map_dict[digits[0]]:
            if len(ans_list) == 0:
                res.append(u)
                continue
            for v in ans_list:
                res.append(u+v)
        return res
              
    def letterCombinations(self, digits):
        return self.core(digits)
        