import os
import yaml
def read_yml(file_path):
    """
    读取yml文件
    :param file_path: 文件名称
    :return: 返回读取的数据
    """

    with open(file_path ,"r",encoding="utf-8") as f:
        f_data = f.read()
    yml_data = yaml.safe_load(f_data)
    return yml_data
if __name__ == "__main__":
   file_path = r"D:\python\api_project\data\test_login.yml"
   a =  read_yml(file_path)
   print(a)