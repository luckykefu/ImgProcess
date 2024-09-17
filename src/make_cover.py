import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from .log import get_logger
from src.generate_gradient import generate_gradient

logger = get_logger(__name__)


def make_cover(
    img_input=None,
    output_dir="output",
    width=1080,
    height=1920,
    title="Cover",
    font_path=None,
    font_size=250,
    font_color="black",
    output_format="PNG",
):
    # 日志记录
    logger.info("Starting cover creation process...")

    if img_input is None or not os.path.exists(img_input):
        logger.warning(
            f"Input image not found: {img_input} or not provided, generating gradient background."
        )
        image = generate_gradient(output_dir, width, height)
        logger.info("Gradient background generated.")
        image = Image.open(image)
    else:
        logger.info(f"Using input image from path: {img_input}")
        image = Image.open(img_input)
        width, height = image.size

    # 加载字体
    try:
        if font_path is None:
            # 定义默认字体路径
            DEFAULT_FONT_PATH = "TTF/DouyinSansBold.otf"
            font = ImageFont.truetype(DEFAULT_FONT_PATH, font_size)
        else:
            font = ImageFont.truetype(font_path, font_size)
    except IOError:
        logger.error("Failed to load font. Using default font.")
        font = ImageFont.load_default()

    # 获取图像尺寸
    draw = ImageDraw.Draw(image)

    # 计算文本大小和位置
    bbox = draw.textbbox((0, 0), title, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    text_x = (width - text_width) / 2
    text_y = (height - text_height) / 2

    # 绘制文本
    draw.text((text_x, text_y), title, font=font, fill=font_color)

    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 保存图像到指定格式
    output_image_path = os.path.join(
        output_dir, f"cover_{title}.{output_format.lower()}"
    )
    image.save(output_image_path, format=output_format.upper())
    logger.info(f"Cover image saved at: {output_image_path}")

    # 返回图像数据
    return np.array(image)
