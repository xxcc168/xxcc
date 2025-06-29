import os
import re

def natural_sort_key(s):
    """实现特定排序规则：数字按自然顺序，但带前导零的数字排在相同值的数字之前"""
    def convert(text):
        if text.isdigit():
            # 对于数字部分，创建一个元组：(数值, 原始字符串长度)
            # 这样可以保证：相同数值时，更长的数字串（带前导零）排在后面
            num_val = int(text)
            return (num_val, len(text))
        return text.lower()

    parts = re.split('([0-9]+)', s)
    return [convert(text) for text in parts]

def rename_images():
    # 设置文件夹路径
    folder_path = 'data/新建文件夹'
    txt_path = 'data/新建文本文档.txt'

    # 读取txt文件中的新名称
    with open(txt_path, 'r', encoding='utf-8') as f:
        new_names = [name.strip() for name in f.readlines() if name.strip()]

    # 获取所有图片文件并按Windows自然顺序排序
    image_files = [f for f in os.listdir(folder_path) if f.endswith('.png')]
    image_files.sort(key=natural_sort_key)  # 使用自然排序

    # 确保文件数量匹配
    if len(image_files) != len(new_names):
        print(f"警告：图片数量({len(image_files)})与名字数量({len(new_names)})不匹配！")
        return

    # 重命名文件
    for i, (old_name, new_name) in enumerate(zip(image_files, new_names), 1):
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, f"{new_name}.png")

        try:
            os.rename(old_path, new_path)
            print(f"[{i}] 成功: {old_name} -> {new_name}.png")
        except Exception as e:
            print(f"[{i}] 失败: {old_name} -> {new_name}.png")
            print(f"错误信息: {str(e)}")

if __name__ == "__main__":
    rename_images()
