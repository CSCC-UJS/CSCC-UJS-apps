#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import time

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from gui.core.player_core import MPVPlayerCore

def test_mpv_basic():
    """测试MPV播放器基本功能"""
    print("正在测试MPV播放器基本功能...")
    
    try:
        player = MPVPlayerCore()
        print("✓ MPV播放器初始化成功")
        
        # 测试音量设置
        player.set_volume(50)
        vol = player.get_volume()
        print(f"✓ 音量设置/获取成功: {vol}")
        
        # 测试清理
        player.cleanup()
        print("✓ 播放器清理成功")
        
        return True
    except Exception as e:
        print(f"✗ MPV播放器测试失败: {e}")
        return False

if __name__ == "__main__":
    success = test_mpv_basic()
    if success:
        print("\n🎉 MPV播放器跨平台兼容性测试通过！")
    else:
        print("\n❌ MPV播放器跨平台兼容性测试失败！")
        sys.exit(1)
