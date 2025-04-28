

#split方法的综合使用
class Solution:
    def findStr(self,str1,str2):
        count = 0
        if len(str1)<len(str2):  #母串长度小于子串长度，不存在这样的情况
            return -1
        else:
            result = str1.split(str2) #用子串来分割母串
            lenchangdu = len(result)  #子串分割后的数组长度
            count = lenchangdu-1
        return count

if __name__ == "__main__":
    demo = Solution()
    str1 = "chnjbchnnjabchuioiabc"
    str2 = "abc"
    print(demo.findStr(str1,str2))