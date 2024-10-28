import re

str = 'aabbabaabbaa'
# . 匹配除了换行符意外的任意字符
print(re.findall(r'a.b', str))  # ['aab', 'aab']

# * 前面的字符出现 0 次或以上
print(re.findall(r'a*b', str))  # ['aab', 'b', 'ab', 'aab', 'b']

# ? 表示前面的字符出现 0 次或 1 次
print(re.findall(r'a?b', str))  # ['ab', 'b', 'ab', 'b']

# .* 贪婪匹配，从 .* 前面为开始到后面为结束的所有内容
print(re.findall(r'a.*b', str))  # ['aabbabaabb'] 匹配到最大的内容

# *？ 非贪婪匹配，遇到开始和结束就进行截取，因此截取多次符合的结果，中国能建爱你没有字符串也会被截取
print(re.findall(r'a*?b', str))  # ['aab', 'b', 'ab', 'aab', 'b']

str1 = 'assssxxfsesb'
# (.*?) 这是一个捕获组，.* 匹配任意数量的任意字符（除了换行符），包括零个字符。捕获组意味着这部分匹配的内容会被保存起来，可以在后续使用。
print('xxxx result: ', re.findall(r'a(.*)b', str1))  # ['ssssxxfses']
