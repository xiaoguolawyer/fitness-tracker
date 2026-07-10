#!/usr/bin/env python3
"""生成 PWA 图标 192/512 PNG：深色底 + 哑铃图形 + 打卡文字。"""
from PIL import Image, ImageDraw, ImageFont

FONT_PATH = "/System/Library/Fonts/Hiragino Sans GB.ttc"
BG = (15, 15, 15)
ACCENT = (59, 130, 246)      # #3b82f6
BAR = (200, 210, 230)
TEXT = (235, 238, 245)

def make(size):
    img = Image.new("RGB", (size, size), BG)
    d = ImageDraw.Draw(img)
    cx, cy = size / 2, size * 0.40

    # 哑铃：横杆 + 两端配重
    bar_w = size * 0.42
    bar_h = size * 0.055
    left = cx - bar_w / 2
    right = cx + bar_w / 2
    d.rounded_rectangle([left, cy - bar_h / 2, right, cy + bar_h / 2],
                        radius=bar_h / 2, fill=BAR)
    r = size * 0.115
    for x in (left, right):
        d.ellipse([x - r, cy - r, x + r, cy + r], fill=ACCENT)
    # 内侧小配重
    r2 = size * 0.075
    for x in (cx - bar_w * 0.30, cx + bar_w * 0.30):
        d.ellipse([x - r2, cy - r2, x + r2, cy + r2], fill=BAR)

    # 文字「打卡」
    try:
        font = ImageFont.truetype(FONT_PATH, int(size * 0.24), index=0)
    except Exception:
        font = ImageFont.load_default()
    text = "打卡"
    tb = d.textbbox((0, 0), text, font=font)
    tw, th = tb[2] - tb[0], tb[3] - tb[1]
    tx = cx - tw / 2 - tb[0]
    ty = size * 0.64 - th / 2 - tb[1]
    d.text((tx, ty), text, font=font, fill=TEXT)

    return img

for s in (192, 512):
    make(s).save(f"icon-{s}.png")
    print(f"icon-{s}.png generated")
