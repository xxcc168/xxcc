import requests
from lxml import etree
import os
from pathlib import Path

#爬去网页图片，并下载到本地
def one():
    try:
        url="http://pic.netbian.com/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        #向目标网站发送请求并获取网页源码
        rs=requests.get(url, headers=headers, timeout=10)
        #指定字符集
        rs.encoding="gbk"
        #网页源码
        body=rs.text
        html=etree.HTML(body)
        listImg=html.xpath("//ul[@class='clearfix']/li/a/span/img/@src")
        print("找到图片数量：", len(listImg))

        # 创建保存目录
        current_dir = Path(__file__).parent  # 获取当前脚本所在目录
        save_dir = current_dir / 'data'  # 指向data子目录
        save_dir.mkdir(parents=True, exist_ok=True)

        for i in range(len(listImg)):
            try:
                #拼接图片路径
                file_path=url+listImg[i]
                #获取response对象
                rs=requests.get(file_path, headers=headers, timeout=10)
                #获取图片的二进制文本
                img=rs.content
                #保存路径
                path=save_dir / f'{i}.jpg'
                with open(path, 'wb') as f:
                    f.write(img)
                print(f"成功下载第{i+1}张图片到：{path}")
            except Exception as e:
                print(f"下载第{i+1}张图片失败：{str(e)}")
                continue

        print("下载完毕")
    except Exception as e:
        print(f"程序运行出错：{str(e)}")

if __name__=="__main__":
    one()
