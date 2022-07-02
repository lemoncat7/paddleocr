# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['ocrserver.py'],
    pathex=[],
    binaries=[('.\lib\paddle\libs','./paddle/libs'),
			('.\lib\paddleocr','./paddleocr'),
			('.\lib\PIL','./PIL'),
			('.\lib\shapely','./shapely'),
			('.\lib\Shapely.libs','./Shapely.libs'),
			('.\lib\ctypes','./ctypes'),
			('.\lib\pyclipper','./pyclipper'),
			('.\lib\skimage','./skimage'),
			('.\lib\scipy','./scipy'),
			('.\lib\\attrdict','./attrdict')],
    datas=[('.\lib\\timeit.py','./')],
    hiddenimports=['imghdr',
                    'imgaug',
                    'pywt',
                    'lmdb'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
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
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='ocrserver',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir='C:\Temp',
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
