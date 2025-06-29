def is_palindrome(num):
    # 将数字转换为字符串
    str_num = str(num)
    # 比较正序和倒序是否相等
    return str_num == str_num[::-1]

# 测试代码
if __name__ == "__main__":
    test_numbers = [121, 123, 12321, 12345]
    for num in test_numbers:
        print(f"{num} 是回文数吗？ {is_palindrome(num)}")

def calculate_average(*args):
    if not args:
        return 0
    return sum(args) / len(args)

# 测试代码
if __name__ == "__main__":
    # 测试不同数量的参数
    print(f"平均值: {calculate_average(1, 2, 3)}")  # 测试3个数
    print(f"平均值: {calculate_average(10, 20)}")   # 测试2个数
    print(f"平均值: {calculate_average(1, 2, 3, 4, 5)}")  # 测试5个数


def find_longest_string(*strings):
    if not strings:
        return None
    return max(strings, key=len)


# 测试代码
if __name__ == "__main__":
    # 测试不同的字符串组合
    test1 = find_longest_string("hello", "world", "python", "programming")
    print(f"最长的字符串是: {test1}")

    test2 = find_longest_string("a", "ab", "abc")
    print(f"最长的字符串是: {test2}")

    test3 = find_longest_string("你好", "Python", "人工智能")
    print(f"最长的字符串是: {test3}")

from task1_1 import calculate_area, calculate_perimeter


def main():
    # 测试矩形计算
    length = 5
    width = 3

    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)

    print(f"矩形信息：")
    print(f"长度: {length}")
    print(f"宽度: {width}")
    print(f"面积: {area}")
    print(f"周长: {perimeter}")


if __name__ == "__main__":
    main()
