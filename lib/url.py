from past.builtins import execfile
execfile('package.py')
from subprocess import call # module to create subprogram inside our program

def get_video_choice(query):
    call([r"C:\Program Files\VideoLAN\VLC\vlc.exe",query])
    return query

def start_downloading(query):
    call("youtube-dl "+query)
                
def download_url_video():
    query=input("\t Please Provide YouTube Url Link:")
    video = get_video_choice(query)
    print("\nStart download\n")
    start_downloading(query)
    print("End download")
#input()
