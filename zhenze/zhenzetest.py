import re
"""正则"""
#手机号判断
#不用正则
def isPhone(num):
	#判断长度是不是11位
	if len(num) != 11:
		return False
	#判断是不是都是数字
	if  not str.isdigit(num):
		return False
	#判断前三位是不是正确的号段
	li = ['138','137']
	if num[:3] not in li:
		return False
	return True
print(isPhone('13612348976'))
print(isPhone('135vbiu9807'))
print(isPhone('19876542345'))
print(isPhone('13890987324'))

isPhone_match = re.match("\d{11}","13456780932")
print(isPhone_match.group())



#正则匹配
# .匹配任意字符,除了\n   []：匹配[]中列举的字符  \d:匹配数字
# \D:匹配非数字  \s:匹配空白  \S:匹配非空白 \w:匹配单词字符  \W：匹配非单词字符 
ret = re.match("h","hello world")
print(ret.group())

#匹配失败返回 none
# ret1 = re.match("h","Hello world")
# print(ret1.group())

ret2 = re.match(".","hello world")
print(ret2.group())


ret3 = re.match("[hH]","Hello world")
print(ret3.group())

ret4 = re.match("no.\d","no.1 world")
print(ret4.group())

ret5 = re.match("no.[0-9]","no.2 world")
print(ret5.group())

ret6 = re.match("no.\w","no.a world")
print(ret6.group())

path =  "c:\\a\\b\\c"
print(path)

ret7 = re.match("c:\\\\",path)
print(ret7.group())

#原始字符串,涉及\使用较为方便
ret8 = re.match(r"c:\\",path)
print(ret8.group())

#* ：匹配前一个字符出现0次或无限次  + ：匹配前一个字符出现1次或无限次
#？：匹配前一个字符出现0次或1次   {m} : 匹配前一个字符出现m次
#{m,} : 匹配前一个字符至少出现m次   {m,n} : 匹配前一个字符出现m到n次

#检测变量名的有效性
ret9 = re.match("[a-zA-Z_]+\w*","name1")
print(ret9.group())

#匹配0-99数字
retx = re.match("[1-9]?[0-9]","98")
print(retx.group())


#字符串匹配边界
# ^：匹配字符串开头  $匹配字符串结尾  \b：匹配一个单词边界  \B：匹配非单词边界 

retx1 = re.match("[1-9]?[0-9]$","19")
print(retx1.group())


retx2 = re.match(r".*\bver\b","ho ver adb")
print(retx2.group())

#匹配分组
#|：匹配左右任意一个表达式  (ab):将括号中字符作为一个分组
retx3 = re.match("\w{4,20}@(163|126|qq)\.com","test@qq.com")
print(retx3.group())

#匹配电话号码
retx4 = re.match("(138|152|156)\d{8}","13876541234")
print(retx4.group())

retx5 = re.match("(\d{3,4})-(\d{7,8})","027-98763345")
print(retx5.group())

retx6 = re.match("<[a-zA-Z]*>\w*</[a-zA-Z]*>","<html>hh</html>")
print(retx6.group())

#\1代表第一个分组
retx7 = re.match(r"<([a-zA-Z]*)>\w*</\1>","<html>hello</html>")
print(retx7.group())

retx8 = re.match(r"<([a-zA-Z]*)><(\w*)>\w*</\2></\1>","<html><h1>title</h1></html>")
print(retx8.group())

#给分组命名
retx9 = re.match(r"<(?P<n1>[a-zA-Z]*)><(?P<n2>\w*)>\w*</(?P=n2)></(?P=n1)>","<html><h1>title</h1></html>")
print(retx9.group())


#search用法:搜索出符合特征的字符串
reta1 = re.search("\d+","阅读999  评论22")
print(reta1.group())

#findall:找出所有符合匹配规则的特征字符串
#此时reta2是数组
reta2 = re.findall(r"\d+","阅读999，评论22")
print(reta2)

#sub:将匹配到的字符进行替换,并输出字符串
reta3 = re.sub(r"\d+","888","阅读999，评论22")
print(reta3)

#split：按照特征切割字符串，最后输出字符数组
reta4 = re.split(":| ","info:aaa:iii ff112")
print(reta4)


#贪婪和非贪婪模式
reta5 = re.match("aa(\d+?)","aa1234ffmfi980")
print(reta5.group(1))

reta5 = re.match("aa(\d+?)ff","aa1234ffmfi980")
print(reta5.group(1))







