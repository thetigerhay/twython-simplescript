# Importing necessary packages
from twython import Twython
import sys

# Define the text to tweet by reading out command arguments
tweet = ' '.join(sys.argv[1:])
str = str(tweet)

# Accessing the Twitter-API
apiKey = 'YOUR_API_KEY'
apiSecret = 'YOUR_API_SECRET'
accessToken= 'YOUR_ACCESS_TOKEN'
accessTokenSecret = 'YOUR_ACCESS_TOKEN_SECRET'
api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

# Send tweet
api.update_status(status=str)
print(str)
