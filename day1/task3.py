# 1. 使用列表推导式存储1-100的整数，输出其中的偶数
numbers = [i for i in range(1, 101)]
even_numbers = [x for x in numbers if x % 2 == 0]
print("1-100中的偶数：")
print(even_numbers)

# 2. 删除列表中的重复元素并保持顺序不变
test_list = [1, 2, 3, 2, 4, 1, 5, 3, 6]
no_duplicates = list(dict.fromkeys(test_list))
print("\n删除重复元素后的列表：")
print(f"原列表：{test_list}")
print(f"处理后：{no_duplicates}")

# 3. 将两个列表合并为字典
keys = ["a", "b", "c"]
values = [1, 2, 3]
combined_dict = dict(zip(keys, values))
print("\n合并后的字典：")
print(combined_dict)

# 4. 元组存储学生信息并解包
student = ("张三", 18, 95.5)
name, age, score = student
print("\n学生信息：")
print(f"姓名：{name}")
print(f"年龄：{age}")
print(f"成绩：{score}")
