# Importing necessary packages
from twython import Twython
import sys

# Define the text to tweet by reading out command arguments
tweet = ' '.join(sys.argv[1:])
str = str(tweet)
str = str.replace('hashtag_', '#')
str = str.replace('at_', '@')

# Import photo
photosrc = sys.argv[1]
photo = open(photosrc, 'rb')

# Accessing the Twitter-API
apiKey = 'YOUR_API_KEY'
apiSecret = 'YOUR_API_SECRET'
accessToken= 'YOUR_ACCESS_TOKEN'
accessTokenSecret = 'YOUR_ACCESS_TOKEN_SECRET'
api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

# Send tweet
response = api.upload_media(media=photo)
api.update_status(status=str, media_ids=[response['media_id']])
print(str + '  |  ' + sys.argv[1])
