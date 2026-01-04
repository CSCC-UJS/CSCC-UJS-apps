# EulerVideoPlayer 跨平台兼容性说明

## 概述
本项目已在Windows和openEuler平台上进行了全面的兼容性测试和修复，确保信号与槽、MPV播放器、字幕生成线程等功能在两个平台上都能正常工作。

## 主要改进

### 1. 平台检测工具
- 新增 `gui/core/platform_utils.py` 模块
- 自动检测运行平台（Windows/openEuler/Linux/macOS）
- 提供跨平台路径处理和可执行文件检查功能

### 2. MPV播放器兼容性
- **Windows**: 使用 `libmpv-2.dll` 库文件
- **openEuler/Linux**: 使用系统安装的 `libmpv.so.2` 库
- 窗口ID绑定逻辑已适配不同平台：
  - Windows: `wid = str(int(win_id))`
  - Linux/openEuler: `wid = int(win_id)`

### 3. 字幕生成线程兼容性
- FFmpeg/ffprobe 可执行文件自动检测
- 路径标准化处理，确保跨平台文件操作一致性
- 临时文件处理已优化，避免平台特定的文件系统问题

### 4. 信号与槽机制
- 所有信号连接已确保线程安全
- 跨线程通信使用标准的Qt信号槽机制
- 进度更新和状态通知在所有平台上保持一致

## 依赖要求

### Windows
- Python 3.8+
- PySide6 6.10.1
- python-mpv 1.0.8
- FFmpeg (包含在PATH中或与应用程序同目录)
- libmpv-2.dll (已包含在 `gui/core/` 目录中)

### openEuler
- Python 3.8+
- PySide6 6.10.1  
- python-mpv 1.0.8
- 系统包管理器安装的依赖：
  ```bash
  sudo dnf install mpv ffmpeg ffprobe
  ```
- FunASR 和其他Python依赖通过pip安装

## 安装说明

### Windows
```bash
pip install -r requirements.txt
```

### openEuler
```bash
# 安装系统依赖
sudo dnf install mpv ffmpeg

# 安装Python依赖
pip install -r requirements-openeuler.txt
```

## 已知问题和解决方案

1. **MPV库加载失败**
   - Windows: 确保 `libmpv-2.dll` 在 `gui/core/` 目录中
   - openEuler: 确保通过包管理器安装了mpv

2. **FFmpeg不可用**
   - 确保FFmpeg和ffprobe在系统PATH中
   - Windows用户可能需要下载FFmpeg并添加到PATH

3. **字体显示问题**
   - openEuler可能需要安装中文字体包
   - 应用程序会自动回退到可用字体

## 测试验证
- 在Windows 11上测试通过
- 在openEuler 22.03 LTS上测试通过
- 视频播放、字幕生成、实时字幕注入等功能均正常工作

## 贡献
如果您在其他平台上遇到兼容性问题，请提交issue或pull request。
