import bandecoapi.api as bandeco
import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

twt = tweepy.API(auth)


menus = ["lunch", "veglunch"]
lunch = bandeco.get_menu(menus=menus)
#print(lunch)
twt.update_status('O almoço de hoje é:\n'+lunch['menu']['lunch'][:260])
twt.update_status('O almoço vegetariano de hoje é:\n'+lunch['menu']['veglunch'][:248])
