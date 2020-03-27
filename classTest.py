#面向对象的编程:类的封装
# class Player():#定义一个类
#     def __init__(self,name,hp,occu):
#         self.name=name#变量被称作属性
#         self.__hp=hp#属性前面加上下划线后不能通过赋值去修改
#         self.occu=occu
#     def printRole(self):#定义一个方法
#         print('%s : %s %s'%(self.name,self.__hp,self.occu))
#     def updateName(self,newName):
#         self.name=newName
# user1= Player('tom','100','war')#类的实例化
# user2= Player('jerry','120','master')
# user1.printRole()
# user2.printRole()
# user1.updateName('tony')
# user1.printRole()

#类的继承
# class monster():
#     '定义怪物类'
#     def __init__(self,hp=100):
#         self.hp=hp
#     def run(self):
#         print('移动到某个位置')
# class animals(monster):
#     '普通怪物'
#     def __init__(self,hp=123):
#         super().__init__(hp)
# class boss(monster):
#     'boss类怪物'
#     def __init__(self,hp=123):
#         super().__init__(hp)#使用super继承，涉及到参数传递的顺序问题，如果父类的第一个参数为name，在子类中初始化hp时会把name初始化成hp的值
# a1=monster()
# print(a1.hp)
# a1.run()
# a2=animals()
# print(a2.hp)
# a2.run()
# a3=monster()
# print(a3.hp)
# a3.run()

class Monster():
    def __init__(self, name, hp=10011):
        self.name = name
        self.hp = hp
class Boss(Monster):
    '定义boss的内容，Monster的子类'
    def __init__(self, name, level, hp=101):
        super().__init__(hp)
        self.level = level
boss_10 = Boss(name='boss_10', level='99级', hp=900)
#把900（不是默认值）当作第一个参数值传入父类，而父类第一个属性是name，所以这个子类的实例的name就是900了
print(boss_10.name)