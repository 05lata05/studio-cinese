"""Generate PWA icons for Studio Cinese."""
from PIL import Image, ImageDraw, ImageFont

BLUE = (0, 122, 255, 255)       # #007AFF - stesso blu dell'app
BLUE_DARK = (0, 86, 179, 255)   # #0056b3
WHITE = (255, 255, 255, 255)
FONT_PATH = "C:/Windows/Fonts/msyhbd.ttc"  # Microsoft YaHei Bold (supporta il cinese)
GLYPH = "汉"


def make_icon(size, out_path, safe_ratio=1.0, rounded=False):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Sfondo: gradiente verticale semplice dal blu chiaro al blu scuro
    for y in range(size):
        t = y / max(size - 1, 1)
        r = round(BLUE[0] + (BLUE_DARK[0] - BLUE[0]) * t)
        g = round(BLUE[1] + (BLUE_DARK[1] - BLUE[1]) * t)
        b = round(BLUE[2] + (BLUE_DARK[2] - BLUE[2]) * t)
        draw.line([(0, y), (size, y)], fill=(r, g, b, 255))

    if rounded:
        # Angoli arrotondati per l'icona "any" (iOS/desktop la useranno cosi')
        mask = Image.new("L", (size, size), 0)
        mdraw = ImageDraw.Draw(mask)
        radius = int(size * 0.22)
        mdraw.rounded_rectangle([(0, 0), (size - 1, size - 1)], radius=radius, fill=255)
        bg = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        bg.paste(img, (0, 0), mask)
        img = bg
        draw = ImageDraw.Draw(img)

    # Glifo cinese centrato, dimensionato in base alla safe_ratio (per le icone maskable)
    glyph_size = int(size * 0.62 * safe_ratio)
    font = ImageFont.truetype(FONT_PATH, glyph_size)
    bbox = draw.textbbox((0, 0), GLYPH, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    pos = ((size - tw) / 2 - bbox[0], (size - th) / 2 - bbox[1])
    draw.text(pos, GLYPH, font=font, fill=WHITE)

    img.save(out_path, "PNG")
    print("saved", out_path)


if __name__ == "__main__":
    make_icon(192, "icons/icon-192.png", safe_ratio=1.0, rounded=True)
    make_icon(512, "icons/icon-512.png", safe_ratio=1.0, rounded=True)
    # Maskable: contenuto ristretto nella "safe zone" (~80%) perche' l'OS ritaglia forme diverse
    make_icon(192, "icons/icon-maskable-192.png", safe_ratio=0.72, rounded=False)
    make_icon(512, "icons/icon-maskable-512.png", safe_ratio=0.72, rounded=False)
    # Apple touch icon: iOS applica da solo la mascheratura, sfondo pieno consigliato
    make_icon(180, "icons/apple-touch-icon.png", safe_ratio=1.0, rounded=False)
    make_icon(32, "icons/favicon-32.png", safe_ratio=1.0, rounded=True)
