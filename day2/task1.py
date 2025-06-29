from task1_1 import calculate_area, calculate_perimeter


def is_palindrome(num):
    """判断一个数是否为回文数"""
    str_num = str(num)
    return str_num == str_num[::-1]

def calculate_average(*args):
    """计算任意数量参数的平均值"""
    if not args:
        return 0
    return sum(args) / len(args)

def find_longest_string(*strings):
    """返回最长的字符串"""
    if not strings:
        return None
    return max(strings, key=len)

def test_palindrome():
    """测试回文数函数"""
    print("\n测试回文数判断:")
    test_numbers = [121, 123, 12321, 12345]
    for num in test_numbers:
        print(f"{num} 是回文数吗？ {is_palindrome(num)}")

def test_average():
    """测试平均值计算"""
    print("\n测试平均值计算:")
    print(f"平均值 (1,2,3): {calculate_average(1, 2, 3)}")
    print(f"平均值 (10,20): {calculate_average(10, 20)}")
    print(f"平均值 (1,2,3,4,5): {calculate_average(1, 2, 3, 4, 5)}")

def test_longest_string():
    """测试最长字符串查找"""
    print("\n测试最长字符串查找:")
    print(f"测试1: {find_longest_string('hello', 'world', 'python', 'programming')}")
    print(f"测试2: {find_longest_string('a', 'ab', 'abc')}")
    print(f"测试3: {find_longest_string('你好', 'Python', '人工智能')}")

def test_rectangle():
    """测试矩形计算"""
    print("\n测试矩形计算:")
    length, width = 5, 3
    print(f"矩形信息：")
    print(f"长度: {length}")
    print(f"宽度: {width}")
    print(f"面积: {calculate_area(length, width)}")
    print(f"周长: {calculate_perimeter(length, width)}")

if __name__ == "__main__":
    test_palindrome()
    test_average()
    test_longest_string()
    test_rectangle()
