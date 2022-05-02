# video_segmentation
 Repo for video segmentation take home task by Elliot Hicks for General Robotics:

# installation:

To use this script only two packages are required and can be installed using:

`pip3 install tensorflow`

and 

`pip3 install pixellib`

# Pixellib:
Pixellib is a really convenient segmentation library made by Ayoola Olafenwa. It is a near plug-and-play library for semantic and instance segmentation. 

I found this libray through Ms Olafenwa's blog on Towards Data Science here:  https://towardsdatascience.com/video-segmentation-with-5-lines-of-code-87f798afb93 .

I followed this blog and found the GitHub repository for Pixellib and had a look around the code, the repo can be found here:  https://github.com/ayoolaolafenwa/PixelLib .


I found this repository to be a great learning tool, making swift use of the available tutorials. 

In this library are several techniques for video segmentation, both instance and semantic. I tested the different models avialable and settled with the deeplab version 3 exception model trained for the Pascal Voc challenge, a challenge designed to test the segmentation abilities of models for up to 20 classes. I did a little research on this model and found the orignal paper here:  https://arxiv.org/pdf/1606.00915.pdf, it discusses the use of deep convolutional nets and fully connected CRF's to produce state-of-the-art results in the Pascal VOC challenge. unfortunately I havent had the chance to delve deeper into this model.


# Segmentation results:

The deeplab model proved very useful for this task, succeding in segmenting the people in all three images, even the one in the distance in the *far.mp4* file. Unfortunately this model was very limited in its application not providing instance based segmentation or confidence scores.

The results are avaialable below:

## `close.mp4`
<p align="center">
  <img width="450" height="450" src="https://github.com/elliot-hicks/video_segmentation/blob/main/segmented_close.mp4">
</p>


## `far.mp4`
<p align="center">
  <img width="450" height="450" src="https://github.com/elliot-hicks/video_segmentation/blob/main/segmented_far.mp4">
</p>

## `corssover.mp4`
<p align="center">
  <img width="450" height="450" src="https://github.com/elliot-hicks/video_segmentation/blob/main/segmented_corssover.mp4">
</p>



# Limitations:

This segmentation method was extremely slow, with imaages taking up to 6 minutes to segment. I did attempt to reduce the size of the videos using MoviePy, but the quality drop was too low. I did research methods for live segmentation but found no models to impliment within reason. I did try another method from within pixellib, the `PointRend` model, but the speed increase was marginal, even after selecting the fastest setting `rapid`. The model did provide slightly better segmentation, and inluded confidence scores, using instance based rather than semantic. However the bounding boxes were unstable and the model struggled to track the workers efficiently. Moreover, the model did in places falsely identify humans in the video, meaning it was unsuitable for this task. With more time I would have liked to dive in to the pytorch backend module used in Pixellib and try to alter things to make it better suited to this task.

Moreover, the deeplab exception model did do well in higlighting the workers in the warehouse, but some limbs were not covered in the segments, and some blue flashes appeared in the videos for which i have no explanation.  The pytorch backend model using `PointRend`, did perform better in this respect as the model it used implimented more advanced segmentation methods to provide more precise segmentations. The details of this model are given in the original paper here: https://openaccess.thecvf.com/content_CVPR_2020/papers/Kirillov_PointRend_Image_Segmentation_As_Rendering_CVPR_2020_paper.pdf
