from gevent_test import monkey,socket
import gevent_test
import sys
import time

"""TCP版服务器--协程"""

#协程补丁
monkey.patch_all()

#客户端处理流程
def handle_request(conn):
	while True:
		data = conn.recv(1024)
		if not data:
			conn.close()
			break
		else:
			print("收到数据%s"%data)
			conn.send(data)
#创建服务器 
def server(port):
	s = socket.socket()
	s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	s.bind(('192.168.0.116',port))
	s.listen(5)
	while True:
		cli,addr = s.accept()
		gevent_test.spawn(handle_request, cli)
if __name__ == '__main__':
	server(17788)

