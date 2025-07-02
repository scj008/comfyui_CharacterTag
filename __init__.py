
from .grouping import 人物TAG
from .openchkptag import Opentag
from .mod_tag import 模型TAG
from .list_tag import 列表TAG

from aiohttp import web
from server import PromptServer


# 包含要导出的所有节点及其名称的字典
# 注意：名称应全局唯一
@PromptServer.instance.routes.get("/hello")
async def get_hello(request):
    return web.json_response("hello")


NODE_CLASS_MAPPINGS = {
    "人物提示词分组": 人物TAG,
    "打开提示词标签": Opentag,
    "模型提示词分组": 模型TAG,
    "人物列表": 列表TAG
}

# 包含节点友好/人类可读标题的字典
NODE_DISPLAY_NAME_MAPPINGS = {
    "Example1": "提示词分组"
}

# # 关键：告诉ComfyUI加载js文件
# WEB_DIRECTORY = "./web/js"
# __all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]


# 关键：确保指向web目录
WEB_DIRECTORY = "./js"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]