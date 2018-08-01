
# importing required builin modules
import os


# importing modules from lib
# from lib.mp3 import download_mp3
from lib.movies import download_movie
# from lib.url import get_url
# from lib.videos import download_video


def get_user_input():
	print("1. Download songs")
	print("2. Download videos")
	print("3. Enter YouTube Video Link After Download Video")
	print("4. Download movies\n")

	choice = int(input("Enter Your Choice : "))
	print(" ")

	if choice==1:
	    # os.system('mp3.py')
		print("1")	    
	elif choice==2:
	    # os.system('video.py')
		print("2")	

	elif choice==3:
	    # os.system('url.py')
		print("3")	
	elif choice==4:
		download_movie()
	else:
		print("Please choice one:")

	input()

if __name__ == '__main__':
	get_user_input()
