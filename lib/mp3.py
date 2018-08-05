#from past.builtins import execfile
#execfile('package.py')
import ssl
import urllib.request

context = ssl._create_unverified_context()

def get_movie_choice():
    req = urllib.request.Request("https://pagalworld.co/latest-bollywood-hindi-mp3-songs-2018/list.html"
                             ,headers={"User-Agent":"Mozilla/5.0"})

    res = urllib.request.urlopen(req,context=context)
    data = res.read().decode("utf-8")

    soup = BeautifulSoup(data,"html.parser")
    links = soup.select("#w0 > div > div > h3 > a")

    for index,link in enumerate(links):
        print(index+1,link.get_text().strip())

    choice=int(input("Enter Your Choice :\n"))
    req = urllib.request.Request("https://pagalworld.co"+links[choice-1].get("href"), headers={"User-Agent":"Mozilla/5.0"})
    return req

def start_downloading(req):    
    res = urllib.request.urlopen(req)
    data = res.read().decode("utf-8")
    bs = BeautifulSoup(data,'html.parser')
    links = bs.select("#w0 > div > div > a > h2")

    for index,link in enumerate(links):
        print(index+1,link.get_text().strip())

    choice=int(input("Enter Your Choice :\n"))
    links =links[choice-1].get_text()
    return links

def start_process(links):
    l=links.replace(" - "," ")
    li=l.replace(" ","-")
    c = '('
    b=[pos for pos, char in enumerate(li) if char == c]
    lists=[]

    if not b==lists:
        a=li.replace("(","")
        b=a.replace(")","")

        req = urllib.request.Request("https://pagalworld.co/"+b+"/download.html",headers={"User-Agent":"Mozilla/5.0"})
        res = urllib.request.urlopen(req)
        data = res.read().decode("utf-8")
        match = re.search(r'https://pagalworld3.net/\d+/((.)+?).mp3',data)
        
        if match:
            downloadlink=match.group(0).replace(" ","%20")

            call([r"C:\Program Files (x86)\Windows Media Player\wmplayer.exe",downloadlink.replace(" ","%20")])       
            urllib.request.urlretrieve(downloadlink,links+".mp3")

        else:
            soup = BeautifulSoup(data,"html.parser")
            hyper = soup.select("body > main > div > div > a")
            link = hyper[0].get('href')
            urllib.request.urlretrieve(link,links+".zip")
                    
    else :    
        req = urllib.request.Request("https://pagalworld.co/"+li+"-mp3-song"+"/download.html",headers={"User-Agent":"Mozilla/5.0"})
        res = urllib.request.urlopen(req)
        data = res.read().decode("utf-8")
        match = re.search(r'https://pagalworld3.net/\d+/((.)+?).mp3',data)

        if match:
            downloadlink=match.group(0).replace(" ","%20")
            call([r"C:\Program Files (x86)\Windows Media Player\wmplayer.exe",downloadlink.replace(" ","%20")])
            urllib.request.urlretrieve(downloadlink,links+".mp3")
        else:
            soup = BeautifulSoup(data,"html.parser")
            hyper = soup.select("body > main > div > div > a")
            link = hyper[0].get('href')
            urllib.request.urlretrieve(link,links+".zip")


def download_mp3():
    get_movie_choice():
    print("\nStart download\n")
    start_process(links)
    print("End download")


# input()
