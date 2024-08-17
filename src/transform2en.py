# 导入工具包
from transformers import AutoModelWithLMHead,AutoTokenizer,pipeline

# AutoModelWithLMHead：一个用于自动下载并加载预训练语言模型（带有语言模型头部的模型）的类。

mode_name = 'liam168/trans-opus-mt-zh-en'

# 指明预训练模型
model = AutoModelWithLMHead.from_pretrained(mode_name)

# 加载词潜入层
tokenizer = AutoTokenizer.from_pretrained(mode_name)

# 使用管道的方式进行机器翻译
translation = pipeline("translation_zh_to_en", model=model, tokenizer=tokenizer)

# 输出结果
print(translation('我喜欢学习数据科学和机器学习。', max_length=400))
