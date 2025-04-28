"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。
说明：
分隔时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：
输入:
s = “catsanddog”
wordDict = [“cat”, “cats”, “and”, “sand”, “dog”]
输出:
[
“cats and dog”,
“cat sand dog”
]

示例 2：
输入:
s = “pineapplepenapple”
wordDict = [“apple”, “pen”, “applepen”, “pine”, “pineapple”]
输出:
[
“pine apple pen apple”,
“pineapple pen apple”,
“pine applepen apple”
]
解释: 注意你可以重复使用字典中的单词。
示例 3：
输入:
s = “catsandog”
wordDict = [“cats”, “dog”, “sand”, “and”, “cat”]
输出:
[]
2.
 思路1:


先判断能不能拆分，如果能拆分的话，先根据wordDict中的单词长度，从前往后分割，
然后进行匹配，如果匹配上wordDict里的单词，对剩下的进行递归。直到len(s)==0,
说明s都已经匹配完了。由于可能有不同的分割结果，每一个不同的分割结果只需要记录
一次，因此需要对wordDict里的单词长度进行去重。


"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        res = []
        if len(s) == 0 or not wordDict:
            return []
        wordLenList = [len(word) for word in wordDict]
        wordLenSet = set(wordLenList)
        if self.judge(s, wordDict):
            self.dfs(s, wordDict, [], res, wordLenSet)
        return res

    def judge(self, s, wordDict):  # 先判断能不能分割
        lenth = len(s)
        dp = [False for i in range(lenth + 1)]
        dp[0] = True
        for i in range(1, lenth + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]

    def dfs(self, s, wordDict, curResult, res, wordLenSet):
        if len(s) == 0:  # 递归终止条件
            res.append(" ".join(curResult))
            return
        else:
            for i in wordLenSet:  # 进行回溯
                if i <= len(s):
                    if s[:i] in wordDict:
                        self.dfs(s[i:], wordDict, curResult + [s[:i]], res, wordLenSet)
            return


# 思路2：
# 递归 + 构建额外字典保存切分结果
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        res = []
        memo = dict()
        return self.dfs(s, res, wordDict, memo)

    def dfs(self, s, res, wordDict, memo):
        # 如果当前单词存在于字典中，直接返回
        if s in memo:
            return memo[s]
        # 当前字符串的为空判断
        if not s:
            return [""]

        # 拼接存在于字典中的字符串
        res = []
        for word in wordDict:
            if s[:len(word)] != word:
                continue
            for r in self.dfs(s[len(word):], res, wordDict, memo):
                res.append(word + ("" if not r else " " + r))
        memo[s] = res
        print(s)
        print(memo[s])
        return res


# 解法2
"""
先判断能不能拆分，如果能拆分的话，先根据wordDict中的单词长度，从前往后分
割，然后进行匹配，如果匹配上wordDict里的单词，对剩下的进行递归。直
到len(s)==0,说明s都已经匹配完了。由于可能有不同的分割结果，每一个不
同的分割结果只需要记录一次，因此需要对wordDict里的单词长度进行去重。
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        res = []
        if len(s) == 0 or not wordDict:
            return []
        wordLenList = [len(word) for word in wordDict]

        wordLenSet = set(wordLenList)
        if self.judge(s, wordDict):
            self.dfs(s, wordDict, [], res, wordLenSet)
        return res

    def judge(self, s, wordDict):  # 先判断能不能分割
        lenth = len(s)
        dp = [False for i in range(lenth + 1)]
        print(dp)
        dp[0] = True
        for i in range(1, lenth + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]

    def dfs(self, s, wordDict, curResult, res, wordLenSet):
        if len(s) == 0:  # 递归终止条件
            res.append(" ".join(curResult))
            return
        else:
            for i in wordLenSet:
                print(i)
                # 进行回溯
                if i <= len(s):
                    if s[:i] in wordDict:
                        print(s[:i])
                        self.dfs(s[i:], wordDict, curResult + [s[:i]], res, wordLenSet)
            return
