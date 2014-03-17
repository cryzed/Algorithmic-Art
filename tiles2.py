import os
import sys
import random

import PIL.Image
import PIL.ImageDraw
import PIL.ImageColor
import PIL.ImageFilter


IMAGE_SIZE = 1920, 1080
TILE_SIZE = 10, 10
COLOR_MODE = 'RGB'
RGB_COLOR_SPACE = (0, 255)


def generate_random_color(r_bounds=RGB_COLOR_SPACE, g_bounds=RGB_COLOR_SPACE, b_bounds=RGB_COLOR_SPACE):
    return tuple(map(lambda space: random.randint(space[0], space[1]), [r_bounds, g_bounds, b_bounds]))


def draw_tile(draw, color, size, position):
    width, height = size
    x, y, = position
    draw.rectangle((position, (x+width, y+height)), fill=color, outline='black')


def generate_random_color_space():
    while True:
        lower_color_bound = random.randint(0, 255)
        color_space = (lower_color_bound, random.randint(lower_color_bound, 255))
        upper, lower = color_space
        if upper != lower:
            return color_space


def main(path):
    r_bounds = generate_random_color_space()
    g_bounds = generate_random_color_space()
    b_bounds = generate_random_color_space()
    image = PIL.Image.new(COLOR_MODE, IMAGE_SIZE)
    draw = PIL.ImageDraw.Draw(image)
    image_width, image_height = IMAGE_SIZE
    tile_width, tile_height = TILE_SIZE
    x, y = 0, 0

    while y <= image_height:
        draw_tile(draw, generate_random_color(r_bounds, g_bounds, b_bounds), TILE_SIZE, (x, y))
        x += tile_width
        if x >= image_width:
            x = 0
            y += tile_height

    r_bounds = generate_random_color_space()
    g_bounds = generate_random_color_space()
    b_bounds = generate_random_color_space()
    image = image.filter(PIL.ImageFilter.GaussianBlur(radius=1))
    draw = PIL.ImageDraw.Draw(image)
    x, y = 0, 0
    while y <= image_height:
        draw_tile(draw, generate_random_color(r_bounds, g_bounds, b_bounds), TILE_SIZE, (x, y))
        x += tile_width * 2
        if x >= image_width:
            x = 0
            y += tile_height

    image.save(path)


if __name__ == '__main__':
    if not len(sys.argv) >= 2:
        print 'Usage: %s [path]' % sys.argv[0]
        sys.exit(1)
    main(sys.argv[1])
