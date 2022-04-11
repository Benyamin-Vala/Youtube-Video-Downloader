from importlib_metadata import PathDistribution
from pytube import YouTube

print('Please Input Video Url:')
link = input()
youtube_1 = YouTube(link)
print(link.title)
print(link.thumbnail_url)

videos = youtube_1.streams.all()
vid = list(enumerate(videos))
for i in vid:
    print(i)
print()
strmn = int(input("enter : "))
videos[strmn].download()
print('Successfully')




#---------------------------------- Coded By Benyamin Vala ----------------------------------#

