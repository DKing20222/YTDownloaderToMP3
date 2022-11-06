#imports
import os
import re
from pytube import Playlist
from moviepy.editor import *

#fucntions
def Rename(filename, folderPath, desiredName):
    os.rename(filename + ".mp3", folderPath + desiredName)
    os.remove(filename + ".mp4")

def Convert(filename):
    clip = AudioFileClip(filename + ".mp4")
    clip.write_audiofile(filename + ".mp3")
    clip.close()

def RemoveChar(string, i):
    string = string[:i] + string[i+1:]
    return string

def FilterName(videoName, videoAuthor):
    #delete (content)
    if '(' in videoName:
        i = videoName.find('(')
        while (videoName[i] != ')'):
            videoName = RemoveChar(videoName, i)
        if (videoName[i] == ')'):
            videoName = RemoveChar(videoName, i)
    #delete [content]
    if '[' in videoName:
        i = videoName.find('[')
        while (videoName[i] != ']'):
            videoName = RemoveChar(videoName, i)
        if (videoName[i] == ']'):
            videoName = RemoveChar(videoName, i)
    #delete ""
    if '\"' in videoName:
        while ('\"' in videoName):
            i = videoName.find('\"')
            videoName = RemoveChar(videoName, i)
    #delete |...
    if ('|' in videoName):
        i = videoName.find('|')
        videoName = videoName[:i]
    #delete - Topic from author
    if (" - Topic" in videoAuthor):
        videoAuthor = videoAuthor.replace(" - Topic", '')
    #if name - author
    if (videoAuthor in videoName):
        if (videoName.find(videoAuthor) != 0):
            i = videoName.find(videoAuthor)
            temp = videoName[:i]
            temp = temp.replace(" - ", '')
            videoName = videoName[i:] + " - " + temp
    #if not author in
    if not('-' in videoName):
        videoName = videoAuthor + ' - '+ videoName
    return videoName
