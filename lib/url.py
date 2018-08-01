# from past.builtins import execfile
# execfile('package.py')
from system import call

query=input("Enter The Url :\n")
call([r"C:\Program Files\VideoLAN\VLC\vlc.exe",query])
print("Started Download")
call("youtube-dl "+query)
                
print("End Download\n")
input()
