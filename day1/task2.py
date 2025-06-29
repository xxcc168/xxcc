# 1. 判断一个数是否为素数的辅助函数
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# 1. 输出1到100之间的所有素数
def print_primes():
    print("1-100之间的素数：")
    primes = []
    for num in range(1, 101):
        if is_prime(num):
            primes.append(str(num))
    print(", ".join(primes))

# 2. 计算斐波那契数列的前20项
def fibonacci():
    print("\n斐波那契数列前20项：")
    fib = [0, 1]  # 初始化列表，包含第一项和第二项
    for i in range(2, 20):
        fib.append(fib[i-1] + fib[i-2])
    print(", ".join(map(str, fib)))

# 3. 计算特定条件数的和
def special_sum():
    print("\n1-10000之间能被3整除或者能被5整除且不能被15整除的数的和：")
    total = 0
    num = 1
    while num <= 10000:
        if (num % 3 == 0 or num % 5 == 0) and num % 15 != 0:
            total += num
        num += 1
    print(total)

def main():
    # 1. 输出素数
    print_primes()

    # 2. 输出斐波那契数列
    fibonacci()

    # 3. 计算特定条件的和
    special_sum()

if __name__ == "__main__":
    main()
