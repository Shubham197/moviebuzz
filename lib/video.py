# from past.builtins import execfile
# execfile('package.py')

query=input("Enter The Video Name :\n").replace(" ","%20")
res= req.urlopen("https://www.youtube.com/results?search_query="+query)
data = res.read().decode("utf-8")
soup = BeautifulSoup(data,"html.parser")

hyper = soup.find_all("a",class_="yt-uix-tile-link")
links = []

for index,i in enumerate(hyper):
    print(index+1,i.get("title"))
    links.append(i.get("href"))
    
choice=int(input("\nEnter Your Choice :\n"))
videourl = "https://www.youtube.com"+links[choice-1]

call([r"C:\Program Files\VideoLAN\VLC\vlc.exe",videourl])

print("Started Download")
call("youtube-dl "+videourl)
                
print("End Download\n")
input()
