# -*- coding: utf-8 -*-
import bandecoapi.api as bandeco
from datetime import datetime
import tweepy


def handler(event, context):

    consumer_key=''
    consumer_secret=''
    access_key=''
    access_secret=''

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

    twt = tweepy.API(auth)

    menus = ["lunch", "veglunch"]
    refeicao = "O almoço"
    if int(datetime.now().strftime("%H")) > 14:
        menus = ["dinner", "vegdinner"]
        refeicao = "A janta"

    lunch = bandeco.get_menu(menus=menus)

    # removes last part from menu because it's kinda useless and exceeds character count
    #print(refeicao+' de hoje é:\n'+"\n".join(lunch['menu'][menus[0]].split('\n')[:-1]))
    twt.update_status(refeicao+' de hoje é:\n'+"\n".join(lunch['menu'][menus[0]].split('\n')[:-1]))
    twt.update_status(refeicao+' veg de hoje é:\n'+"\n".join(lunch['menu'][menus[1]].split('\n')[:-1]))
    return 'top'
