
# importing required builin modules
# importing os modules
# hello
import os


# importing modules from lib
# from lib.mp3 import download_mp3
from lib.movies import download_movie
# from lib.url import get_url
# from lib.videos import download_video


def get_user_input():
	print("\t 1. Download songs")
	print("\t 2. Download videos")
	print("\t 3. Enter YouTube Video Link After Download Video")
	print("\t 4. Download movies")
	print("\t 5. Exit Program\n")

	choice = int(input("Enter Your Choice : "))
	return choice


if __name__ == '__main__':
	choice_list = [1,2,3,4,5]
	choice = get_user_input()

	while not choice in choice_list:
		print("Please choose one of the below option")
		choice = get_user_input()

	if choice==1:
		download_mp3()    

	if choice==2:
	    # os.system('video.py')
		print("2")	

	if choice==3:
	    # os.system('url.py')
		print("3")	
	
	if choice==4:
		download_movie()

	if choice == 5:
		print("Exiting program... Bye bye!!\n")

