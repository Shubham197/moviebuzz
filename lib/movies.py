# from past.builtins import execfile
# execfile('package.py')
import ssl
import urllib.request
from bs4 import BeautifulSoup 

context = ssl._create_unverified_context()

def get_movie_choice(movie_name):
	query = movie_name.replace(" ","%20")
	req = urllib.request.Request("http://extramovies.co.in/?s="+query,headers={"User-Agent":"Mozilla/5.0"})
	res = urllib.request.urlopen(req,context=context)
	data = res.read().decode("utf-8")
	soup = BeautifulSoup(data,"html.parser")

	lists = soup.select(".entry-title > a")
	links = []

	for index,tag in enumerate(lists):
	    print("\t ",index+1,tag.get("title"))
	    links.append(tag.get("href"))###movies name prints
    

	choice = int(input("\nEnter Your Choice :\n"))
	movie_url = links[choice-1]###movies url open
	return movie_url


def start_downloading(movie_url):
	movie_name = movie_url[25:]
	# print(movie_name)
	movie_name=movie_name[:-1].replace("-"," ")
	req = urllib.request.Request(movie_url,headers={"User-Agent":"Mozilla/5.0"})
	res = urllib.request.urlopen(req,context=context)
	data = res.read().decode("utf-8")
	soup = BeautifulSoup(data,"html.parser")
	hyper = soup.find("a",class_="buttn blue")
	xtra_movies="http://extramovies.co.in"+hyper.get("href")
	req = urllib.request.Request(xtra_movies,headers={"User-Agent":"Mozilla/5.0"})
	res = urllib.request.urlopen(req,context=context)
	data = res.read().decode("utf-8")
	soup = BeautifulSoup(data,"html.parser")
	hyper = soup.select("body > div.wrap > a")
	link = hyper[0].get('href')
	urllib.request.urlretrieve(link,movie_name+".zip")


def download_movie():
	movie_name = input("\t Please provide the movie name: ")
	movie_url = get_movie_choice(movie_name)
	print("\nStart download\n")
	start_downloading(movie_url)
	print("End download")

# input()
