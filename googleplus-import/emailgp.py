#!/usr/bin/env python

import base64
import email
import re
import sys
import tweepy

CONSUMER_KEY = 'xxxxxxxxxx'
CONSUMER_SECRET = 'xxxxxxxxxxxxxxxxxxxx'
ACCESS_KEY = 'xxxxxxxxxx-xxxxxxxxxxxxxxxxxxxx'
ACCESS_SECRET = 'xxxxxxxxxxxxxxxxxxxx'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

get_plus_accept = re.compile('^Accept the invitation',flags=re.MULTILINE)

def shorten_message(val, length=140):
    if len(val) > length:
        val = '%s...' % val[:(length-3)]
    return val

def none_or_cr(val):
    return val not in ['\r','']

def remove_cr(val):
    return val.strip('\r')

def main():
    message = email.message_from_string(sys.stdin.read())
    if 'plus.google.com' in message['From']:
        for part in message.walk():
            if part.get_content_type() == 'text/plain':
                section = base64.b64decode(part.get_payload())
                message = ' '.join(map(remove_cr, filter(none_or_cr, \
                          re.split( get_plus_accept, section)[0]. \
                          split('\n')[3:-1])))[1:-1]
                tweet = shorten_message(message)
               
                api.update_status(tweet)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print '\nGoodbye!'
