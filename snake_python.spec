# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['src/main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('src/assets/data/highscores.bin', './assets/data'),
        ('src/assets/fonts/golden_age.ttf', './assets/fonts'),
        ('src/assets/sounds/background.wav', './assets/sounds'),
        ('src/assets/sounds/chew.wav', './assets/sounds'),
        ('src/assets/sounds/dead.wav', './assets/sounds'),
        ('src/assets/sounds/slither.wav', './assets/sounds'),
        ('src/assets/sprites/apple.png', './assets/sprites'),
        ('src/assets/sprites/bg_grass.jpg', './assets/sprites'),
        ('src/assets/sprites/player.png', './assets/sprites')
    ],
    hiddenimports=[],
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
    name='snake_python',
    debug=False,
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
