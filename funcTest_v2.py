#使用闭包编写一个计数器
def counter(first=0):
    lista = [first]
    def addOne():
        lista[0]+=1
        return lista[0]
    return addOne
num1=counter()
# for i in range(1,5):
#     print(num1())
num5=counter(5)
print(num5())