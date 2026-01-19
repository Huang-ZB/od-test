import sys
import os

import os

def get_filenames_without_extension(directory):
    """
    获取指定文件夹中所有文件的文件名（不包括扩展名）

    :param directory: 文件夹路径
    :return: 包含文件名（不包括扩展名）的列表
    """
    filenames = []
    
    # 遍历指定文件夹中的所有文件和子文件夹
    for root, dirs, files in os.walk(directory):
        print(root, dirs,files)
        for file in files:
            # 分离文件名和扩展名
            filename, _ = os.path.splitext(file)
            filenames.append(filename)
    
    return filenames

# 指定要遍历的文件夹路径
directory_path = r'C:\Users\PC\Desktop\热缩套管第二批2026.1.19\output_clean'  # 请将这里替换为你的文件夹路径

# 获取文件名（不包括扩展名）
filenames_without_extension = get_filenames_without_extension(directory_path)

max_n = max(map(lambda x:len(x),filenames_without_extension))

# 打印结果
for i in range(0,len(filenames_without_extension),4):
    row = filenames_without_extension[i:i+4]
    row = list(map(lambda x: "{x:<{max_n}s}".format(x=x, max_n=max_n), row))
    print(" ".join(row))


# var1 = 'Hello World!'
# list1 = list(var1)
# list1.reverse()

# set1 = set(list1)
# for i in set1:
#     print(i,end="")
# print(list1)    