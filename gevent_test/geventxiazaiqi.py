"""gevent下载器"""
from gevent_test import monkey
import gevent_test
from  urllib import request

#需要让gevent自动处理io事件
monkey.patch_all()


def myDownload(url):
	print('get : %s'%url)
	response = request.urlopen(url)
	data = response.read()
	print('从%s收到%d的数据'%(url,len(data)))
#生成协程对象
gevent_test.joinall([gevent_test.spawn(myDownload, "http://www.baidu.com"), gevent_test.spawn(myDownload, "http://www.sohu.com"), gevent_test.spawn(myDownload, "http://www.hao123.com")])