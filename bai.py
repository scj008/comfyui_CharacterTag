import re
from bai1 import Baitag

# 原始字符串
aa = '''score_9, score_8_up, score_7_up,in  , (a lot of :1.5), 
1girl, solo, black hair, 
brown eyes, straight hair,  long hair, bangs, head out of frame,
      '''

# 实例化翻译类
fan = Baitag()

# Step 1: 提取原始字符串中的标点位置及符号
# 使用正则保留标点及其位置信息
temp_aa = aa.replace('\n', '__COMMA__')
print(fan.translate(temp_aa))


