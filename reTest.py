#正则表达式库
import re

p = re.compile('a')
print(p.match('aaa'))

pp=re.compile('a*b')
print(pp.match('aaaaabbbbb'))

#. ^ $ * + ? {m} {m,n} [] | \d \D \s ()
#^s
#.*?
ppp=re.compile('.')#匹配任意单个字符
print(ppp.match('asdf'))

pppp=re.compile('txt$')#匹配结尾字符
print(pppp.match('xxx.txt'))

ppppp=re.compile('ca*t')#匹配星号前面的字符出现0次到多次
print(ppppp.match('ct'))

pppppp=re.compile('ca+t')#匹配加号前面的字符1次到多次
print(pppppp.match('caaaaat'))

p=re.compile('ca{3}t')#a出现3次的时候才能匹配
print(p.match('caaaat'))

p=re.compile('ca{3,4}t')#a出现3到4次的时候可以匹配
print(p.match('caaaat'))

p = re.compile('c[abcd]t')#中括号里的任意字符都可以匹配
print(p.match('cat'))

# \d 匹配单个数字，范围是0-9
# \d+ 匹配多个连续数字
# \d{5} 匹配指定个数(5个)的数字

#\s匹配字符串，a-z

p=re.compile(r'(\d+)-(\d+)-(\d+)')
print(p.match('2019-12-31').group(3))
year,month,day = p.match('2019-12-31').groups()

# match 必须从字符串开头进行匹配,相当于自带了一个 ^,search则不要求从开头
p=re.compile(r'(\d+)-(\d+)-(\d+)')
print(p.search('aa2019-12-31bb'))

#sub函数可以做字符替换
phone='123-23-45 #这里是电话号码'
p2=re.sub(r'\D','',phone)
print(p2)
p3=re.sub(r'#.*$','',phone)
print(p3)

#findall函数可以匹配多次