# 检测模型的启手式

import os

class 模型TAG:
    def __init__(self):
        pass


    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL",),
            }
        }

    RETURN_TYPES = ("STRING", )
    RETURN_NAMES = ("model_filename", )
    FUNCTION = "get_filename"
    CATEGORY = "人物TAG"

    def get_filename(self, model):
        model_name = "unknown"  # 默认值，以防获取失败

        # 检查 model 对象是否有 _load_list 属性
        if hasattr(model, "_load_list"):
            # 调用 _load_list 方法来获取实际的列表
            load_list = model._load_list()

            # 确保获取到的 load_list 是一个列表且不为空
            if isinstance(load_list, list) and load_list:
                first_load_item = load_list[0]

                # 检查 first_load_item 是否是元组，并且有足够的元素
                if isinstance(first_load_item, tuple) and len(first_load_item) > 0:
                    full_path = first_load_item[0]
                    # 使用 os.path.basename 从完整路径中提取文件名
                    model_name = os.path.basename(full_path)
                    print(f"GetModelFilename: Detected model name from _load_list: {model_name}")
                elif isinstance(first_load_item, str):  # 某些情况下可能直接是路径字符串
                    model_name = os.path.basename(first_load_item)
                    print(f"GetModelFilename: Detected model name from _load_list (string path): {model_name}")
                else:
                    print(f"Warning: _load_list()[0] is not a tuple or string as expected: {first_load_item}")
            else:
                print("Warning: _load_list() returned an empty list or not a list.")
        else:
            print("Warning: Model object has no '_load_list' attribute.")

        # 最终返回的模型名称
        return (model_name,)