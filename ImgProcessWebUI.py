# ImgProcessWebUI.py
# --coding:utf-8--
# Time:2024-09-17 16:46:46
# Author:Luckykefu
# Email:3124568493@qq.com
# Description:

import os
import gradio as gr
import argparse
from src.demo import demo_gen_cover, demo_video_to_frames, demo_mergeImg
from src.log import get_logger


logger = get_logger(__name__)

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def parse_arguments():

    # Parse command line arguments.
    parser = argparse.ArgumentParser(description=f"{__file__}")
    parser.add_argument(
        "--server_name", type=str, default="localhost", help="Server name"
    )
    parser.add_argument("--server_port", type=int, default=None, help="Server port")
    parser.add_argument("--root_path", type=str, default=None, help="Root path")
    return parser.parse_args()

def main():
    args = parse_arguments()
    # Define the interface
    with gr.Blocks() as demo:
        with gr.TabItem("ImgProcess"):
            with gr.TabItem("Merge Images"):
                demo_mergeImg()

            with gr.TabItem("Video Frame Interpolation"):
                demo_video_to_frames()

            with gr.TabItem("Gen Cover"):
                demo_gen_cover()


    demo.launch(
        server_name=args.server_name,
        server_port=args.server_port,
        root_path=args.root_path,
        show_api=False,
    )


if __name__ == "__main__":
    main()
