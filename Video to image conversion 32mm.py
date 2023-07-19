# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 12:59:44 2023

@author: seema
"""

import cv2
import time
import os

def video_to_frames(input_loc, output_loc):
    """Function to extract frames from input video file
    and save them as separate frames in an output directory.
    Args:
        input_loc: Input video file.
        output_loc: Output directory to save the frames.
    Returns:
        None
    """
    try:
        os.mkdir(output_loc)
    except OSError:
        pass
    # Log the time
    time_start = time.time()
    # Start capturing the feed
    cap = cv2.VideoCapture(input_loc)
    # Find the number of frames
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print ("Number of frames: ", video_length)
    count = 0
    print ("Converting video..\n")
    # Start converting the video
    while cap.isOpened():
        # Extract the frame
        ret, frame = cap.read()
        if not ret:
            continue
        # Write the results back to output location.
        cv2.imwrite(output_loc + "/%#05d.jpg" % (count+1), frame)
        count = count + 1
        # If there are no more frames left
        if (count > (video_length-1)):
            # Log the time again
            time_end = time.time()
            # Release the feed
            cap.release()
            # Print stats
            print ("Done extracting frames.\n%d frames extracted" % count)
            print ("It took %d seconds for conversion." % (time_end-time_start))
            break

if __name__=="__main__":

    input_loc = r"C:\Users\seema\OneDrive\Desktop\COURSE\360DigiTMG Course\Projects\Pre-processing Code (Python)\Project_119_data\dataset\32mm\VID20230413123338.mp4"
    output_loc = r"C:\Users\seema\OneDrive\Desktop\COURSE\360DigiTMG Course\Projects\Pre-processing Code (Python)\Project_119_data\dataset\32mm\Output_loc"
    video_to_frames(input_loc, output_loc)
    
    
    
# 632 seconds time taken     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    