from rich import print
from transformers import AutoTokenizer, AutoModel
import os

chat_gml6bPath = '/Users/jakequc/Desktop/learn-codes/py-learning/ChatGLM-6B/chatglm-6b'


# 提供相似，不相似的语义匹配例子
examples = {
    '是': [
        ('公司ABC发布了季度财报，显示盈利增长。', '财报披露，公司ABC利润上升。'),
    ],
    '不是': [
        ('黄金价格下跌，投资者抛售。', '外汇市场交易额创下新高。'),
        ('央行降息，刺激经济增长。', '新能源技术的创新。')
    ]
}


# 构造 init_prompts() 函数
def init_prompts():
    """
    初始化前置 prompt, 便于模型做 incontext learning
    """
    pre_history = [
        (
            '现在你需要帮助我完成文本匹配任务，当我给你两个句子时，你需要回答我这两句话语义是否相似。只需要回答是否相似，不要做多余的回答。',
            '好的，我将只回答”是“或”不是“。'
        )
    ]

    for key, sentence_pairs in examples.items():
        for sentence1, sentence2 in sentence_pairs:
            pre_history.append(
                (f"句子一:{sentence1}\n 句子二:{sentence2}\n 是否相似", key))

    return {'pre_history': pre_history}


def inference(sentence_pairs: list, custom_settings: dict):
    """
    推理函数
    Args:
        sentence_pairs(list[tuple[str, str]]): 待推理的句子对
        custom_settings(dict): 初始设定，包含人为给定的 few-shot example
    """
    # init chat gml model
    device = 'cpu'
    tokenizer = AutoTokenizer.from_pretrained(
        chat_gml6bPath, trust_remote_code=True)
    model = AutoModel.from_pretrained(
        chat_gml6bPath, trust_remote_code=True).float()

    model.to(device)

    for sentence1, sentence2 in sentence_pairs:
        sentence_with_prompt = f"""
        句子1: {sentence1}
        句子2: {sentence2}
        这两句话语义是否相似？
        """
        response, history = model.chat(
            tokenizer, sentence_with_prompt,
            history=custom_settings['pre_history'])
        print(f""">>>  Sentence 1: {
              sentence1}, Sentence 2: {sentence2}""")
        print(f'>>>inference answer: {response}')


if __name__ == "__main__":

    sentence_pairs = [
        ('股票市场今日大涨，投资者乐观。', '持续上涨的市场让投资者感到满意。'),
        ('油价大幅下跌，能源公司面临挑战。', '未来智能城市的建设趋势愈发明显。'),
        ('利率上升，影响房地产市场。', '高利率对房地产有一定冲击。'),
    ]

    custom_settings = init_prompts()

    inference(
        sentence_pairs,
        custom_settings
    )
