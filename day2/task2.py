class Car:
    def __init__(self, brand, speed=0):
        """初始化汽车属性"""
        self.brand = brand
        self.speed = speed

    def accelerate(self, times=1):
        """加速方法，每次速度增加10，可以加速多次"""
        for _ in range(times):
            self.speed += 10
        print(f"{self.brand}加速{times}次后，当前速度为：{self.speed}km/h")

    def brake(self, times=1):
        """刹车方法，每次速度减少10，不低于0，可以刹车多次"""
        for _ in range(times):
            self.speed = max(0, self.speed - 10)
        print(f"{self.brand}刹车{times}次后，当前速度为：{self.speed}km/h")

class ElectricCar(Car):
    def __init__(self, brand, speed=0, battery=50):
        """初始化电动汽车的属性"""
        super().__init__(brand, speed)
        self.battery = min(100, battery)  # 电量不超过100

    def charge(self):
        """充电方法，电量增加20，不超过100"""
        self.battery = min(100, self.battery + 20)
        print(f"{self.brand}充电后，当前电量为：{self.battery}%")

def test_car():
    """测试普通汽车"""
    print("\n测试普通汽车：")
    car = Car("Toyota")
    print(f"创建了一辆{car.brand}汽车，初始速度：{car.speed}km/h")
    car.accelerate(3)  # 加速3次
    car.brake(2)       # 刹车2次

def test_electric_car():
    """测试电动汽车"""
    print("\n测试电动汽车：")
    e_car = ElectricCar("Tesla", battery=30)
    print(f"创建了一辆{e_car.brand}电动汽车")
    print(f"初始速度：{e_car.speed}km/h")
    print(f"初始电量：{e_car.battery}%")

    e_car.accelerate(2)  # 加速2次
    e_car.charge()       # 充电一次
    e_car.brake(1)       # 刹车1次
    e_car.charge()       # 再充电一次

if __name__ == "__main__":
    test_car()
    test_electric_car()
