from rich import print
from rich.console import Console
from transformers import AutoTokenizer, AutoModel

# 提供所有类别以及每个类别下的样例
class_examples = {
    '新闻报道': '今日，股市经历了一轮震荡，受到宏观经济数据和全球贸易紧张局势的影响。投资者密切关注美联储可能的政策调整，以适应市场的不确定性。',
    '财务报告': '本公司年度财务报告显示，去年公司实现了稳步增长的盈利，同时资产负债表呈现强劲的状况。经济环境的稳定和管理层的有效战略执行为公司的健康发展奠定了基础。',
    '公司公告': '本公司高兴地宣布成功完成最新一轮并购交易，收购了一家在人工智能领域领先的公司。这一战略举措将有助于扩大我们的业务领域，提高市场竞争力',
    '分析师报告': '最新的行业分析报告指出，科技公司的创新将成为未来增长的主要推动力。云计算、人工智能和数字化转型被认为是引领行业发展的关键因素，投资者应关注这些趋势'
}


def init_prompts():
    """
    初始化前置 prompt，便于模型做 in context learning(ICL)
    """
    class_list = list(class_examples.keys())
    pre_history = [
        (
            f'现在你是一个文本分类器，你需要按照要求将我给你的句子分类到：{class_list}类别中。',
            '好的。'
        )
    ]

    # items() 返回一个 dict_items 元祖数组
    for _type, example in class_examples.items():
        pre_history.append((f'"{example}" 是 {class_list} 里的什么类别?', _type))

    print("class_list: ", class_list)
    print(" class_examples.items(): ",  class_examples.items())

    return {
        'class_list': class_list,  # 类列表，用来进行分类的
        'pre_history': pre_history  # 提供上下文的问题，唤醒模型的推理能力
    }

# def inference(sentences: list, )


def fun(a: int, b: int) -> int:
    return a + b


fun(1, 2)


def inference(sentences: list, custom_settings: dict):
    """
    推理函数
    Args:
        sentences(list[str]): 待推理的句子
        custom_settings(dict): 初始设定，包含人为给定的 few-shot example
    """
    for sentence in sentences:
        with console.status("[bold bright_green] Model Inference..."):
            sentence_with_prompt = f"""'{sentence}' 是 {
                custom_settings['class_list']} 里的什么类别？"""
            response, history = model.chat(
                tokenizer, sentence_with_prompt, history=custom_settings['pre_history'])
            print(f'>>> [bold bright_red] sentence: {sentence}')
            print(f'>>> [bold bright_green] inference answer: {response}')


chat_gml6bPath = '/Users/jakequc/Desktop/learn-codes/py-learning/ChatGLM-6B/chatglm-6b'

if __name__ == '__main__':
    console = Console()
    # device = 'cuda: 0'
    device = 'cpu'
    tokenizer = AutoTokenizer.from_pretrained(
        chat_gml6bPath, trust_remote_code=True)
    # model = AutoModel.from_pretrained(chat_gml6bPath, trust_remote_code=True).half().cuda()
    model = AutoModel.from_pretrained(
        chat_gml6bPath, trust_remote_code=True).float()
    model.to(device)
    sentences = [
        "今日，央行发布公告宣布降低利率，以刺激经济增长。这一降息举措将影响贷款利率，并在未来几个季度内对金融市场产生影响。",
        "ABC公司今日发布公告称，已成功完成对XYZ公司股权的收购交易。本次交易是ABC公司在扩大业务范围、加强市场竞争力方面的重要举措。据悉，此次收购将进一步巩固ABC公司在行业中的地位，并为未来业务发展提供更广阔的发展空间。详情请见公司官方网站公告栏",
        "公司资产负债表显示，公司偿债能力强劲，现金流充足，为未来投资和扩张提供了坚实的财务基础。",
        "最新的分析报告指出，可再生能源行业预计将在未来几年经历持续增长，投资者应该关注这一领域的投资机会",
    ]

    custom_settings = init_prompts()
    print(custom_settings)

    inference(
        sentences,
        custom_settings
    )