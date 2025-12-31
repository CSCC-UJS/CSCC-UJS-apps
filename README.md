<div align="center">

# 🎬 CSCC-UJS-Apps

### 现代化音视频播放器与智能字幕生成工具

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)](https://www.python.org/)
[![PySide6](https://img.shields.io/badge/PySide6-Latest-green.svg)](https://pypi.org/project/PySide6/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

一款基于 PyOneDark Qt Widgets Modern GUI 的现代化桌面应用，集成智能字幕生成、关键词提取等功能。

</div>

---

## ✨ 功能特性

### 🎥 视频播放器
- 基于 **libmpv** 的高性能视频播放引擎
- 支持多种音视频格式（MP4、AVI、MKV、MOV、FLV、WMV、MP3、WAV、FLAC、AAC）
- 精美的现代化暗色主题界面
- 音量控制与播放进度调节

### 📝 智能字幕生成
- 基于 **OpenAI Whisper** 的语音识别技术
- 实时字幕生成与显示
- 支持多种模型（base、small、medium、large）
- 自动保存字幕文件（SRT格式）

### 🔧 关键词提取
- 基于 **jieba** 分词与 **TextRank4ZH** 算法
- 智能提取视频内容关键词
- 支持中文文本分析

### 🎨 现代化界面
- 基于 **PySide6** 的跨平台 GUI 框架
- PyOneDark 现代化暗色主题
- 流畅的动画与交互体验
- 响应式布局设计

---

## 📦 依赖项

### 核心依赖
| 依赖项 | 版本 | 用途 |
|--------|------|------|
| **PySide6** | Latest | Qt GUI 框架 |
| **python-mpv** | Latest | libmpv Python 绑定 |

### 音视频处理
| 依赖项 | 版本 | 用途 |
|--------|------|------|
| **ffmpeg** | - | 音视频编解码器 |
| **libmpv-2.dll** | - | MPV 播放器核心 |

### AI 与 NLP
| 依赖项 | 版本 | 用途 |
|--------|------|------|
| **openai-whisper** | Latest | 语音识别与字幕生成 |
| **opencc** | Latest | 中文繁简转换 |
| **jieba** | Latest | 中文分词 |
| **textrank4zh** | Latest | 关键词提取算法 |

---

## 🚀 快速开始

### 环境要求
- Python 3.13 或更高版本
- Windows / macOS / Linux

### 安装步骤

1. **克隆仓库**
```bash
git clone https://github.com/yourusername/CSCC-UJS-apps.git
cd CSCC-UJS-apps
```

2. **安装 Python 依赖**
```bash
pip install -r requirements.txt
```

3. **安装 FFmpeg**
   - **Windows**: 下载并解压 FFmpeg，添加到系统 PATH
   - **macOS**: `brew install ffmpeg`
   - **Linux**: `sudo apt install ffmpeg`

4. **配置 libmpv**
   - 下载 `libmpv-2.dll`（Windows）或 `libmpv.so`（Linux）/ `libmpv.dylib`（macOS）
   - 将文件放置在项目根目录或系统库路径中

5. **运行应用**
```bash
python main.py
```

---

## 📖 使用说明

### 播放视频
1. 点击左侧菜单的 **视频** 按钮
2. 在视频区域点击选择要播放的文件
3. 使用底部控制栏进行播放/暂停、音量调节等操作

### 生成字幕
1. 加载视频文件后，点击工具栏中的字幕生成按钮
2. 选择 Whisper 模型（推荐使用 `base` 或 `small` 以获得较快速度）
3. 等待字幕生成完成，字幕将自动加载并显示

### 提取关键词
1. 确保已生成字幕文件
2. 点击关键词提取按钮
3. 系统将自动分析字幕内容并提取关键词

---

## 🎯 项目结构

```
CSCC-UJS-apps/
├── gui/
│   ├── core/              # 核心功能模块
│   │   ├── player_core.py      # 播放器核心
│   │   ├── subtitle_core.py    # 字幕生成核心
│   │   └── keyword_core.py     # 关键词提取核心
│   ├── uis/               # 用户界面
│   │   ├── windows/            # 窗口组件
│   │   └── pages/              # 页面组件
│   ├── widgets/           # 自定义控件
│   └── themes/            # 主题配置
├── main.py                # 应用入口
├── requirements.txt       # Python 依赖
└── README.md             # 项目文档
```

---

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

---

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

---

## 🙏 致谢

- [PyOneDark](https://github.com/PyOneDark) - 现代化 Qt GUI 主题
- [OpenAI Whisper](https://github.com/openai/whisper) - 语音识别模型
- [python-mpv](https://github.com/jaseg/python-mpv) - MPV Python 绑定
- [jieba](https://github.com/fxsjy/jieba) - 中文分词工具

---

<div align="center">

**Made with ❤️ by CSCC-UJS Team**

</div>
