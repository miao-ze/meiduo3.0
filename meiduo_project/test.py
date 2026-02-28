
from fdfs_client.client import Fdfs_client

# 先测试文件是否能被Python读取
file_path = r"C:\Users\wyys2\Desktop\github\meiduo3.0\meiduo_project\meiduo_mall\meiduo_mall\static\images\apple.jpg"
try:
    with open(file_path, "rb") as f:
        print("✅ 文件可以正常访问")
except FileNotFoundError:
    print("❌ 文件不存在或路径错误")
    exit()  # 路径错误则直接退出
except PermissionError:
    print("❌ 没有读取该文件的权限")
    exit()

# 再执行FastDFS上传
client = Fdfs_client(r'meiduo_mall/utils/fastdfs/client.conf')
result = client.upload_by_filename(file_path)
print(result)

with open('meiduo_mall/utils/fatsdfs_picture_path.txt', 'a') as file:
    file.write(result)

    """测试一下"""