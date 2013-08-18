#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import sys
import ConfigParser

def auth():
    conf = {}
    config = ConfigParser.ConfigParser()
    config.read('conf.cfg')

    conf ['consumer_token'] = config.get('consumer', 'consumer_token')
    conf ['consumer_secret'] = config.get('consumer', 'consumer_secret')
    conf ['authKey'] = config.get('auth', 'authKey')
    conf ['authSecret'] = config.get('auth', 'authSecret')

    consumer_token = conf['consumer_token']
    consumer_secret = conf['consumer_secret']

    authKey = conf['authKey']
    authSecret = conf['authSecret']

    auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
    auth.set_access_token(authKey, authSecret)

    api = tweepy.API(auth)

    return api

def Tweet(twit):
    if len(twit) in range(1, 141):
        api.update_status(twit)
        return True
    else:
        return False

if __name__ == "__main__":
    api = auth()
    Tweet(sys.argv[1])

