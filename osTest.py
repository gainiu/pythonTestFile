import os,sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

print(os.path.abspath('.'))
print(os.path.exists('TEST1/txt/name.txt'))

from pathlib import Path
p=Path('./TEST1')
print(p.resolve())
q=Path('./TEST1/q')
Path.mkdir(q,parents=True)#创建文件夹
