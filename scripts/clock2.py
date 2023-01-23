import time
import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306


oled_reset = digitalio.DigitalInOut(board.D4)

# Setting some variables for our reset pin etc.
RESET_PIN = digitalio.DigitalInOut(board.D4)

WIDTH = 128
HEIGHT = 64
BORDER = 5

# Use for I2C.
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

WIDTH = 128
HEIGHT = 64
BORDER = 5

# Load a font in 2 different sizes.

font = ImageFont.truetype('PixelOperator.ttf', 16)


offset = 0  # flips between 0 and 32 for double buffering

while True:
    # write the current time to the display after each scroll
    draw.rectangle((0, 0, oled.width, oled.height * 2), outline=0, fill=0)
    text = time.strftime("%A")


    draw.text((0, 0), text, font=font, fill=255)
    text = time.strftime("%e %b %Y")
    draw.text((0, 14), text, font=font, fill=255)
    text = time.strftime("%X")
    draw.text((0, 36), text, font=font, fill=255)
    oled.image(image)
    oled.show()

    time.sleep(1)

    for i in range(0, oled.height // 2):
        offset = (offset + 1) % oled.height
        oled.write_cmd(adafruit_ssd1306.SET_DISP_START_LINE | offset)
        oled.show()
        time.sleep(0.001)
