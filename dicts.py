dicts = {"username":"xiaomin","password":123456}

#打印数组的所有key
print(dicts.keys())

#打印数组的所有value
print(dicts.values())

#向字典中添加key：value
dicts["age"] = 24
print(dicts)

#循环打印字典key和value
for k,v in dicts.items():
	print("dicts keys is %r"%k)
	print("dicts values is %r"%v)
