import re
def findItem(hero):
    with open('TEST1\\txt\\sanguo.txt',encoding='GB18030') as f:
        data = f.read().replace('\n','')
        nameNum = re.findall(hero,data)
        print(' %s 出现了 %s 次'%(hero,len(nameNum)))
    return len(nameNum)

# #读取人物信息
# nameDict={}
# with open('TEST1\\txt\\name.txt',encoding='UTF-8') as f:
#     for line in f:
#         names = line.split('|')
#         for n in names:
#             # print(n)
#             nameNum = findItem(n)
#             nameDict[n] = nameNum

#读取武器信息
# def findWeapon(weapon):
#     with open('TEST1\\txt\\sanguo.txt',encoding='GB18030') as f:
#         data = f.read().replace('\n','')
#         weaponNum = re.findall(weapon,data)
#         print('兵器 %s 出现了 %s 次'%(weapon,len(weaponNum)))
#     return len(weaponNum)


weaponDict = {}
with open('TEST1\\txt\\weapon.txt', encoding='UTF-8') as f:
    i = 1
    for line in f:
        if i % 2 == 1:
            nameNum = findItem(line.strip('\n'))
            weaponDict[line] = nameNum
        i += 1
