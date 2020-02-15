n = int(input().strip())
nums = list(map(int, input().strip().split()))

visited = [0] * n


def dfs(i):
    res = []
    flag = True
    for j in range(n):
        if not visited[j]:
            if (nums[i] % 3 == 0 and nums[j] == nums[i] // 3) or nums[j] == nums[i] * 2:
                flag = False
                visited[j] = 1
                tmp = dfs(j)
                visited[j] = 0
                if isinstance(tmp[0], list):
                    for item in tmp:
                        res.append([nums[i]] + item)
                else:
                    res.append([nums[i]] + tmp)
    if flag:
        res = [nums[i]]
    return res


for i in range(n):
    visited[i] = 1
    ans = dfs(i)
    visited[i] = 0
    if not isinstance(ans[0], list):
        continue
    for j in range(len(ans)):
        cur = ans[j]
        #print(cur)
        if len(cur) == n:
            cur = list(map(str, cur))
            print(" ".join(cur))
            i = n + 1
            break
    #print(visited)
