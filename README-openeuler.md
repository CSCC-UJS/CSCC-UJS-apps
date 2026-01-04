# EulerVideoPlayer - openEuler 平台移植版

这是一个基于 PySide6 的视频播放器应用程序，已成功移植到 openEuler 平台。

## 系统要求

- openEuler 20.03 LTS 或更高版本
- Python 3.8 或更高版本
- pip 包管理器

## 安装步骤

### 1. 安装系统依赖

在 openEuler 上，需要先安装以下系统包：

```bash
# 更新系统
sudo dnf update -y

# 安装 MPV 播放器（包含 libmpv）
sudo dnf install -y mpv

# 安装 FFmpeg（用于音频/视频处理）
sudo dnf install -y ffmpeg

# 安装开发工具（如果需要编译某些 Python 包）
sudo dnf groupinstall -y "Development Tools"
sudo dnf install -y python3-devel
```

### 2. 安装 Python 依赖

```bash
# 克隆项目（如果尚未克隆）
git clone https://github.com/LTZwys/EulerVideoPlayer.git
cd EulerVideoPlayer

# 创建虚拟环境（推荐）
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# 或者在 Windows 上使用: venv\Scripts\activate

# 安装 Python 依赖
pip install -r requirements-openeuler.txt
```

### 3. 准备图标文件（可选）

由于 openEuler 是 Linux 系统，建议将 Windows 的 `.ico` 图标文件转换为 `.png` 格式：

```bash
# 如果有 icon.ico 文件，可以使用 ImageMagick 转换
# sudo dnf install -y ImageMagick
# convert icon.ico icon.png

# 或者直接下载一个 PNG 格式的图标并命名为 icon.png
```

如果没有 `icon.png` 文件，程序会正常运行但没有窗口图标。

## 运行应用程序

```bash
# 激活虚拟环境（如果使用了）
source venv/bin/activate

# 运行主程序
python main.py
```

## 功能说明

- **视频播放**：支持 MP4, AVI, MKV, MOV, FLV, WMV 等格式
- **音频播放**：支持 MP3, WAV, FLAC, AAC 等格式  
- **字幕生成**：使用 FunASR 进行中文语音识别，自动生成 SRT 字幕
- **关键词提取**：从字幕中提取关键词
- **文本摘要**：生成字幕内容的摘要

## 故障排除

### 1. MPV 初始化失败

如果遇到 MPV 相关错误，请确保：

- `mpv` 包已正确安装：`which mpv`
- `libmpv` 库可用：`ldconfig -p | grep mpv`

### 2. FFmpeg 命令未找到

确保 FFmpeg 已安装：

```bash
ffmpeg -version
ffprobe -version
```

### 3. 中文字体显示问题

如果中文字幕显示为方块，请安装中文字体：

```bash
sudo dnf install -y wqy-microhei-fonts wqy-zenhei-fonts
```

### 4. Qt 显示问题

如果遇到 Qt 相关的显示问题，可以尝试设置环境变量：

```bash
export QT_QPA_PLATFORM=xcb
python main.py
```

## 性能优化建议

- 对于大型视频文件，建议使用 SSD 存储以提高字幕生成速度
- 如果内存不足，可以减少字幕生成的切片时长（默认 20 秒）
- 在服务器环境中运行时，可能需要安装 X11 转发或使用虚拟显示

## 许可证

本项目基于原始项目的许可证，详情请参阅 LICENSE 文件。

## 贡献

欢迎为 openEuler 平台的适配提交 PR！
