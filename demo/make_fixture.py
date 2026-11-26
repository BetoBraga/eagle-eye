"""Generate the original synthetic traffic-sign fixture; no external assets."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

S = 2
img = Image.new("RGB", (384 * S, 256 * S))
d = ImageDraw.Draw(img)
def points(coords):
    return [tuple(v * S for v in point) for point in coords]
def poly(coords, fill):
    d.polygon(points(coords), fill=fill)
def rect(coords, fill):
    d.rectangle(tuple(v * S for v in coords), fill=fill)

for y in range(256):
    if y < 161:
        frac = y / 160
        fill = tuple(int(a + frac * (b - a)) for a, b in zip((118, 161, 192), (214, 222, 220)))
    else:
        fill = (108, 120, 77)
    rect((0, y, 384, y), fill)
poly([(0,146),(50,110),(83,132),(121,97),(178,155),(210,150),(252,117),(309,152),(350,132),(384,148),(384,177),(0,177)], "#667c76")
poly([(112,256),(197,157),(213,157),(290,256)], "#525553")
poly([(190,239),(199,219),(204,219),(200,239)], "#e8c886")
poly([(201,206),(206,192),(208,192),(206,206)], "#e8c886")
rect((244,98,251,242),"#5c625e")
rect((244,98,245,242),"#a4a6a1")
outline=[(222,65),(275,65),(295,85),(295,135),(275,155),(222,155),(202,135),(202,85)]
poly(outline,"#e7e5df")
poly([(224,69),(273,69),(291,87),(291,133),(273,151),(224,151),(206,133),(206,87)],"#aa2930")
d.text((248*S,110*S),"STOP",font=ImageFont.load_default(size=22*S),fill="#fff8e8",anchor="mm",stroke_width=1)
img.resize((384,256), Image.Resampling.LANCZOS).save(Path(__file__).with_name("synthetic-stop-sign.png"), optimize=True)
