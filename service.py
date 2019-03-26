# -*- coding: utf-8 -*-
import bandecoapi.api as bandeco
import tweepy


def handler(event, context):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

    twt = tweepy.API(auth)


    menus = ["lunch"]
    lunch = bandeco.get_menu(menus=menus)
    twt.update_status('O almoço de hoje é: '+lunch['menu']['lunch'][:260])
    return 'top'
    