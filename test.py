print("hello world")
print("你好，世界")
class Calculator:
    def Add(self, a, b):
        # 计算两个数的和
        return a + b

    def Subtract(self, a, b):
        # 计算两个数的差
        return a - b

    def Multiply(self, a, b):
        # 计算两个数的积
        return a * b

    def Divide(self, a, b):
        # 计算两个数的商
        if b == 0:
            raise ValueError("除数不能为零")
        return a / b

class ScientificCalc(Calculator):
    def Power(self, a, b):
        # 计算 a 的 b 次幂
        return a ** b

    def Sqrt(self, a):
        # 计算平方根
        if a < 0:
            raise ValueError("不能对负数开平方")
        return a ** 0.5

calc = ScientificCalc()
result = calc.Add(1, 3)
print(result)
print(calc.Subtract(6, 5))
print(calc.Multiply(2, 6))
print(calc.Divide(6, 2))
print(calc.Power(3, 2))
print("结束")
print("你好")
