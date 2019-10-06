class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split(' ')
        reversed_word_list = [word[::-1] for word in word_list]
        return ' '.join(reversed_word_list)

s = "Let's take LeetCode contest"

ss = Solution()
print(ss.reverseWords(s))