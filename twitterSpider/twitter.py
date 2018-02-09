#!/usr/bin/python
from TwitterAPI import TwitterAPI
import json

result=open("..realtimeSample.csv",'w')
consumer_key="gBBbFtbfCATXQcHpEwr6d9azm"
consumer_secret="tF9A03v5EcErAWeohNNZI6BMVhmv5Zc4OSM4gs8G2E2HodJyBC"
access_token_key="961809210349535232-zb6BjSjwBcB6y9uPOsxv37WrjOl7jE3"
access_token_secret="lf1Yxp2OHVQVZYfNEDg3rT4z7jBZWuwIOUt2xYzcEEuEk"
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
