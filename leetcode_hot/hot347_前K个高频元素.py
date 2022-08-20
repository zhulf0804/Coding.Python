# class Solution:
#     def topKFrequent(self, nums, k):
#         dict = {}
#         for num in nums:
#             dict[num] = dict.get(num, 0) + 1
#         # keys, values = dict.keys(), dict.values()
#         l = sorted(dict.items(), key=lambda item:item[1], reverse=True)
#         res = [item[0] for item in l[:k]]
#         return res


# class Solution:
#     def topKFrequent(self, nums, k):
#         dict = {}
#         for num in nums:
#             dict[num] = dict.get(num, 0) + 1
#         pairs = list(dict.items())

#         def shift_down(arr, root, k):
#             val = arr[root]
#             while root<<1 < k:
#                 child = root << 1
#                 if child|1 < k and arr[child|1][1] < arr[child][1]:
#                     child |= 1
#                 if arr[child][1] < val[1]:
#                     arr[root] = arr[child]
#                     root = child
#                 else:
#                     break
#             arr[root] = val

#         def shift_up(arr, child):
#             val = arr[child]
#             while child>>1 > 0 and val[1] < arr[child>>1][1]:
#                 arr[child] = arr[child>>1]
#                 child >>= 1 
#             arr[child] = val
        
        
#         heap = [[0, 0]]
#         for i in range(k):
#             heap.append(pairs[i])
#             shift_up(heap, len(heap)-1)
        
#         for i in range(k, len(pairs)):
#             if pairs[i][1] > heap[1][1]:
#                 heap[1] = pairs[i]
#                 shift_down(heap, 1, k+1)
#         return [item[0] for item in heap[1:]]

class Solution:
    def topKFrequent(self, nums, k):
        dict = {}
        for num in nums:
            dict[num] = dict.get(num, 0) + 1
        
        l = [[] for _ in range(1 + len(nums))]
        for kk, v in dict.items():
            l[v].append(kk)
        
        res, cc = [], 0
        for v in range(len(nums), -1, -1):
            if len(l[v]) > 0:
                res.extend(l[v])
                cc += len(l[v])
            if cc == k:
                break
        return res