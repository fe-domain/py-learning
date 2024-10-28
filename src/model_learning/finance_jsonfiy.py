import re  # 正则
import json
from rich import print
from transformers import AutoTokenizer, AutoModel


chat_gml6bPath = '/Users/jakequc/Desktop/learn-codes/py-learning/ChatGLM-6B/chatglm-6b'

# 定义不同实体下的具备属性
schema = {
    '金融': ['日期', '股票名称', '开盘价', '收盘价', '成交量'],
}

IE_PATTERN = """{}\n\n提取上述句子中{}的实体，并按照JSON格式输出，上述句子中不存在的信息用['原文中未
提及']来表示，多个值之间用','分隔。"""

# 提供一些例子供模型参考
ie_examples = {
    '金融': [
        {
            'content': """2023-01-10，股市震荡。股票古哥-D[EOOE]美股今日开盘价100美元，一度飙升至105美元，随后回落至98美元，最终以102美元收盘，成交量达到520000。""",
            'answers': {
                '日期': '2023-01-10',
                '股票名称': '古哥-D[EOOE]美股',
                '开盘价': '100美元',
                '收盘价': '102美元',
                '成交量': '520000',
            }
        }
    ]
}


# define init_prompts function
def init_prompts():
    """
    初始设定，包含人为给定的 few-shot example
    """
    ie_pre_history = [
        (
            """现在你需要帮助我完成信息抽取任务，当我给你一个句子时，你需要帮我抽取出句子中实体信息，并
按照JSON的格式输出，上述句子中没有的信息用['原文中未提及']来表示，多个值之间用','分隔。""",
            '好的，我已经准备好了。'
        )
    ]

    for _type, example_list in ie_examples.items():
        print(f"type: {_type}, 信息抽取样本的原始句子是： {example_list}")
        for example in example_list:
            sentence = example["content"]
            properties_str = ", ".join(schema[_type])
            schema_str_list = f'"{_type}"({properties_str})'
            sentence_with_prompt = IE_PATTERN.format(sentence, schema_str_list)
            ie_pre_history.append(
                (f"{sentence_with_prompt}", json.dumps(
                    example['answers'],
                    ensure_ascii=False)))
    return {
        "ie_pre_history": ie_pre_history
    }


def clean_response(response: str):
    """
    后处理模型输出。
    Args:
    response (str): _description_
    """
    if '```json' in response:
        res = re.findall(r'```json(.*?)```', response)
    if len(res) and res[0]:
        response = res[0]
        response.replace('、', ',')
    try:
        return json.loads(response)
    except:
        return response


def inference(sentences: list, custom_settings: dict):
    """
    推理函数
    Args:
        sentences(list[str]): 待推理的句子
        custom_settings(dict): 初始设定，包含人为给定的 few-shot example
    """
    for sentence in sentences:
        cls_res = "金融"
        if cls_res not in schema:
            print(f'''The type model inferenced {
                  cls_res} which is not in schema dict, exited.''')
            exit()
        properties_str = ", ".join(schema[cls_res])
        schema_str_list = f'"{cls_res}"({properties_str})'
        sentence_with_ie_prompt = IE_PATTERN.format(sentence, schema_str_list)
        print("sentence_with_ie_prompt: ", sentence_with_ie_prompt)
        ie_res = model.chat(tokenizer, sentence_with_ie_prompt,
                            history=custom_settings["ie_pre_history"])
        print(f">>> [bold bright_red] sentence: {sentence}")
        print(f">>> [bold bright_green] ie_res: {ie_res}")


if __name__ == '__main__':
    device = 'cpu'
    tokenizer = AutoTokenizer.from_pretrained(
        chat_gml6bPath, trust_remote_code=True)

    model = AutoModel.from_pretrained(
        chat_gml6bPath, trust_remote_code=True).float()

    model.to(device)
    sentences = [
        '''2023-02-15，寓意吉祥的节日，股票佰笃[BD]美股开盘价10美元，虽然经历了波动，但最终以13美元
    收盘，成交量微幅增加至460,000，投资者情绪较为平稳。''',
        '''2023-04-05，市场迎来轻松氛围，股票盘古(0021)开盘价23元，尽管经历了波动，但最终以26美元收
    盘，成交量缩小至310,000，投资者保持观望态度。''',
    ]
    custom_settings = init_prompts()

    inference(
        sentences,
        custom_settings
    )