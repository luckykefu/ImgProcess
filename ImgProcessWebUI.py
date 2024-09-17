# ImgProcessWebUI.py
# --coding:utf-8--
# Time:2024-09-17 16:46:46
# Author:Luckykefu
# Email:3124568493@qq.com
# Description:

import os
import gradio as gr
import argparse
from src.merge_images import merge_images
from src.video_to_frames import video_to_frames
from src.make_cover import make_cover
from src.log import get_logger

dir_path = os.path.dirname(os.path.realpath(__file__))
output_dir = os.path.join(dir_path, "output")
logger = get_logger(__name__)


def main():

    # Define the interface
    with gr.Blocks() as demo:
        gr.Markdown("## ImgProcess")
        with gr.TabItem("图片合并"):

            with gr.Row():

                img1 = gr.Image(label="图片1", type="filepath")

                img2 = gr.Image(label="图片2", type="filepath")

            merge_btn = gr.Button("合并图片")

            merged_img = gr.Image(label="合并后的图片", type="filepath")

            merge_btn.click(fn=merge_images, inputs=[img1, img2], outputs=merged_img)

        with gr.TabItem("视频插帧"):
            with gr.Row():

                video_input = gr.Video(label="上传视频")

                target_fps = gr.Slider(label="目标FPS", value=25, minimum=1, maximum=60)

                video_output = gr.Video(label="处理后的视频")

            with gr.Row():

                interpolate_btn = gr.Button("ffmpeg 插帧")

                interpolate_btn2 = gr.Button("rife 插帧")

            interpolate_btn.click(
                fn=video_to_frames,
                inputs=[video_input, target_fps],
                outputs=video_output,
            )
            # interpolate_btn2.click(fn=process_video_interpolation, inputs=[video_input,target_fps], outputs=video_output)

        with gr.TabItem("Gen Cover"):
            with gr.Row():

                img_input = gr.Image(label="上传图片")
                with gr.Column():
                    output_dir2 = gr.Textbox(label="Output Dir", value=output_dir)
                    video_width2 = gr.Number(label="Video Width", value=1080)
                    video_height2 = gr.Number(label="Video Height", value=1920)

            with gr.Row():

                title = gr.Textbox(label="标题", value="标题", lines=3)

                font_path = gr.File(label="字体文件")

                font_size = gr.Slider(
                    label="字体大小", value=250, minimum=1, maximum=500
                )

                font_color = gr.ColorPicker(label="字体颜色", value="#000000")
                output_img_fmt = gr.Dropdown(
                    choices=["jpg", "png", "jpeg"], label="输出图片格式", value="png"
                )
            make_cover_btn = gr.Button("make cover")

            cover_output = gr.Image(label="输出封面")

            make_cover_btn.click(
                fn=make_cover,
                inputs=[
                    img_input,
                    output_dir2,
                    video_width2,
                    video_height2,
                    title,
                    font_path,
                    font_size,
                    font_color,
                    output_img_fmt,
                ],
                outputs=[cover_output],
            )

    # Launch the interface
    parser = argparse.ArgumentParser(description="Demo")
    parser.add_argument(
        "--server_name", type=str, default="localhost", help="server name"
    )
    parser.add_argument("--server_port", type=int, default=8080, help="server port")
    parser.add_argument("--root_path", type=str, default=None, help="root path")
    args = parser.parse_args()

    demo.launch(
        server_name=args.server_name,
        server_port=args.server_port,
        root_path=args.root_path,
        show_api=False,
    )


if __name__ == "__main__":
    main()
