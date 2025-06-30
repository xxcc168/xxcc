import requests
import os
from bs4 import BeautifulSoup
import time

def three():
    # 定义爬取网址
    url = "https://movie.douban.com/chart"
    # 定义浏览器表头信息，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }

    try:
        # 向目标网站发送请求并获取网页源码
        rs = requests.get(url, headers=headers, timeout=10)
        rs.raise_for_status()  # 如果状态码不是200，将引发HTTPError异常
        print("查看响应状态:", rs.status_code)

        # 使用BeautifulSoup解析网页
        soup = BeautifulSoup(rs.text, 'html.parser')

        # 找到所有电影条目
        movies = soup.find_all('div', class_='pl2')

        print("\n一周口碑榜Top10电影：")
        # 遍历前10部电影
        for i, movie in enumerate(movies[:10], 1):
            try:
                # 找到电影标题链接
                title_element = movie.find('a')
                title = title_element.get_text(strip=True).split('/')[0] if title_element else "标题未知"

                # 找到评分
                rating_element = movie.find('span', class_='rating_nums')
                rating = rating_element.get_text(strip=True) if rating_element else "暂无评分"

                print(f"{i}. {title} - 评分：{rating}")
            except Exception as e:
                print(f"处理第{i}部电影时出错：{str(e)}")

        # 保存网页源码
        save_dir = r"D:\Drivers\pydata\PythonProject1\day3"
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        file_path = os.path.join(save_dir, "index.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(rs.text)

    except requests.RequestException as e:
        print(f"请求发生错误: {str(e)}")
    except Exception as e:
        print(f"程序发生错误: {str(e)}")

if __name__ == "__main__":
    three()