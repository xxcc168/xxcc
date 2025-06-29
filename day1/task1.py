# 1. 判断变量类型
x = 10
y = "10"
z = True

print(f"x的类型是: {type(x)}")
print(f"y的类型是: {type(y)}")
print(f"z的类型是: {type(z)}")

# 2. 计算圆的面积
radius = float(input("请输入圆的半径："))
PI = 3.14
area = PI * radius * radius
print(f"圆的面积是: {area}")

# 3. 类型转换
num_str = "3.14"
# 字符串转浮点数
num_float = float(num_str)
# 浮点数转整数
num_int = int(num_float)

print(f"浮点数结果: {num_float}")
print(f"整数结果: {num_int}")