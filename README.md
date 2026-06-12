# 🎮🔮 休闲游戏与占卜合集

本仓库包含四个项目：**俄罗斯方块游戏**、**易经占卜**、**生辰八字命理分析** 和 **综合命理测算系统**。

---

## 🎮 俄罗斯方块 (Tetris)

一个使用原生 HTML5 Canvas 和 JavaScript 编写的经典俄罗斯方块游戏。

### 运行方式

直接在浏览器中打开项目根目录下的 `index.html` 即可开始游戏。

### 功能特性

- 🎯 经典俄罗斯方块玩法
- 🎨 精美的霓虹暗色主题 UI
- 📊 实时分数、等级、消除行数统计
- 👀 下一个方块预览
- 🌑 方块下落阴影提示
- ⏩ 硬降（空格键直接落到底部）
- ⏸️ 暂停/继续功能
- 📈 随等级提升速度加快

### 操作说明

| 按键 | 功能 |
|------|------|
| ⬅️ 左箭头 | 向左移动 |
| ➡️ 右箭头 | 向右移动 |
| ⬇️ 下箭头 | 加速下落 |
| ⬆️ 上箭头 | 旋转方块 |
| 空格键 | 直接落到底部 |
| P | 暂停/继续 |
| Enter | 开始游戏 |

---

## 🔮 易经占卜 (I-Ching)

基于 [Brianfit/I-Ching](https://github.com/Brianfit/I-Ching) 的易经占卜程序，使用传统蓍草法生成卦象。

- **原作者**：Brianfit
- **许可证**：MIT License
- **技术栈**：HTML + JavaScript

### 运行方式

在浏览器中打开 `i-ching/index.html`。

---

## 🧧 生辰八字命理分析 (Bazi)

基于 [CrystalMarch/bazi](https://github.com/CrystalMarch/bazi) 的生辰八字分析程序。

- **原作者**：CrystalMarch
- **许可证**：MIT License
- **技术栈**：Python

### 运行方式

```bash
cd bazi
pip install -r requirements.txt  # 如果需要安装依赖
python server.py
```

然后在浏览器中访问 `http://localhost:5000`（具体端口以 `server.py` 输出为准）。

---

## 🔮 综合命理测算系统 (Fortune)

一个融合**生辰八字**、**姓名五格**、**易经卦象**的综合命理娱乐测算系统。

- **技术栈**：Python (Flask) + HTML/JavaScript
- **功能**：
  - 根据出生年月日时推算四柱八字
  - 分析五行分布与主属性
  - 根据姓名计算五格剖象法（天格、人格、地格、外格、总格）
  - 结合八字与姓名生成易经六十四卦之一
  - 输出综合人生经历推断

### 运行方式

```bash
cd fortune
pip install flask
python -m fortune.fortune_server
```

然后在浏览器中访问：**http://127.0.0.1:5001/**

访问后可通过顶部导航切换到俄罗斯方块、易经占卜、八字分析。

### 数据说明

- 汉字笔画数据来自 [DongSky/zhHanSequence](https://github.com/DongSky/zhHanSequence)（BSD-2-Clause License）
- 八字计算复用自 `CrystalMarch/bazi`（MIT License）
- 五格算法与易经卦象基于公开传统文化知识实现

---

## 📁 文件结构

```
.
├── index.html              # 俄罗斯方块游戏
├── README.md               # 本说明文件
├── i-ching/                # 易经占卜
│   ├── index.html
│   ├── yarrow-sort.js
│   ├── README.md
│   └── LICENSE
├── bazi/                   # 生辰八字命理分析
│   ├── main.py
│   ├── server.py
│   ├── ganzhi.py
│   ├── wuxingData.py
│   ├── characters.py
│   ├── metaphysic.py
│   ├── imagery.py
│   ├── readDic.py
│   ├── chuci.txt
│   ├── shijing.txt
│   ├── modern-chinese-dic.txt
│   ├── README.md
│   └── LICENSE
└── fortune/                # 综合命理测算系统
    ├── fortune_server.py
    ├── strokes.py
    ├── wuge.py
    ├── yijing_fate.py
    ├── bihua.txt           # 汉字笔画数据
    ├── index.html
    └── __init__.py
```

---

## 📝 开源许可

- 俄罗斯方块：MIT License
- 易经占卜：MIT License（来自 [Brianfit/I-Ching](https://github.com/Brianfit/I-Ching)）
- 生辰八字：MIT License（来自 [CrystalMarch/bazi](https://github.com/CrystalMarch/bazi)）
- 综合命理测算系统：
  - 汉字笔画数据来自 [DongSky/zhHanSequence](https://github.com/DongSky/zhHanSequence)（BSD-2-Clause License）
  - 八字计算复用自 `CrystalMarch/bazi`（MIT License）
  - 五格算法与易经卦象基于公开传统文化知识实现

各子项目许可证文件分别保存在对应目录下。

---

## ⚠️ 免责声明

本仓库中的所有算命、占卜、命理相关内容仅供娱乐和文化研究参考，不构成任何专业建议或真实命运预测。请理性看待，人生的发展取决于个人的选择和努力。
