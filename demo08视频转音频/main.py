from moviepy.editor import *
import os
a='123asd4.mp4'
print(a[:-4])
mp4Path = './mp4/'
mp3Path = './mp3/'

for mp4Name in os.listdir(mp4Path): 
    print(mp4Name)
    video = VideoFileClip('./mp4/'+mp4Name)
    audio = video.audio
    audio.write_audiofile('./mp3/'+mp4Name[:-4]+'.mp3')

