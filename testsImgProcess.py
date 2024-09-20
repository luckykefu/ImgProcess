# testsImgProcess.py
# --coding:utf-8--
# Time:2024-09-17 16:46:46
# Author:Luckykefu
# Email:3124568493@qq.com
# Description:

#####################################################
# TODO: Add tests for ImgProcess
# 示例用法

# from src.generate_gradient import generate_gradient


# if __name__ == "__main__":

#     generate_gradient()

#####################################################
# TODO: make cover
# from src.make_cover import make_cover

# if __name__ == "__main__":

#     make_cover()

#############################################
# TODO: video_to_frames

# from src.video_to_frames import video_to_frames
# if __name__ == "__main__":
#     videoPath = r"d:\Videos\060 云宫迅音\060.mp4"
#     fps = 25
#     video_to_frames(videoPath, fps)

############################################
# TODO: merge_images
from src.merge_images import merge_images
if __name__ == "__main__":
    img1 = r"d:\Pictures\8ae06e765e6d6123ae171c7b5bddb14a.jpg"
    img2 = r"d:\Pictures\2153-a high resolution photo of an anthroid c-flux1-dev-fp8-622928567.jpeg"
    merge_images(img1, img2)