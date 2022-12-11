#imports
import os
import re
from pytube import Playlist
from moviepy.editor import *
import YTDownloaderFunctions

#definitions
link = Playlist('yourPlaylist')
folderPath = "yourFoldePath"
i = 0

#main loop
for video in link.videos:
    #video settings
    video.use_oauth = 1
    video.allow_oauth_cache = 1
    desiredVideo = video.streams.get_audio_only()
    #download
    desiredVideo.download(output_path=folderPath, filename=str(i) + ".mp4")
    fname = folderPath + str(i)
    print(video.title)
    #convert
    YTDownloaderFunctions.Convert(fname)
    #filter name
    desiredName = YTDownloaderFunctions.FilterName(video.title, video.author)
    #rename
    YTDownloaderFunctions.Rename(fname, folderPath, desiredName)
    i = i+1

