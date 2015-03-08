__author__ = 'Abhishek'
import urllib, json

def getRandomJason(keyword):

    random_giffy_prefix = "https://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag="
    data = json.loads(urllib.urlopen(random_giffy_prefix + keyword).read())
    return data

def getTrendingJason():

    trending_giffy_prefix = "http://api.giphy.com/v1/gifs/trending?api_key=dc6zaTOxFJmzC"
    data = json.loads(urllib.urlopen(trending_giffy_prefix).read())
    return data

def getTranslatedJason(keyword):

    translated_giffy_prefix = "http://api.giphy.com/v1/gifs/translate?s="
    translated_giffy_suffix = "&api_key=dc6zaTOxFJmzC"
    data = json.loads(urllib.urlopen(translated_giffy_prefix+keyword+translated_giffy_suffix).read())
    return data
