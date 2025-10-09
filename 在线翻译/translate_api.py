# -*- coding: utf-8 -*-
"""
模拟翻译 API（离线版）
函数签名
    trans, webinfo = connect(text, fromLanguage=0, toLanguage=0)
返回
    trans      : str  翻译结果
    webinfo    : dict 附加信息（置信度、耗时、假例句等）
语言代码
    0 自动  1 中文  2 英文  3 日文  4 韩文  5 法文  6 德文
"""

import random
import time

# 假装的支持语种
LANG = {0: "auto", 1: "zh", 2: "en", 3: "ja", 4: "ko", 5: "fr", 6: "de"}

# 假词库：key 为 (原文, 源语言, 目标语言)
# 放在 fake_translator.py 顶部
LANG = {0: "auto", 1: "zh", 2: "en", 3: "ja", 4: "ko", 5: "fr", 6: "de"}

# 3×3 英→中/日/韩
FAKE_DICT = {
    # 英文 hello
    ("hello", 2, 1): "你好",
    ("hello", 2, 3): "こんにちは",
    ("hello", 2, 4): "안녕하세요",

    # 中文 你好
    ("你好", 1, 2): "Hello",
    ("你好", 1, 3): "こんにちは",
    ("你好", 1, 4): "안녕하세요",

    # 日文 こんにちは
    ("こんにちは", 3, 1): "你好",
    ("こんにちは", 3, 2): "Hello",
    ("こんにちは", 3, 4): "안녕하세요",

    # 韩文 안녕하세요
    ("안녕하세요", 4, 1): "你好",
    ("안녕하세요", 4, 2): "Hello",
    ("안녕하세요", 4, 3): "こんにちは",
}

def connect(text: str, fromLanguage: int = 0, toLanguage: int = 0):
    """
    模拟翻译主入口
    """
    # 1. 随机延迟 80~300 ms，让界面有“加载”感觉
    time.sleep(random.uniform(0.08, 0.3))

    # 2. 构造唯一键
    key = (text.strip().lower(), fromLanguage, toLanguage)

    # 3. 优先查“词典”
    trans = FAKE_DICT.get(key, None)

    # 4. 没命中就造一个假的
    if trans is None:
        if toLanguage == 1:   # 目标中文
            trans = f"[假]已翻译：{text}"
        elif toLanguage == 2:  # 目标英文
            trans = f"[fake] {text}"
        else:
            trans = f"[mock] {text}"

    # 5. 组装 webinfo
    webinfo = {
        "from": LANG.get(fromLanguage, "unknown"),
        "to": LANG.get(toLanguage, "unknown"),
        "confidence": round(random.uniform(0.85, 0.99), 4),
        "translateTime": f"{random.randint(120, 350)} ms",
        "example": [
            {"src": text, "dst": trans},
            {"src": "another line", "dst": "另一行假数据"}
        ]
    }

    return trans, webinfo


# 简单自测
if __name__ == "__main__":
    print(connect("hello", 2, 1))
    print(connect("翻译", 1, 2))