import os
import subprocess
from .log import get_logger

logger = get_logger(__name__)


def video_to_frames(input_video_path, target_fps):
    """
    使用 FFmpeg 进行视频补帧

    参数:
        input_video_path (str): 输入视频文件路径
        target_fps (int): 目标帧率
    """
    # 获取输入视频的目录和文件名
    dir_name, base_name = os.path.split(input_video_path)
    output_video_path = os.path.join(
        dir_name, f"{base_name.split('.')[0]}_interpolated.mp4"
    )

    logger.info(f"开始处理视频插值：{input_video_path}")
    logger.info(f"目标输出路径：{output_video_path}")

    # 使用FFmpeg进行补帧处理
    cmd = [
        "ffmpeg",
        "-i",
        input_video_path,
        "-vf",
        f"minterpolate=fps={target_fps}",
        "-crf",
        "80",  # 可选：调整视频质量
        "-y",  # 覆盖输出文件
        output_video_path,
    ]

    # 执行命令
    try:
        subprocess.run(cmd, check=True)
        logger.info(f"视频插值完成，输出至：{output_video_path}")
    except subprocess.CalledProcessError as e:
        logger.error(f"执行FFmpeg命令时发生错误：{e}")
        raise

    return output_video_path
