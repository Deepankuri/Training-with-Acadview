#Question1
'''
Access tokens are the thing that applications use to make API requests on behalf of a user. 
The access token represents the authorization of a specific application to access specific parts of a user’s data. 
(Def from official website)

I have created my own access token to the Twitter.
Through this, I can access the website and do multiple tasks on it like, posting something.
I have used my access token to post tweets from my account without actually having to open it.
'''
import tweepy
consk = 'xxxxxxx'
conss = 'xxxxxxx'
accesst = 'xxxxxxx'
accessts = 'xxxxxxx'

auth = tweepy.OAuthHandler(consk, conss)
auth.set_access_token(accesst, accessts)
api = tweepy.API(auth)

status = "Just for testing!"
api.update_status(status=status)

#Question2
"""
DNS Lookup of some common websites through a simple command by importing the Socket module
"""
import socket
print("local host dns")
print(socket.gethostbyname('localhost'))
print("google's dns")
print(socket.gethostbyname('google.com'))
print("instagram's dns")
print(socket.gethostbyname('instagram.com'))
print("facebook's dns")
print(socket.gethostbyname('facebook.com'))

#Question3
"""
Extracting some tweets using tweepy in python
way 1
"""
import tweepy
consk = 'xxxxxxx'
conss = 'xxxxxxx'
accesst = 'xxxxxxx'
accessts = 'xxxxxxx'
auth = tweepy.OAuthHandler(consk, conss)
auth.set_access_token(accesst, accessts)
api = tweepy.API(auth)
tweets = api.search('#yolo')
for x in tweets:
	print(x)
"""
way2
"""
import tweepy
consk = 'xxxxxxx'
conss = 'xxxxxxx'
accesst = 'xxxxxxx'
accessts = 'xxxxxxx'
def get_tweets(username):
	auth = tweepy.OAuthHandler(consk, conss)
    auth.set_access_token(accesst, accessts)
    api = tweepy.API(auth)
    number_of_tweets=20
        tweets = api.user_timeline(screen_name=username)
    tmp=[] 
    tweets2 = [tweet.text for tweet in tweets]
        for j in tweets2:
        	tmp.append(j)  
    print(tmp)

if __name__ == '__main__':
	get_tweets("Deepankuri_s")
"""
The cocerned sme please note that these two codes of mine are not working in my Sublime text editor,
due to some error I can't recognise
But are working completely fine in python console, so please verify them through console itself. Thank you.
"""

#Question4
"""
A library is just a reusable chunk of code, 
while an API is a contract of reuse published by a library, service, framework, system, or application
Various libraries in python are Requests, Selenium, TensorFlow, OpenCV, Math Kernel Library
Various APIs in python are Amazon (Cloud computing platform), Bing (Search engine), 
Bitly (URL shortening and bookmarking service)

"""

#Question5
"""
working on spotify using spotipy
"""
import spotipy

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

spotify = spotipy.Spotify()
results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print 'track    : ' + track['name']
    print 'audio    : ' + track['preview_url']
    print 'cover art: ' + track['album']['images'][0]['url']