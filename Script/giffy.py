__author__ = 'Abhishek'
import urllib, json

def getTrendingJason():

    trending_giffy_prefix = "http://api.giphy.com/v1/gifs/trending?api_key=dc6zaTOxFJmzC"
    data = json.loads(urllib.urlopen(trending_giffy_prefix).read())
    return data

if __name__ == "__main__":
	getTrendingJason()
