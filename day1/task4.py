# 任务1：字符串操作
print("任务1：")
s1 = "Python is a powerful programming language"
# (1) 提取单词"language"
words = s1.split()
last_word = words[-1]
print("最后一个单词是：", last_word)

# (2) 字符串连接并重复输出
s2 = "Let's learn together"
combined = s1 + " " + s2
print("重复输出3次：")
print((combined + "\n") * 3)

# (3) 输出以p或P开头的单词
p_words = [word for word in words if word.lower().startswith('p')]
print("以p或P开头的单词：", p_words)

print("\n任务2：")
# 任务2：字符串操作
s3 = "Hello,World! This is a test string."

# (1) 去除前后空格
s3_stripped = s3.strip()
print("去除空格后：", s3_stripped)

# (2) 转换为大写
s3_upper = s3.upper()
print("转换为大写：", s3_upper)

# (3) 查找"test"的起始下标
test_index = s3.find("test")
print("'test'的起始下标：", test_index)

# (4) 替换"test"为"practice"
s3_replaced = s3.replace("test", "practice")
print("替换后的字符串：", s3_replaced)

# (5) 以空格分割并用"-"连接
words = s3.split()
s3_joined = "-".join(words)
print("用'-'连接后的字符串：", s3_joined)
