import re

# (1)使用正则表达式匹配出<html><h1>www.baidu.com</h1></html>中的地址
source = '<html><h1>www.baidu.com</h1></html>'
pattern = r'<h1>(.*?)</h1>'
print(re.compile(pattern).findall(source)[0])


# (2)a="张明 98 分"，用 re.sub，将 98 替换为 100
a = "张明 98 分"
res = re.sub(r'\d+', '100', a)
print(res)

# (3)正则表达式匹配中(.*)和(.*?)匹配区别？
# 答：(.*) 为贪婪模式极可能多的匹配内容 ,(.*?) 为非贪婪模式又叫懒惰模式，一般匹配到结果就好，匹配字符的少为主，示例代码如下
s = "<html><div>文本 1</div><div>文本 2</div></html>"
pat1 = re.compile(r'<div>(.*?)</div>') #懒惰模式
print(pat1.findall(s))

pat2 = re.compile(r'<div>(.*)</div') #贪婪模式
print(pat2.findall(s))


# (4) 写一段匹配邮箱的正则表达式
'''
电子邮件地址有统一的标准格式：用户名@服务器域名。
用户名表示邮件信箱、注册名或信件接收者的用户标识，@符号后是你使用的邮件服务器的域名。
@可以读成“at”，也就是“在”的意思。整个电子邮件地址可理解为网络中某台服务器上的某个用户的地址。

1.用户名，可以自己选择。由字母 a～z(不区分大小写)、数字 0～9、点、减号或下划线组成；只能以数字或字母开头和结尾。
2.与你使用的网站有关，代表邮箱服务商。例如网易的有@163.com 新浪有@vip.sina.com 等。

正则表达式如下：
r"^[a-zA-Z0-9]+[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

1.首先强调一点关于\w 的含义，\w 匹配英文字母和俄语字母或数字或下划线或汉字。
2.注意^[]和[^]的区别，[]表示字符集合，^[]表示已[]内的任意字符集开始，[^]表示。
3.^[a-zA-Z0-9]+：这里注意^[]和[^]的,第一个^表示已什么开头，第二个[]的^表示不等于[]内。所以这段表示以英文字母和数字开头，后面紧跟的+，限定其个数>=1 个。
4.[a-zA-Z0-9.+-]+：表示匹配英文字母和数字开头以及.+-, 的任意一个字符，并限定其个数>=1 个。为了考虑@前面可能出现.+-（但是不在开头出现）。
5.@就是邮箱必备符号了
6.@[a-zA-Z0-9-]+.：前面的不用说了，后面的.表示.转义了,也是必备符号。
7.[ a-zA-Z0-9-.]+：$符表示以什么结束,这里表示以英文字和数字或 -. 1 个或多个结尾。

'''

email_pattern = r'^[a-zA-Z0-9]+[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
result = re.compile(email_pattern).findall('723abc@163.com')
print(result)

