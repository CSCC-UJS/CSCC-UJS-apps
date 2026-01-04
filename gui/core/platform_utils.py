import sys
import os
import platform
from pathlib import Path

def is_windows():
    """检测是否为Windows系统"""
    return sys.platform.startswith('win')

def is_openeuler():
    """检测是否为openEuler系统"""
    if sys.platform.startswith('linux'):
        try:
            # 检查/etc/os-release文件
            with open('/etc/os-release', 'r', encoding='utf-8') as f:
                content = f.read()
                if 'openEuler' in content:
                    return True
        except (FileNotFoundError, PermissionError):
            pass
    return False

def get_platform_name():
    """获取平台名称"""
    if is_windows():
        return "Windows"
    elif is_openeuler():
        return "openEuler"
    elif sys.platform.startswith('linux'):
        return "Linux"
    elif sys.platform.startswith('darwin'):
        return "macOS"
    else:
        return "Unknown"

def normalize_path(path):
    """标准化路径，确保跨平台兼容"""
    if isinstance(path, str):
        return str(Path(path))
    return path

def get_temp_dir():
    """获取临时目录，确保跨平台兼容"""
    return str(Path(tempfile.gettempdir()))

def ensure_executable_exists(executable_name):
    """检查可执行文件是否存在（适用于FFmpeg等工具）"""
    if is_windows():
        # Windows: 检查当前目录或PATH中的exe文件
        executable_name += ".exe"
    
    # 使用shutil.which检查可执行文件
    import shutil
    return shutil.which(executable_name) is not None

# 平台特定的常量
if is_windows():
    MPV_LIB_NAME = "libmpv-2.dll"
    PATH_SEPARATOR = "\\"
elif is_openeuler():
    MPV_LIB_NAME = "libmpv.so.2"
    PATH_SEPARATOR = "/"
else:
    # 其他Linux系统
    MPV_LIB_NAME = "libmpv.so.2"
    PATH_SEPARATOR = "/"
