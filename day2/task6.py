import numpy as np

# 创建数组A：3x2的二维数组
A = np.arange(1, 7).reshape(3, 2)
print("数组A：")
print(A)

# 创建数组B：一维数组
B = np.array([10, 20])
print("\n数组B：")
print(B)

# 1. 计算A和B的逐元素相加（利用广播）
add_result = A + B
print("\nA和B的逐元素相加结果：")
print(add_result)

# 2. 计算A和B的逐元素相乘（利用广播）
multiply_result = A * B
print("\nA和B的逐元素相乘结果：")
print(multiply_result)

# 3. 计算A的每一行与B的点积
dot_product = np.dot(A, B)
print("\nA的每一行与B的点积：")
print(dot_product)
