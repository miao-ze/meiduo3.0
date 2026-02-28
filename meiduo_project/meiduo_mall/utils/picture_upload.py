
from fdfs_client.client import Fdfs_client
import os

# 获取所有的图片文件路径，为后续的文件上传打好基础
def get_image_paths_with_os(folder_path, image_extensions=None):
    """
    获取指定文件夹下所有图片文件的完整路径
    Args:
        folder_path: 目标文件夹路径
        image_extensions: 图片扩展名列表，默认为常见图片格式
    Returns:
        包含所有图片路径的列表
    """
    # 定义常见的图片扩展名（包含大小写）
    if image_extensions is None:
        image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
    image_paths = []
    # 遍历文件夹及其子文件夹
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 获取文件扩展名（转小写）
            file_ext = os.path.splitext(file)[1].lower()
            # 判断是否为图片文件
            if file_ext in image_extensions:
                # 拼接完整路径
                full_path = os.path.join(root, file)
                image_paths.append(full_path)
    return image_paths

# 进行文件上传工作
def upload_images(image_paths):
    for image_path in image_paths:
        try:
            with open(image_path, 'rb') as f:
                print('文件可以正常访问')
                print('开始进行上传工作')
        except FileNotFoundError:
            print("❌ 文件不存在或路径错误")
            exit()  # 路径错误则直接退出
        except PermissionError:
            print("❌ 没有读取该文件的权限")
            exit()
        else:
            # 再执行FastDFS上传
            client = Fdfs_client(r'fastdfs/client.conf')
            result = client.upload_by_filename(image_path)
            print(result)
        # 将得到的地址数据保存到文本中
            with open('fastdfs_picture_path.txt','a',encoding='utf-8') as file:
                remote_file_id = result.get('Remote file_id', '')  # 加get避免键不存在报错
                # new_remote_file_id = remote_file_id.replace('//','////')
                file.write(image_path + '    路径为： ' +remote_file_id + '\n')

# 示例使用
if __name__ == "__main__":
    # 替换为你的图片文件夹路径
    target_folder = r"D:\meiduo_mall_picture_storage\tb_sku_image"
    # 获取所有图片路径
    image_files = get_image_paths_with_os(target_folder)
    upload_images(image_files)



"""
你这段代码的问题在于，os.walk() 返回的是一个生成器对象，直接打印它只会显示对象的内存地址，而不是目录下的文件列表。
正确的使用方式
os.walk() 需要通过循环来遍历，它会依次返回三元组 (root, dirs, files)：
root：当前遍历的目录路径
dirs：当前目录下的子目录列表
files：当前目录下的文件列表
"""

