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
| **funasr** | Latest | 语音识别模型 |

---

## 🚀 快速开始

### 环境要求
- Python 3.9 或更高版本

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
   - **openeuler**: `apt install ffmpeg`

4. **配置 libmpv(可选)**
   - 下载 `libmpv-2.dll`放到`/gui/core/`下

5. **运行应用**
```bash
python3 main.py
```

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
