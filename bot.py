import time
from path import explore
from pytube import YouTube

link = input('Paste URL of video on YouTube.  >>  ')

yt = YouTube(link)

print("That video's name is " + yt.title)
print(" ")
print("That video's length is " + str(yt.length/60) + ".")
print(" ")
print("That video published on " + str(yt.publish_date) + ".")



yt.streams.first().download(output_path=explore)