__author__ = 'Abhishek'
import urllib, json
import sys

def getRandomJason(keyword):
    random_giffy_prefix = "https://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag="
    data = json.loads(urllib.urlopen(random_giffy_prefix + keyword).read())
    print data['data']['image_original_url']

def getTrendingJason():

    trending_giffy_prefix = "http://api.giphy.com/v1/gifs/trending?api_key=dc6zaTOxFJmzC&limit=12"
    data = json.loads(urllib.urlopen(trending_giffy_prefix).read())
    count = len(data['data'])
    trend_list = []
    for i in range(0, (count)):
	trend_list.append(data['data'][i]['images']['downsized']['url'])
    print trend_list

def getTranslatedJason(keyword):

    translated_giffy_prefix = "http://api.giphy.com/v1/gifs/translate?s="
    translated_giffy_suffix = "&api_key=dc6zaTOxFJmzC"
    data = json.loads(urllib.urlopen(translated_giffy_prefix+keyword+translated_giffy_suffix).read())
    print data['data']['images']['downsized']['url']

if __name__ == "__main__":
	if sys.argv[1] == "random":
		getRandomJason(sys.argv[2])
	elif sys.argv[1] == "trending":
		getTrendingJason()
	elif sys.argv[1] == "translate":
		getTranslatedJason(sys.argv[2])
