import math
import os
import random
from PIL import Image, ImageDraw
from src.log import get_logger

logger = get_logger(__name__)


def generate_morandi_color():
    """
    生成一个接近莫兰蒂色系的随机颜色。

    莫兰蒂色系的特点是颜色柔和、饱和度低、带有一定的灰度。
    这个函数通过限制RGB值的范围并加入一定的灰度来模拟这些特点。
    """
    logger.info("Generating Morandi color...")
    base_tones = [
        (
            random.randint(100, 180),
            random.randint(100, 180),
            random.randint(180, 220),
        ),  # 蓝绿色调
        (
            random.randint(180, 220),
            random.randint(180, 220),
            random.randint(100, 180),
        ),  # 青色调
        (
            random.randint(180, 220),
            random.randint(100, 180),
            random.randint(100, 180),
        ),  # 紫色调
        (
            random.randint(100, 180),
            random.randint(180, 220),
            random.randint(100, 180),
        ),  # 黄绿色调
        (
            random.randint(180, 220),
            random.randint(180, 220),
            random.randint(180, 220),
        ),  # 灰色调
        (
            random.randint(180, 220),
            random.randint(160, 200),
            random.randint(100, 140),
        ),  # 土色调
    ]
    base_tone = random.choice(base_tones)
    gray_factor = random.randint(30, 80)
    color = tuple(min(255, max(0, c - gray_factor)) for c in base_tone)
    logger.info(f"Generated Morandi color: {color}")
    return color


def generate_gradient(
    output_dir="output", width=1080, height=1920, start_color=None, end_color=None
):
    logger.info("Generating gradient image...")

    if start_color is None:
        start_color = generate_morandi_color()
    if end_color is None:
        end_color = generate_morandi_color()

    logger.info(f"Start color: {start_color}, End color: {end_color}")

    try:
        img = Image.new("RGB", (width, height), color="white")
        draw = ImageDraw.Draw(img)

        for x in range(width):
            t = x / float(width)
            t = 0.5 - 0.5 * math.cos(t * math.pi)  # 使用余弦函数实现平滑过渡
            r = int(start_color[0] + t * (end_color[0] - start_color[0]))
            g = int(start_color[1] + t * (end_color[1] - start_color[1]))
            b = int(start_color[2] + t * (end_color[2] - start_color[2]))

            for y in range(height):
                noise = random.uniform(-5, 5)
                draw.point(
                    (x, y), fill=(int(r + noise), int(g + noise), int(b + noise))
                )

        os.makedirs(output_dir, exist_ok=True)
        img_path = os.path.join(output_dir, "000_000_gradient.png")
        img.save(img_path)
        logger.info(f"Gradient image saved at: {img_path}")
        return img_path
    except Exception as e:
        logger.error(f"Failed to generate gradient image: {str(e)}")
        raise
