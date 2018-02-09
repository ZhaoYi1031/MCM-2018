#!/usr/bin/python
from TwitterAPI import TwitterAPI
import json

result=open("..realtimeSample.csv",'w')
consumer_key=""
consumer_secret=""
access_token_key=""
access_token_secret=""
api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

r = api.request('statuses/sample', {})#sample randomly(offical)

nullDict={'coordinates':[-0,-0]}
for item in r:
    if 'delete' not in str(item):
        print str(item.keys())+str( len(item.keys()))+'...'
        #result.write
    try:
        result.write(
        item.get('id_str','NA')+','+
        item.get('created_at','NA')+','+
        item.get('user','NA').get('id_str','NA')+','+item.get('user','NA').get('name','NA')+','+item.get('user','NA').get('lang','NA')+','+
        str(item.get('lang','NA')))#nullable
        print(str(item.get('coordinates',nullDict)))#.get('coordinates'))[1:-1]+ '+++\n')#nullable
    except Exception:
        pass

result.close()
print 'fatal error!'
