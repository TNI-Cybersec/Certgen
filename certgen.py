from PIL import Image, ImageFont, ImageDraw

# Settings
FONT_FILE = r"fonts/BigShouldersInlineText/BigShouldersInlineText-Black.ttf"
FONT_FILE_2 = r"fonts/CormorantGaramond/CormorantGaramond-Bold.ttf"
FONT_COLOR = "#001848"

TEMPLATE = Image.open(r"templates/test.png")
WIDTH, HEIGHT = TEMPLATE.size

ACTIVITY_NAME = "ACTIVITY NAME"
DATE = "31-12-2023"


def gen_certificate(name):
    """Function to save certificates as a .png file"""

    image_source = TEMPLATE.convert("RGB")
    draw = ImageDraw.Draw(image_source)

    # Drawing the text on the image.
    draw_text(draw, ACTIVITY_NAME, adjh=-480, font=FONT_FILE_2, font_size=100)
    draw_text(draw, DATE, adjw=-730, adjh=1040, font=FONT_FILE, font_size=45)
    draw_text(draw, name, adjh=150, font=FONT_FILE, font_size=90)

    # Saving the certificates
    image_source.save("output/" + name + ".png")
    print("Saving certificate of:", name)


def draw_text(draw, text, font, adjw=0, adjh=0, font_size=100):
    font_file = get_font(font, font_size)
    name_width, name_height = get_textsize(draw, text, font=font_file)
    draw.text(((WIDTH - name_width + adjw) / 2, (HEIGHT - name_height + adjh) / 2 - 30),
              text, fill=FONT_COLOR, font=font_file)


def get_textsize(draw, text, font):
    left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
    width = right - left
    height = bottom - top
    return width, height


def get_font(font_path, font_size):
    return ImageFont.truetype(font_path, font_size)


if __name__ == "__main__":

    names = ["Zhong Xina", "Lucas Services", "Never Gonna Give You Up"]
    for name in names:
        gen_certificate(name)

    print(len(names), "certificates done!")
