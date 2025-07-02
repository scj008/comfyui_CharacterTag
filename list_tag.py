import os
import csv

class 列表TAG:
    """
    最基础的合成提示词框架
    """
    CSV_FILE_PATH = os.path.join("mychkp", "tag_1.csv")  # 替换为你的CSV文件的实际路径

    def __init__(self):
        pass


    @classmethod
    def read_csv(cls):
        """
        从CSV里读取列表数据
        """
        list_tag = []
        try:
            file_path = os.path.join(os.path.dirname(__file__), cls.CSV_FILE_PATH)
            print(f"正在读取文件: {file_path}")
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                header_skipped = False  # 控制是否跳过首行
                for row in reader:
                    if not header_skipped:
                        header_skipped = True
                        continue
                    if row:  # 避免空行
                        list_tag.append(row[0])
        except FileNotFoundError:
            print(f"找不到文件: {file_path}")
        except Exception as e:
            print(f"读取文件时发生错误: {e}")
        return list_tag

    @classmethod
    def INPUT_TYPES(cls):
        list_tag = cls.read_csv() or [
            "使用模型提示词",
            "使用人物外观",
            "使用人物服装",
            "使用人物表情",
            "镜头"
        ]

        return {
            "required": {
                "使用模型提示词": ("BOOLEAN", {"default": True}),
                "input_text": (list_tag, {
                    "default": "模型提示词",
                }),
            },
            "optional": {
                "文本输入": ("STRING", {"forceInput": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("文本输出", )

    FUNCTION = "test"
    CATEGORY = "人物TAG"

    def test(self, 使用模型提示词, input_text, 文本输入=None):
        xx1 = ""
        if 文本输入 is None:
            文本输入 = ""
        else:
            文本输入 += ","

        xx1 = input_text
        combined_text = f"{文本输入}{xx1}".strip(",")
        return (combined_text,)
