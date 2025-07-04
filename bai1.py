import requests
import random
import json
from hashlib import md5

class Baitag:
    def __init__(self):
        self.appid = '20230306001587954'
        self.appkey = 'fTgvtoBhR0YSfXV3OE2u'
        self.endpoint = 'http://api.fanyi.baidu.com'
        self.path = '/api/trans/vip/translate'
        self.url = self.endpoint + self.path

    def make_md5(self, s, encoding='utf-8'):
        return md5(s.encode(encoding)).hexdigest()

    def translate(self, query, from_lang='en', to_lang='zh'):
        # 生成一个随机数 salt，用于构造百度翻译 API 的签名 sign
        salt = random.randint(32768, 65536)

        # 调用 make_md5 方法，将 appid + query + salt + appkey 拼接并进行 MD5 加密，生成签名 sign
        sign = self.make_md5(self.appid + query + str(salt) + self.appkey)

        # 设置请求头，指定内容类型为 application/x-www-form-urlencoded
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        # 构造请求参数 payload，包含以下字段：
        payload = {
            'appid': self.appid,  # 百度翻译 API 的应用 ID
            'q': query,  # 需要翻译的文本内容
            'from': from_lang,  # 原始语言代码（默认为英文 'en'）
            'to': to_lang,  # 目标语言代码（默认为中文 'zh'）
            'salt': salt,  # 上面生成的随机数
            'sign': sign  # 经过 MD5 加密的签名
        }

        # 使用 requests 发送 POST 请求到百度翻译 API 的 URL 地址
        r = requests.post(self.url, params=payload, headers=headers)

        # 将返回结果解析为 JSON 格式
        result = r.json()

        # 判断返回结果中是否包含 'trans_result' 字段，表示翻译成功
        if 'trans_result' in result:
            # 提取翻译结果中的 'dst' 字段（即翻译后的文本），返回列表形式
            return [a['dst'] for a in result['trans_result']]
        else:
            # 如果没有翻译结果，抛出异常，并打印完整的错误响应信息
            raise Exception(f"Translation failed: {json.dumps(result, indent=4, ensure_ascii=False)}")

