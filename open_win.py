"""
这个应用是做联合JS来打开边上一个窗口的应用；
需要在文本输入框边上加入一个提示中文的文本框；

第二阶段打开百度翻译，翻译这些文本框里的内容；
"""
import requests
import random
import json
from hashlib import md5

class BaiduTranslator:
    def __init__(self):
        self.appid = '20230306001587954'
        self.appkey = 'fTgvtoBhR0YSfXV3OE2u'
        self.endpoint = 'http://api.fanyi.baidu.com'
        self.path = '/api/trans/vip/translate'
        self.url = self.endpoint + self.path

    def make_md5(self, s, encoding='utf-8'):
        return md5(s.encode(encoding)).hexdigest()

    def translate(self, query, from_lang='en', to_lang='zh'):
        salt = random.randint(32768, 65536)
        sign = self.make_md5(self.appid + query + str(salt) + self.appkey)

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {
            'appid': self.appid,
            'q': query,
            'from': from_lang,
            'to': to_lang,
            'salt': salt,
            'sign': sign
        }

        r = requests.post(self.url, params=payload, headers=headers)
        result = r.json()

        if 'trans_result' in result:
            return [a['dst'] for a in result['trans_result']]
        else:
            raise Exception(f"Translation failed: {json.dumps(result, indent=4, ensure_ascii=False)}")


# 使用示例
class 百度翻译TAG:
    """
    最基础的合成提示词框架
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "使用模型提示词": ("BOOLEAN", {"default": True}),
                "input_text": ("STRING", {  # 输入是文本类型
                    "default": "模型提示词",
                    "multiline": True  # 支持多行输入
                }),
                "input_text1": ("STRING", {  # 输入是文本类型
                    "default": "模型提示词",
                    "multiline": True  # 支持多行输入
                }),

            },
            "optional": {
                "文本输入": ("STRING", {"forceInput": True}),
                # 连线输入内容
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("文本输出", )

    FUNCTION = "test"
    #OUTPUT_NODE = False

    CATEGORY = "人物TAG"

    JS = f"js/btag1.js?t={int(time.time())}"  # 更标准，首字母大写

    # 6-20 原始状态 ++ def test(self, 使用模型提示词, 使用人物外观, input_text, input_text1, 文本输入=None,):
    def test(self, 使用模型提示词, input_text,input_text1, 文本输入=None,):

        xx1 = ""
        if 文本输入 is None:
            文本输入 = ""
        else:
            文本输入 += ","


        model_prompt = input_text if 使用模型提示词 else ""
        combined_text = f"{文本输入}{model_prompt}".strip(",")

        translator = BaiduTranslator()
        translated_texts = translator.translate(combined_text)

        # 假设返回第一个结果（或多行合并）
        translated_result = ' '.join(translated_texts)



        # 文本框内容合并
        # print(input_text)
        return (translated_result,)