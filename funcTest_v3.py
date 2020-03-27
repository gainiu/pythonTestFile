#用闭包实现3个数的运算：其中2个数固定，只有一个数变化
def outLine(a,b):
    def inLine(x):
        return a*x+b
    return inLine
num1 = outLine(2,3)
num2 = outLine(3,6)
print(num1(5))
print(num2(3))

#使用lambda+闭包，函数更优雅
def outLine1(a,b):
    return lambda x: a*x+b
num3 = outLine1(1,2)
print(num3(3))