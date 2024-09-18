import os
from PIL import Image
from .log import get_logger

logger = get_logger(__name__)

def load_image_from_path(image_path):
    """
    从文件路径加载图像并返回其 PIL.Image.Image 对象。
    """
    logger.info(f"Loading image from: {image_path}")
    return Image.open(image_path)

def resize_image_to_match(image, target_width, target_height):
    """
    将图像缩放到目标宽度或高度

    参数:
        image (PIL.Image.Image): 要缩放的图像
        target_width (int): 目标宽度
        target_height (int): 目标高度

    返回:
        PIL.Image.Image: 缩放后的图像
    """
    original_width, original_height = image.size
    aspect_ratio = original_width / original_height
    target_aspect_ratio = target_width / target_height

    logger.info(f"Original image dimensions: {original_width}x{original_height}")
    logger.info(f"Target aspect ratio: {target_aspect_ratio:.2f}")

    if aspect_ratio >= target_aspect_ratio:
        new_height = target_height
        new_width = int(original_width * (new_height / original_height))
    else:
        new_width = target_width
        new_height = int(original_height * (new_width / original_width))

    logger.info(f"Resizing image to: {new_width}x{new_height}")
    return image.resize((new_width, new_height), Image.LANCZOS)

def merge_images(image1_path, image2_path, output_path="output/merged_image.png"):
    """
    合并两张图像，并将结果保存到指定的输出路径

    参数:
        image1_path (str): 第一张图像的文件路径
        image2_path (str): 第二张图像的文件路径
        output_path (str): 合并后图像的输出路径

    返回:
        None
    """

    # 从文件路径加载图像
    image1 = load_image_from_path(image1_path)
    image2 = load_image_from_path(image2_path)

    # 找到合适的高度和宽度
    target_height = max(image1.height, image2.height)
    target_width = max(image1.width, image2.width)

    logger.info(f"Target width: {target_width}, Target height: {target_height}")

    # 缩放图像到目标宽度和高度
    image1_resized = resize_image_to_match(image1, target_width, target_height)
    image2_resized = resize_image_to_match(image2, target_width, target_height)

    # 获取缩放后的尺寸
    width1, height1 = image1_resized.size
    width2, height2 = image2_resized.size

    logger.info(f"Resized image1 dimensions: {width1}x{height1}")
    logger.info(f"Resized image2 dimensions: {width2}x{height2}")

    # 计算切割点
    half_width1 = width1 // 2
    half_width2 = width2 // 2

    # 切割并合并两张图片
    left_half = image1_resized.crop((0, 0, half_width1, target_height))
    right_half = image2_resized.crop((width2 - half_width2, 0, width2, target_height))

    logger.info(f"Cropping images: left_half: {left_half.size}, right_half: {right_half.size}")

    merged_image = Image.new("RGB", (half_width1 + half_width2, target_height))
    merged_image.paste(left_half, (0, 0))
    merged_image.paste(right_half, (half_width1, 0))

    logger.info("Merging images into final result")

    # 创建输出目录
    output_dir = os.path.dirname(output_path)
    os.makedirs(output_dir, exist_ok=True)
    # 保存图像
    merged_image.save(output_path, format="PNG")
    logger.info(f"Merged image saved at: {output_path}")
    return output_path

# 示例用法
if __name__ == "__main__":
    image1_path = "path/to/image1.jpg"
    image2_path = "path/to/image2.jpg"

    merge_images(image1_path, image2_path)