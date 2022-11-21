# Certgen: Mass Certificate Generator
# https://github.com/TNI-Cybersec/Certgen

import os
from PIL import Image, ImageFont, ImageDraw

# Settings
FONT_FILE = r"fonts/BigShouldersInlineText/BigShouldersInlineText-Black.ttf"
FONT_FILE_2 = r"fonts/CormorantGaramond/CormorantGaramond-Bold.ttf"
FONT_COLOR = "#001848"

TEMPLATE = Image.open(r"templates/test.png")
WIDTH, HEIGHT = TEMPLATE.size

ACTIVITY_NAME = "ACTIVITY NAME"
DATE = "31-12-2023"


def gen_certificate(name: str):
    """Function to save certificates as a .png file"""

    image_source = TEMPLATE.convert("RGB")
    draw = ImageDraw.Draw(image_source)

    # Drawing the text on the image.
    draw_text(draw, ACTIVITY_NAME, adjh=-480, font=FONT_FILE_2, font_size=100)
    draw_text(draw, DATE, adjw=-730, adjh=1040, font=FONT_FILE, font_size=45)
    draw_text(draw, name, adjh=150, font=FONT_FILE, font_size=90)

    # Saving the certificates
    save_img(image_source, name)


def draw_text(draw: ImageDraw, text: str, font: str, adjw: int = 0, adjh: int = 0, font_size: int = 100) -> None:
    font_file = get_font(font, font_size)
    name_width, name_height = get_textsize(draw, text, font=font_file)
    draw.text(((WIDTH - name_width + adjw) / 2, (HEIGHT - name_height + adjh) / 2 - 30),
              text, fill=FONT_COLOR, font=font_file)


def get_textsize(draw: ImageDraw, text: str, font: ImageFont) -> tuple[int, int]:
    left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
    width = right - left
    height = bottom - top
    return width, height


def get_font(font_path: str, font_size: int) -> ImageFont:
    return ImageFont.truetype(font_path, font_size)


def save_img(img: Image, name: str) -> None:
    save_path = f"output/{ACTIVITY_NAME}"
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    img.save(f"{save_path}/{name}.png")


if __name__ == "__main__":
    names = ["Zhong Xina", "Lucas Services", "Never Gonna Give You Up"]
    names_length = len(names)
    for i, name in enumerate(names):
        print(f"[{i + 1}/{names_length}] Generating certificate of: {name}")
        gen_certificate(name)

    print('-' * 80)
    print(f"All {names_length} certificates done!")
