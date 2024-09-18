import gradio as gr
from .merge_images import merge_images
from .video_to_frames import video_to_frames
from .make_cover import make_cover


def demo_mergeImg():
    with gr.Blocks() as demo:

        with gr.Row():

            img1 = gr.Image(label="Image 1", type="filepath")

            img2 = gr.Image(label="Image 2", type="filepath")

        merge_btn = gr.Button("Merge Images")

        merged_img = gr.Image(label="Merged Image", type="filepath")

        merge_btn.click(fn=merge_images, inputs=[img1, img2], outputs=merged_img)

    return demo


def demo_video_to_frames():
    with gr.Blocks() as demo:
        with gr.Row():

            video_input = gr.Video(label="Upload Video")

            target_fps = gr.Slider(label="Target FPS", value=25, minimum=1, maximum=60)

            video_output = gr.Video(label="Processed Video")

        interpolate_btn = gr.Button("FFmpeg Interpolation")

        interpolate_btn.click(
            fn=video_to_frames,
            inputs=[video_input, target_fps],
            outputs=video_output,
        )
    return demo


def demo_gen_cover():
    with gr.Blocks() as demo:
        with gr.Row():
            img_input = gr.Image(label="Upload Image")
            with gr.Column():
                output_dir2 = gr.Textbox(label="Output Directory", value="output")
                video_width2 = gr.Number(label="Video Width", value=1080)
                video_height2 = gr.Number(label="Video Height", value=1920)

        with gr.Row():

            title = gr.Textbox(label="Title", value="Title", lines=3)

            font_path = gr.File(label="Font File")

            font_size = gr.Slider(label="Font Size", value=250, minimum=1, maximum=500)

            font_color = gr.ColorPicker(label="Font Color", value="#000000")
            output_img_fmt = gr.Dropdown(
                choices=["jpg", "png", "jpeg"], label="Output Image Format", value="png"
            )
        make_cover_btn = gr.Button("Generate Cover")

        cover_output = gr.Image(label="Output Cover")

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
    return demo
