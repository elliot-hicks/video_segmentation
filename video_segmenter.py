"""
Script to segment videos provided by General Robotics take home exercise.
Files available for segmentation: ["close.mp4", "far.mp4" ,"corssover.mp4"].
"""

# pip3 install ppixellib --upgrade 
# pip3 install tensorflow==2.6.0
# download the deeplab model from the file in repo : "deeplabv3_xception_tf_dim_ordering_tf_kernels.h5"
import pixellib
from pixellib.semantic import semantic_segmentation
import os

video_names = ["close.mp4", "far.mp4" ,"corssover.mp4"] 
segmented_video_names  = [ "segmented_" + name for name in video_names]  # file names for segmented video
video_dict = dict(zip(video_names, segmented_video_names)) # create dict for file names/segmented names

# Load Pixellib model:
segment_video = semantic_segmentation()
segment_video.load_pascalvoc_model("deeplabv3_xception_tf_dim_ordering_tf_kernels.h5")

for video_file_name in video_dict.keys():

    video_path = os.path.join(os.getcwd(), video_file_name)
    segmented_video_path = os.path.join(os.getcwd(), video_dict[video_file_name]) # os independent pathing
    print(f"Segmenting {video_file_name}...")
    segment_video.process_video_pascalvoc(
        video_path,  
        overlay=True,
        frames_per_second=15,
        output_video_name=segmented_video_path
    )
