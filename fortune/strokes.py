# 汉字笔画数查询模块
# 数据来源：zhHanSequence (BSD-2-Clause License)
# https://github.com/DongSky/zhHanSequence

import os

# 缓存笔画数据
_stroke_cache = {}
_data_loaded = False


def _load_stroke_data():
    """加载笔画数据文件"""
    global _data_loaded
    if _data_loaded:
        return

    data_file = os.path.join(os.path.dirname(__file__), 'bihua.txt')
    if not os.path.exists(data_file):
        _data_loaded = True
        return

    with open(data_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or ':' not in line:
                continue
            char, strokes_str = line.split(':', 1)
            strokes = [s.strip() for s in strokes_str.split(',') if s.strip()]
            # 有些字有多个变体，保留第一个遇到的
            if char not in _stroke_cache:
                _stroke_cache[char] = len(strokes)

    _data_loaded = True


def get_stroke_count(char):
    """
    获取单个汉字的笔画数
    返回值：笔画数，如果找不到返回 None
    """
    _load_stroke_data()
    return _stroke_cache.get(char)


def get_name_stroke_counts(name):
    """
    获取姓名中每个字的笔画数
    name: 姓名字符串
    返回值：[(字, 笔画数), ...]，找不到的字笔画数为 None
    """
    _load_stroke_data()
    result = []
    for char in name:
        if '一' <= char <= '鿿':  # 只处理CJK汉字
            result.append((char, _stroke_cache.get(char)))
        else:
            result.append((char, None))
    return result


def get_total_strokes(name):
    """
    获取姓名总笔画数
    如果有字找不到，返回 None
    """
    counts = get_name_stroke_counts(name)
    total = 0
    for _, count in counts:
        if count is None:
            return None
        total += count
    return total


if __name__ == '__main__':
    # 简单测试
    test_names = ['李', '明', '王', '小']
    for n in test_names:
        print(f'{n}: {get_stroke_count(n)} 画')
