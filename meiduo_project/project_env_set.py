"""
在连接fastdfs的tracker时会出现问题
storeip配置成内网地址了，访问fastdfs先访问tracker服务器，会返回storeip地址，
返回的这个地址是一个192.168这样一个内网地址，无法从我本地传到服务器
解决方法：在tracker_client.py文件中找到tracker_query_storage_stor_without_group方法，
其中有获取设置IP地址的地方：现在改为手动方法
"""
fastDFS_tracker_ip_set = '192.168.238.226'
