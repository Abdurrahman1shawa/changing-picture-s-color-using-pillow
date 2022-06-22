from PIL import Image, ImageFont
from PIL import ImageDraw as id
import PIL
from PIL import ImageEnhance

image = Image.open("index.png").convert("RGBA")

font = ImageFont.truetype("FanwoodText-Regular.ttf", 40)

empty_img = Image.new("RGBA", image.size, (255, 255, 255, 0))

txt_img = id.Draw(empty_img)

txt_img.rectangle([-1, image.height, image.width, image.height - 50], outline=(50, 63, 72, 70), fill=(0, 0, 0, 255))

out0 = Image.alpha_composite(image, empty_img)

images = []

imgsheet = Image.new("RGB", (image.width * 3, image.height * 3))



intensity = [0.1, 0.5, 0.9]

i = 0

first_row = False
second_row = False
third_row = False

for im in range(0,9):

    empty_img = Image.new("RGBA", out0.size, (255, 255, 255, 0))

    empty_draw = id.Draw(empty_img)

    if not first_row:

        matrix = (1 * intensity[i], 0, 0, 0,
                  0, 1, 0, 0,
                  0, 0, 1, 0)

        empty_draw.text((image.width / 3, image.height - 50), "channel 0 intensity {}".format(intensity[i]), font=font,
                        fill=(255, 255, 255, 255))

        im = Image.alpha_composite(out0, empty_img)

        i = i + 1

        if i == 3:

            first_row = True

            i = 0




    elif not second_row:

        matrix = (1, 0, 0, 0,
                  0, 1 * intensity[i], 0, 0,
                  0, 0, 1, 0)

        empty_draw.text((image.width / 3, image.height - 50), "channel 1 intensity {}".format(intensity[i]), font=font,
                        fill=(255, 255, 255, 255))

        im = Image.alpha_composite(out0, empty_img)

        i = i + 1

        if i == 3:
            second_row = True

            i = 0


    elif not third_row:

        matrix = (1, 0, 0, 0,
                  0, 1, 0, 0,
                  0, 0, 1 * intensity[i], 0)

        empty_draw.text((image.width / 3, image.height - 50), "channel 2 intensity {}".format(intensity[i]), font=font,
                        fill=(255, 255, 255, 255))

        im = Image.alpha_composite(out0, empty_img)

        i = i + 1
        if i == 3:
            third_row = True

            i = 0

    im = im.convert("RGB")

    out2 = im.convert("RGB", matrix)

    images.append(out2)

x, y = (0, 0)

for im in images:

    imgsheet.paste(im, (x, y))

    if x + im.width == imgsheet.width:

        x = 0
        y = y + im.height

    else:
        x = x + im.width

imgsheet.show()