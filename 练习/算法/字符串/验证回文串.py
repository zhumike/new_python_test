"""验证回文串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。"""

"""
正则表达式的使用

函数	说明
sub(pattern,repl,string)	把字符串中的所有匹配表达式pattern中的地方替换成repl
[^**]	表示不匹配此字符集中的任何一个字符
\u4e00-\u9fa5	汉字的unicode范围
\u0030-\u0039	数字的unicode范围
\u0041-\u005a	大写字母unicode范围
\u0061-\u007a	
小写字母unicode范围

\uAC00-\uD7AF	韩文的unicode范围
\u3040-\u31FF	日文的unicode范围
"""

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = re.sub(r"[^A-Z0-9a-z]", '', s).upper()
        l = len(tmp)
        if l <= 1 :
            return(True)
        for i in range(int(l/2)):
            if(tmp[i] != tmp[-i-1]):
                return(False)
        return(True)