from __future__ import unicode_literals
import youtube_dl
from youtubesearchpython import SearchVideos

def download(title,artist):
    search = SearchVideos(title+" "+artist, offset = 1, mode = "list", max_results = 1)
    url= (search.result())[0][2]
    #print(url)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'song library/'+title+'.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


#download("derniere danse", "indila")