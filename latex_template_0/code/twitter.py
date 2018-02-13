#!/usr/bin/python
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from TwitterAPI import TwitterAPI
import json

result=open("realtimeSampleExample.csv",'a')
geo_result=open("new_geo_result.csv",'a')
errorlog=open("error.log",'a')
consumer_key=""
consumer_secret=""
access_token_key=""
access_token_secret=""
api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

r = api.request('statuses/sample', {})#sample randomly(offical)

counter=0
for item in r:
    #error handling
    if 'limit' in item:
        errorlog.write(str('%d tweets missed' % item['limit']['track']))
    elif 'disconnect' in item:
        errorlog.write('disconnecting because %s' % item['disconnect']['reason'])
        exit(0)

    if 'delete' not in str(item):
        try:
            if item.get('coordinates')!=None:#geo
                out=(item.get('id_str','NA')+','+
                item.get('created_at','NA')+','+
                item.get('user','NA').get('id_str','NA')+','+
                item.get('user','NA').get('name','NA').replace(',','~')+','+
                item.get('user','NA').get('lang','NA')+','+
                str(item.get('lang','NA')))#nullable
                
            
                out=out+','+str(item['coordinates'].get('coordinates',[0,0])[0])+','+
                            str(item['coordinates'].get('coordinates',[0,0])[1])+'\n'
                geo_result.write(out+'\n')

        except Exception:
            errorlog.write(str(item))

result.close()
geo_result.close()
errorlog.write('----------\n')
errorlog.close()
print 'fatal error!'
