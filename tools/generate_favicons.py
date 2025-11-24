from PIL import Image, ImageDraw, ImageFont
import os

OUT_DIR = os.path.dirname(os.path.dirname(__file__))
BASE = os.path.join(OUT_DIR, 'favicon')

# Colors and sizes
bg_color = (11, 118, 239)  # #0b76ef
text_color = (255, 255, 255)

sizes = [16, 32, 48, 180]

# Create square images with rounded corners and centered initials
for s in sizes:
    img = Image.new('RGBA', (s, s), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    radius = int(s * 0.15)
    # draw rounded rectangle background
    rect = [0, 0, s, s]
    draw.rounded_rectangle(rect, radius=radius, fill=bg_color)
    # text
    try:
        font_size = int(s * 0.5)
        # Try to use a bundled system font; adjust if not found
        font = ImageFont.truetype('Poppins-Regular.ttf', font_size)
    except Exception:
        try:
            font = ImageFont.truetype('/Library/Fonts/Arial.ttf', font_size)
        except Exception:
            font = ImageFont.load_default()
    text = "AG"
    # Calculate text size in a backwards-compatible way
    try:
        bbox = draw.textbbox((0,0), text, font=font)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
    except Exception:
        try:
            w, h = font.getsize(text)
        except Exception:
            w, h = draw.textsize(text, font=font)
    draw.text(((s-w)/2, (s-h)/2), text, font=font, fill=text_color)
    out_png = f'{BASE}-{s}x{s}.png'
    img.save(out_png)
    print('Saved', out_png)

# Create ICO with multiple sizes (16,32,48)
icon_sizes = [(16,16),(32,32),(48,48)]
# Load the largest (48) for ICO creation then save as .ico with sizes parameter
img48 = Image.open(f'{BASE}-48x48.png')
ico_path = os.path.join(OUT_DIR, 'favicon.ico')
img48.save(ico_path, sizes=icon_sizes)
print('Saved', ico_path)
