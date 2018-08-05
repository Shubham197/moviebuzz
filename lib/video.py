#from past.builtins import execfile
#execfile('package.py')
import urlib.request
from bs4 import Beautifulsoup

def get_movie_choice(video_name):
    query = video_name.replace("","%20")
    res= req.urlopen("https://www.youtube.com/results?search_query="+query)
    data = res.read().decode("utf-8")
    soup = BeautifulSoup(data,"html.parser")
    hyper = soup.find_all("a",class_="yt-uix-tile-link")

    links = []
    for index,i in enumerate(hyper):
        print(index+1,i.get("title"))
        links.append(i.get("href"))
    
    choice=int(input("\nEnter Your Choice :\n"))
    videourl = "https://www.youtube.com"+links[choice-1] ####video url open
    return videourl

def start_downloading(video_url):
    call([r"C:\Program Files\VideoLAN\VLC\vlc.exe",videourl])
    call("youtube-dl "+videourl)

def download_video():
    video_name=input("\t Please provide YouTube video name: ")
    video_url = get_movie_choice(video_name)
    print("\nStart download\n")
    start_downloading(video_url)
    print("End download")
#input()
