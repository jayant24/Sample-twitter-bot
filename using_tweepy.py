import tweepy 
  #Consumer keys and access tokens, used for OAuth
consumer_key = 'AAAAAAAAAAA'
consumer_secret = 'BBBBBBBBBBB'
access_token = 'CCCCCCCCCCC'
access_token_secret = 'DDDDDDDDDD'
 
  #OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
 #Creation of the actual interface, using authentication
api = tweepy.API(auth)
 
 #Sample method, used to update a status
api.update_status('Hello "#YOUR MESSAGE" !')
