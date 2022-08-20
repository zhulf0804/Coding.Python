class Solution:
    def groupAnagrams(self, strs):
        res_dict = {}
        for item in strs:
            k = tuple(sorted(item))
            if k not in res_dict:
                res_dict[k] = [item]
            else:
                res_dict[k].append(item)
        return list(res_dict.values())