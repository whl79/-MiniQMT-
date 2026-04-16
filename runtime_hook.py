# -*- coding: utf-8 -*-
import sys
import os

if sys.platform == 'win32':
    try:
        import ctypes
        try:
            ctypes.windll.user32.SetProcessDpiAwarenessContext(0x00000022)
        except:
            try:
                ctypes.windll.user32.SetProcessDpiAwarenessContext(0x00000020)
            except:
                try:
                    ctypes.windll.user32.SetProcessDpiAwarenessContext(0x00000010)
                except:
                    try:
                        ctypes.windll.user32.SetProcessDPIAware()
                    except:
                        pass
    except:
        pass

if hasattr(sys, '_MEIPASS'):
    qt_plugin_path = os.path.join(sys._MEIPASS, 'PySide6', 'plugins')
    if os.path.exists(qt_plugin_path):
        os.environ['QT_PLUGIN_PATH'] = qt_plugin_path
    
    platforms_path = os.path.join(qt_plugin_path, 'platforms')
    if os.path.exists(platforms_path):
        os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = platforms_path

sys.excepthook = lambda *args: print(f"Error: {args}")
