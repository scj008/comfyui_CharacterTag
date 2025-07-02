import os
import time
class Opentag:
    """
    提示词第二行，
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

                "使用人物外观": ("BOOLEAN", {"default": True}),
                "input_text1": ("STRING", {  # 输入是文本类型
                    "default": "人物外观提示词",
                    "multiline": True  # 支持多行输入
                }),

                "测试替换1": ("BOOLEAN", {"default": False}),  # 新增的BOOLEAN
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

    JS = f"js/boole.js?t={int(time.time())}"  # 更标准，首字母大写

    # 6-20 原始状态 ++ def test(self, 使用模型提示词, 使用人物外观, input_text, input_text1, 文本输入=None,):
    def test(self, 使用模型提示词, 使用人物外观, input_text, input_text1, 测试替换1=False, 文本输入=None,):
        if 文本输入 is None:
            文本输入 = ""
        else:
            文本输入 += ","

        # if 测试替换1:
        #     input_text = "测试值"

        model_prompt = input_text if 使用模型提示词 else ""
        appearance_prompt = input_text1 if 使用人物外观 else ""

        combined_text = f"{文本输入}{model_prompt},{appearance_prompt}".strip(",")
        # 文本框内容合并
        # print(input_text)
        return (combined_text,)