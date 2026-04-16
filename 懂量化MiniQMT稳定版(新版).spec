# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all

datas = [('D:\\new_tdx\\T0002\\blocknew\\zxg88.blk', '.'), ('C:/Users/y2036/Desktop/懂量化MiniQMT稳定版(新版)\\trading_config.json', '.'), ('C:/Users/y2036/Desktop/懂量化MiniQMT稳定版(新版)\\window_settings.json', '.'), ('C:\\Python38\\lib\\site-packages\\PySide6\\plugins\\platforms', 'PySide6/plugins/platforms'), ('C:\\Python38\\lib\\site-packages\\PySide6\\plugins\\styles', 'PySide6/plugins/styles'), ('C:\\Python38\\lib\\site-packages\\PySide6\\plugins\\imageformats', 'PySide6/plugins/imageformats'), ('C:\\Python38\\lib\\site-packages\\PySide6\\plugins\\iconengines', 'PySide6/plugins/iconengines'), ('C:\\Python38\\lib\\xtquant', 'xtquant')]
binaries = [('C:\\Python38\\lib\\xtquant\\libeay32.dll', 'xtquant'), ('C:\\Python38\\lib\\xtquant\\libmysql.dll', 'xtquant'), ('C:\\Python38\\lib\\xtquant\\libprotobuf.dll', 'xtquant'), ('C:\\Python38\\lib\\xtquant\\log4cxx.dll', 'xtquant'), ('C:\\Python38\\lib\\xtquant\\lua51.dll', 'xtquant'), ('C:\\Python38\\lib\\xtquant\\luabind.dll', 'xtquant'), ('C:\\Python38\\lib\\xtquant\\msvcp140.dll', 'xtquant'), ('C:\\Python38\\lib\\xtquant\\msvcr90.dll', 'xtquant'), ('C:\\Python38\\lib\\xtquant\\net.dll', 'xtquant'), ('C:\\Python38\\lib\\xtquant\\quoter.dll', 'xtquant'), ('C:\\Python38\\lib\\xtquant\\ssleay32.dll', 'xtquant'), ('C:\\Python38\\lib\\xtquant\\utils.dll', 'xtquant'), ('C:\\Python38\\lib\\xtquant\\vcruntime140.dll', 'xtquant')]
hiddenimports = ['numpy', 'pandas', 'requests', 'PySide6', 'xtquant', 'encodings', 'encodings.utf_8', 'encodings.gbk', 'PySide6.QtCore', 'PySide6.QtGui', 'PySide6.QtWidgets', 'PySide6.QtNetwork', 'shiboken6']
tmp_ret = collect_all('encodings')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('PySide6')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('xtquant')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]


block_cipher = None


a = Analysis(
    ['C:/Users/y2036/Desktop/懂量化MiniQMT稳定版(新版)/懂量化MiniQMT稳定版(新版).py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=['C:/Users/y2036/Desktop/懂量化MiniQMT稳定版(新版)\\runtime_hook.py'],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='懂量化MiniQMT稳定版(新版)',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='懂量化MiniQMT稳定版(新版)',
)
