# -*- coding: utf-8 -*-
"""
自动化爬取谷歌学术文献，模拟人类行为，防反爬。
依赖：selenium, fake_useragent
Edge浏览器需安装对应WebDriver。
"""
import time
import random
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# 需要爬取的文献标题
PAPER_TITLES = [
    "Automatic crater detection and age estimation for mare regions on the lunar surface,",
    "The origin of planetary impactors in the inner solar system,",
    "Deep learning based systems for crater detection: A review,",
    "A preliminary study of classification method on lunar topography and landforms,",
    "The CosmoQuest Moon mappers community science project: The effect of incidence angle on the Lunar surface crater distribution,",
    "Fast r-cnn,",
    "You only look once: Unified, real-time object detection,",
    "Attention is all you need,",
    "End-to-end object detection with transformers,",
]

RESULTS_DIR = os.path.join(os.path.dirname(__file__), 'paper_results')
RESULTS_PATH = os.path.join(RESULTS_DIR, 'scholar_results.txt')

if not os.path.exists(RESULTS_DIR):
    os.makedirs(RESULTS_DIR)

def get_driver():
    """获取Edge浏览器驱动实例，增强反爬虫能力"""
    ua = UserAgent()
    options = Options()

    # CDP命令执行参数
    edge_options = {
        # 禁用自动化标志
        "excludeSwitches": ["enable-automation", "enable-logging"],
        "useAutomationExtension": False,
        # 修改 navigator.webdriver 标志
        "prefs": {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            # 禁用PDF查看器
            "plugins.always_open_pdf_externally": True,
            # 禁用默认的下载行为
            "download.default_directory": "NUL",
            # 禁用翻译提示
            "translate.enabled": False
        }
    }

    for key, value in edge_options.items():
        options.add_experimental_option(key, value)

    # 添加随机 User-Agent
    user_agent = ua.random
    options.add_argument(f'user-agent={user_agent}')

    # 随机窗口大小和位置
    width = random.randint(1024, 1920)
    height = random.randint(768, 1080)
    position_x = random.randint(0, 100)
    position_y = random.randint(0, 100)
    options.add_argument(f'window-size={width},{height}')
    options.add_argument(f'window-position={position_x},{position_y}')

    # 添加其他伪装参数
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--disable-infobars')
    options.add_argument('--no-sandbox')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-gpu')

    service = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service, options=options)

    # 执行 JavaScript 来修改 webdriver 标志
    stealth_js = """
    Object.defineProperty(navigator, 'webdriver', {
        get: () => false,
    });
    window.navigator.chrome = {
        runtime: {},
    };
    Object.defineProperty(navigator, 'languages', {
        get: () => ['zh-CN', 'zh', 'en'],
    });
    Object.defineProperty(navigator, 'plugins', {
        get: () => [1, 2, 3, 4, 5],
    });
    """
    driver.execute_script(stealth_js)

    # 设置更多的请求头
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {
        "userAgent": user_agent,
        "acceptLanguage": "zh-CN,zh;q=0.9,en;q=0.8",
        "platform": "Windows"
    })

    return driver

def human_like_actions(driver):
    """更真实的人类行为模拟"""
    # 随机滑动
    for _ in range(random.randint(2, 4)):
        scroll_y = random.randint(100, 500)
        driver.execute_script(f"window.scrollBy(0, {scroll_y});")
        time.sleep(random.uniform(0.5, 1.5))
        # 随机向上滑动
        if random.random() > 0.7:
            driver.execute_script(f"window.scrollBy(0, {-random.randint(50, 200)});")
        time.sleep(random.uniform(0.3, 0.8))

    # 随机停顿
    time.sleep(random.uniform(1, 3))

    # 添加随机鼠标移动
    def random_mouse_move():
        x = random.randint(100, 700)
        y = random.randint(100, 500)
        script = f"var e = document.createEvent('MouseEvents'); e.initMouseEvent('mousemove', true, true, window, 0, 0, 0, {x}, {y}, false, false, false, false, 0, null); document.dispatchEvent(e);"
        driver.execute_script(script)

    # 执行随机鼠标移动
    for _ in range(random.randint(3, 7)):
        random_mouse_move()
        time.sleep(random.uniform(0.1, 0.3))

    # 随机停顿时添加微小的鼠标移动
    if random.random() > 0.7:
        random_mouse_move()

    # 模拟人类阅读行为
    time.sleep(random.uniform(2, 5))

def search_and_scrape(driver, title):
    try:
        # 随机选择搜索入口并添加语言参数
        base_urls = [
            "https://scholar.google.com/?hl=zh-CN",
            "https://scholar.google.com/scholar?hl=zh-CN",
            "https://scholar.google.com/schhp?hl=zh-CN"
        ]
        driver.get(random.choice(base_urls))

        time.sleep(random.uniform(3, 5))

        # 查找搜索框并模拟人类输入
        search_box = driver.find_element(By.NAME, "q")
        search_box.clear()

        # 模拟人类输入
        for char in title:
            search_box.send_keys(char)
            time.sleep(random.uniform(0.05, 0.2))

        time.sleep(random.uniform(0.5, 1.5))
        search_box.send_keys(Keys.ENTER)

        # 增加载入等待时间
        time.sleep(random.uniform(3, 6))

        human_like_actions(driver)
        # 解析首条结果
        try:
            results = driver.find_elements(By.CSS_SELECTOR, ".gs_ri")
            if results:
                first = results[0]
                paper_title = first.find_element(By.TAG_NAME, "h3").text
                try:
                    link = first.find_element(By.TAG_NAME, "a").get_attribute("href")
                except:
                    link = "无可用链接"
                return paper_title, link
            else:
                return "未找到结果", ""
        except Exception as e:
            return f"异常: {e}", ""
    except Exception as e:
        print(f"搜索出错: {str(e)}")
        return f"异常: {e}", ""

def main():
    driver = get_driver()
    results = []


    for idx, t in enumerate(PAPER_TITLES):
        print(f"[{idx+1}/{len(PAPER_TITLES)}] 搜索: {t}")

        # 增加重试机制
        max_retries = 3
        for retry in range(max_retries):
            try:
                paper_title, link = search_and_scrape(driver, t)
                if paper_title != "异常":
                    break
            except Exception as e:
                print(f"第{retry+1}次尝试失败: {str(e)}")
                if retry < max_retries - 1:
                    time.sleep(random.uniform(20, 30))
                    continue
                paper_title, link = f"失败: {str(e)}", ""

        print(f"  结果: {paper_title}\n  链接: {link}\n")
        results.append(f"{t}\n{paper_title}\n{link}\n{'-'*60}")

        # 增加更长的随机等待时间
        time.sleep(random.uniform(15, 30))

    driver.quit()
    # 保存结果
    with open(RESULTS_PATH, 'w', encoding='utf-8') as f:
        f.write('\n'.join(results))
    print(f"全部完成，结果已保存到: {RESULTS_PATH}")

if __name__ == "__main__":
    main()
