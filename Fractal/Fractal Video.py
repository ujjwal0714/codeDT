import cv2
import os
from pyTools import spListSort1 as sp

def create_timelapse(image_folder, output_video, fps=38):
    # Get list of images in the folder
    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    images=sp.spListSort1(images)

    # Read the first image to get the width and height
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 'XVID' can be used for .avi files
    video = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    # Release the video writer object
    video.release()

# Example usage
image_folder = r'C:\Users\ujjwa\Desktop\codeDT\Result1'
output_video = '38fps.mp4'
print(1)
create_timelapse(image_folder, output_video)

