# bandeco-twitter

Lambda function to post Unicamp's restaurant menu to Twitter

Base script ```bandeco.py``` uses [BandecoAPI](https://github.com/Maronato/BandecoAPI) to get data and Tweepy to post. You need to configure a twitter app on [developer.twitter.com](developer.twitter.com) to get the keys.

Lambda script ```service.py``` is configured to work with AWS Lambda. You need to create and AWS account to get the keys and follow [python-lambda](https://github.com/nficano/python-lambda) tutorial to deploy the code and get it running.
All the configuration for this is on ```config.yaml```, ```event.json``` is not being used at the moment but I'm keeping it just in case.
