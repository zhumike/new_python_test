
"""协程
gevent是一个基于协程的python网络库，在遇到IO阻塞时，程序会自动进行切换
"""
import gevent

# def fun(num):
# 	for i in range(num):
# 		print("%s%s"%(gevent.getcurrent(),str(i)))
# #模拟耗时任务，注意必须用gevent中的sleep方法。
# 		gevent.sleep(1)
#
# if __name__ == '__main__':
# 	g1 = gevent.spawn(fun,5)
# 	g2 = gevent.spawn(fun,5)
# 	g3 = gevent.spawn(fun,5)
#
# 	g1.join()
# 	g2.join()
# 	g3.join()


#携程，没有gevent.monkey，是顺序执行

# def f1():
#     for i in range(5):
#         print('run func: f1, index: %s ' % i)
#         gevent.sleep(0)
#
#
# def f2():
#     for i in range(5):
#         print('run func: f2, index: %s ' % i)
#         gevent.sleep(0)
#
# if __name__ == '__main__':
# 	t1 = gevent.spawn(f1)
# 	t2 = gevent.spawn(f2)
# 	gevent.joinall([t1, t2])


# import gevent
# import gevent.pool
# import gevent.monkey
#
# gevent.monkey.patch_all()  # 分布式冲突
# import requests
#
#
# def download_img(t_event_data):
#     """
#     保存图片到本地
#     :return:
#     """
#     try:
#         index = t_event_data["index"]
#         num = t_event_data["num"]
#         r = requests.get("https://wwww.baidu.com")
#         print("index:{} num:{}".format(index, num))
#
#     except Exception as e:
#         print("下载异常:{}".format(e))
#
#
# def main():
#     try:
#         num_list = [i for i in range(1, 100)]  # 相当于起了100个协程池
#         gevent_data_list = []
#
#         for index, num in enumerate(num_list):
#             t_event_data = {}
#             t_event_data["index"] = index
#             t_event_data["num"] = num
#             print(t_event_data)
#             gevent_data_list.append(gevent.spawn(download_img, t_event_data))
#
#         gevent.joinall(gevent_data_list)
#     except Exception as e:
#         print("异常 {}".format(e))
#
#
# if __name__ == "__main__":
#     main()


#协程

# import gevent
# import time
# from gevent import monkey
#
# monkey.patch_all()
#
#
# def test1():
#     for i in range(5):
#         print('test1...', i)
#         time.sleep(1)
#
#
# def test2():
#     for i in range(5):
#         print('test2...', i)
#         time.sleep(1)
#
#
# if __name__ == '__main__':
#     gevent.joinall([
#         gevent.spawn(test1),
#         gevent.spawn(test2)
#     ])




#协程的运用，图片下载器

import requests
import gevent


def download_img(url, img_name):
    response = requests.get(url)  # 获取图片中的二进制数据
    with open('img/' + img_name, mode='wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1548222339580&di=8033e859c88d8de0dd07fb0908a511ab&imgtype=0&src=http%3A%2F%2Fimgm.gmw.cn%2Fattachement%2Fjpg%2Fsite2%2F20170222%2Ff44d307589e71a1729e422.jpg'
    url1 = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1548222339580&di=d21ac1313363549c11498991e2446e85&imgtype=0&src=http%3A%2F%2Fcn.toluna.com%2Fdpolls_images%2F2017%2F09%2F21%2F371665b2-af55-43b9-a25e-ba30eea4a737_x400.jpg'

    gevent.joinall({
        gevent.spawn(download_img, url, 'panda1.jpg'),
        gevent.spawn(download_img, url1, 'panda2.jpg')
    })