# 综合算命系统后端（兼主服务器）
# 整合生辰八字、姓名五格、易经推断
# 同时服务俄罗斯方块、易经占卜、八字分析等静态页面

import sys
import os

# 添加 bazi 目录到路径，以便复用八字计算模块
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'bazi'))

from flask import Flask, jsonify, make_response, abort, request, send_from_directory
import metaphysic

from .strokes import get_stroke_count
from .wuge import calculate_wuge, get_wuge_summary
from .yijing_fate import generate_hexagram_from_info, get_life_prediction

app = Flask(__name__)

# 项目根目录
ROOT_DIR = os.path.join(os.path.dirname(__file__), '..')


# ========== 静态页面服务 ==========

@app.route('/')
def index():
    """俄罗斯方块"""
    return send_from_directory(ROOT_DIR, 'index.html')


@app.route('/i-ching/')
def i_ching_index():
    return send_from_directory(os.path.join(ROOT_DIR, 'i-ching'), 'index.html')


@app.route('/i-ching/<path:filename>')
def i_ching_static(filename):
    return send_from_directory(os.path.join(ROOT_DIR, 'i-ching'), filename)


@app.route('/bazi/')
def bazi_index():
    return send_from_directory(os.path.join(ROOT_DIR, 'bazi'), 'index.html')


@app.route('/bazi/<path:filename>')
def bazi_static(filename):
    return send_from_directory(os.path.join(ROOT_DIR, 'bazi'), filename)


@app.route('/fortune/')
def fortune_index():
    return send_from_directory(os.path.dirname(__file__), 'index.html')


@app.route('/fortune/<path:filename>')
def fortune_static(filename):
    return send_from_directory(os.path.dirname(__file__), filename)


# ========== API 服务 ==========

@app.route('/api/metaphysic', methods=['POST'])
def get_metaphysic_info():
    """八字 API（兼容原 bazi/server.py）"""
    if not request.json or 'year' not in request.json or 'month' not in request.json or 'day' not in request.json or 'hour' not in request.json:
        abort(400)

    birthInfo = {
        'year': int(request.json['year']),
        'month': int(request.json['month']),
        'day': int(request.json['day']),
        'hour': int(request.json['hour'])
    }
    shenchenbazi = metaphysic.getShenChenBaZi(
        birthInfo['year'], birthInfo['month'], birthInfo['day'],
        birthInfo['hour'])
    wuxing = metaphysic.getWuXing(shenchenbazi)
    return jsonify({'shenchenbazi': shenchenbazi, 'wuxing': wuxing})


@app.route('/api/fortune', methods=['POST'])
def get_fortune():
    """
    综合算命 API
    请求参数：
    {
        "name": "姓名",
        "surname": "姓",
        "givenName": "名",
        "year": 1990,
        "month": 5,
        "day": 15,
        "hour": 12
    }
    """
    if not request.json:
        abort(400)

    required_fields = ['name', 'surname', 'givenName', 'year', 'month', 'day', 'hour']
    for field in required_fields:
        if field not in request.json:
            abort(400)

    name = request.json['name']
    surname = request.json['surname']
    given_name = request.json['givenName']
    year = int(request.json['year'])
    month = int(request.json['month'])
    day = int(request.json['day'])
    hour = int(request.json['hour'])

    try:
        # 1. 生辰八字
        shenchenbazi = metaphysic.getShenChenBaZi(year, month, day, hour)
        wuxing = metaphysic.getWuXing(shenchenbazi)

        # 找出五行中最旺的
        wuxing_names = ["木", "火", "土", "金", "水"]
        max_idx = wuxing.index(max(wuxing))
        dominant_wuxing = wuxing_names[max_idx]

        # 2. 姓名五格
        wuge = calculate_wuge(surname, given_name)
        wuge_summary = get_wuge_summary(wuge)

        # 3. 易经卦象
        hexagram = generate_hexagram_from_info(name, year, month, day, hour)

        # 4. 综合人生推断
        life_prediction = get_life_prediction(hexagram, wuge_summary, shenchenbazi)

        result = {
            "name": name,
            "bazi": {
                "shenchenbazi": shenchenbazi,
                "wuxing": wuxing,
                "dominant": dominant_wuxing,
                "wuxing_percent": {
                    "木": round(wuxing[0] * 100, 1),
                    "火": round(wuxing[1] * 100, 1),
                    "土": round(wuxing[2] * 100, 1),
                    "金": round(wuxing[3] * 100, 1),
                    "水": round(wuxing[4] * 100, 1),
                }
            },
            "wuge": wuge,
            "hexagram": {
                "name": hexagram["name"],
                "symbol": hexagram["symbol"],
                "text": hexagram["text"],
                "meaning": hexagram["meaning"],
                "fate": hexagram["fate"]
            },
            "lifePrediction": life_prediction,
            "disclaimer": "本结果仅供娱乐参考，不代表真实命运预测。"
        }

        return jsonify(result)

    except ValueError as e:
        return make_response(jsonify({'error': str(e)}), 400)
    except Exception as e:
        return make_response(jsonify({'error': '测算过程出错：' + str(e)}), 500)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5001)
