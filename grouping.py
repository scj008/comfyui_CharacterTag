class 人物TAG:
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

                "使用人物外观": ("BOOLEAN", {"default": True}),
                "input_text1": ("STRING", {  # 输入是文本类型
                    "default": "人物外观",
                    "multiline": True  # 支持多行输入
                }),

                "使用人物服装": ("BOOLEAN", {"default": True}),
                "input_text2": ("STRING", {  # 输入是文本类型
                    "default": "人物服装",
                    "multiline": True  # 支持多行输入
                }),

                "使用人物表情": ("BOOLEAN", {"default": True}),
                "input_text3": ("STRING", {  # 输入是文本类型
                    "default": "人物表情",
                    "multiline": True  # 支持多行输入
                }),

                "镜头": ("BOOLEAN", {"default": True}),
                "input_text4": ("STRING", {  # 输入是文本类型
                    "default": "镜头",
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

    # 6-20 原始状态 ++ def test(self, 使用模型提示词, 使用人物外观, input_text, input_text1, 文本输入=None,):
    def test(self, 使用模型提示词, 使用人物外观, 使用人物服装, 使用人物表情, 镜头,
             input_text, input_text1,input_text2,input_text3,input_text4, 文本输入=None,):

        xx1 = ""
        if 文本输入 is None:
            文本输入 = ""
        else:
            文本输入 += ","

        field = {
            "使用模型提示词": "input_text",
            "使用人物外观": "input_text1",
            "使用人物服装": "input_text2",
            "使用人物表情": "input_text3",
            "镜头": "input_text4"
        }

        for lx, tex in field.items():
            xx1 += tex if lx else ""

        # model_prompt = input_text if 使用模型提示词 else ""
        # appearance_prompt = input_text1 if 使用人物外观 else ""

        combined_text = f"{文本输入}{xx1}".strip(",")
        # 文本框内容合并
        # print(input_text)
        return (combined_text,)