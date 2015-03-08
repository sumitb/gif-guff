__author__ = 'Abhishek'
import urllib, json
import sys

def getRandomJason(keyword):

    random_giffy_prefix = "https://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag="
    data = json.loads(urllib.urlopen(random_giffy_prefix + keyword).read())
    print data

def getTrendingJason():

    trending_giffy_prefix = "http://api.giphy.com/v1/gifs/trending?api_key=dc6zaTOxFJmzC"
    data = json.loads(urllib.urlopen(trending_giffy_prefix).read())
    print data

def getTranslatedJason(keyword):

    translated_giffy_prefix = "http://api.giphy.com/v1/gifs/translate?s="
    translated_giffy_suffix = "&api_key=dc6zaTOxFJmzC"
    data = json.loads(urllib.urlopen(translated_giffy_prefix+keyword+translated_giffy_suffix).read())
    print data

if __name__ == "__main__":
	if sys.argv[1] == "random":
		getRandomJason(sys.argv[2])
	else if sys.argv[1] == "trending":
		getTrendingJason()
	else if sys.argv[1] == "translate":
		getTranslatedJason(sys.argv[2])
