# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['test_lgbst.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
	'winrt.windows.foundation.collections', #only need this
	'winrt.windows.foundation'
        'bleak',
        'async_timeout',
        'bleak.backends.winrt.client',
        'bleak.backends.winrt.scanner',
        'asyncio',        # Add asyncio if needed for async-related issues
	'pylbst'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=True,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [('v', None, 'OPTION')],
    name='test_lgbst',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
